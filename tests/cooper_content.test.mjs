import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
const data=JSON.parse(fs.readFileSync(new URL('../src/content.json',import.meta.url),'utf8'));
const b=data.courses.find(c=>c.id==='cooper-aba-3');
const lessons=b.topics.filter(t=>t.kind!=='glossary');
const outline=data.courses.find(c=>c.id==='bcba-6');
const reference=JSON.parse(fs.readFileSync(new URL('../docs/original-outline-baseline.json',import.meta.url),'utf8'));
test('Original BCBA curriculum remains deeply identical, not merged or replaced',()=>assert.deepEqual(outline,reference));
test('Book has all 31 chapters, 13 parts, 170 section lessons and one glossary appendix',()=>{
 assert.equal(b.chapters.length,31);assert.equal(b.parts.length,13);assert.equal(lessons.length,170);assert.equal(b.topics.length,171);
 for(let n=1;n<=31;n++){assert.ok(lessons.some(t=>t.chapter===n));assert.equal(b.chapters[n-1].number,n);}
});
test('Book lessons have 661 concepts, substantial notes, safe IDs, and source page ranges',()=>{
 assert.equal(lessons.reduce((n,t)=>n+t.concepts.length,0),661);
 for(const t of lessons){assert.match(t.id,/^C\d{2}\.\d{2}$/);assert.ok(t.summary.length>60);assert.ok(t.concepts.length>=2);assert.ok(t.takeaway.length>30);assert.equal(t.pages.pdfStart,t.pages.start+18);assert.equal(t.pages.pdfEnd,t.pages.end+18);assert.ok(t.pages.start<=t.pages.end);assert.ok(t.pages.start>=b.chapters[t.chapter-1].start);assert.ok(t.pages.end<=b.chapters[t.chapter-1].end);}
});
test('All 170 original scenarios have four choices and four nonempty choice-specific rationales',()=>{
 const ids=new Set(),positions=[0,0,0,0];
 for(const t of lessons){const s=t.scenario;assert.ok(s.prompt.length>30);assert.equal(s.options.length,4);assert.equal(new Set(s.options).size,4);assert.equal(s.rationales.length,4);assert.ok(s.rationales.every(r=>r.length>15));assert.equal(s.rationales[s.correctIndex],s.explanation);assert.ok(!ids.has(s.id));ids.add(s.id);positions[s.correctIndex]++;}
 assert.deepEqual(positions,[43,43,42,42]);
});
test('Glossary preserves 521 distinct entries and 516 definition cards, excluding See-only aliases',()=>{
 assert.equal(b.glossary.length,521);assert.equal(new Set(b.glossary.map(e=>e.term)).size,521);
 const t=b.topics.find(t=>t.kind==='glossary');assert.equal(t.cards.length,516);assert.equal(t.scenario,null);assert.deepEqual(t.tasks,[]);
 assert.ok(b.glossary.some(e=>e.term==='A-B-A-B design'));assert.ok(b.glossary.some(e=>e.term==='Good Behavior Game'));
 for(const c of t.cards){assert.ok(c.answer.trim());assert.ok(!c.answer.startsWith('See '));assert.ok(c.pages.start>=786&&c.pages.end<=803);}
});
test('All 1177 book card IDs are distinct and do not collide with original curriculum',()=>{
 const cards=b.topics.flatMap(t=>t.cards),old=new Set(outline.topics.flatMap(t=>t.cards.map(c=>c.id)));assert.equal(cards.length,1177);assert.equal(new Set(cards.map(c=>c.id)).size,1177);assert.ok(cards.every(c=>!old.has(c.id)));
});
test('The separate 104-task crosswalk explicitly reports partial and unmapped coverage',()=>{
 assert.equal(b.crosswalk.length,104);assert.equal(b.crosswalk.filter(r=>r.status==='related').length,79);assert.equal(b.crosswalk.filter(r=>r.status==='partial').length,21);assert.equal(b.crosswalk.filter(r=>r.status==='not-mapped').length,4);
 const ids=new Set(b.topics.map(t=>t.id));const taskIDs=new Set(outline.topics.map(t=>t.id));
 for(const r of b.crosswalk){assert.ok(taskIDs.has(r.id));assert.ok(r.topics.every(id=>ids.has(id)));if(r.status==='not-mapped')assert.equal(r.topics.length,0);}
 for(const t of lessons)assert.ok(t.tasks.every(code=>taskIDs.has(code)));
});
test('Source archive has all 908 pages and 15 original page images with correct indexing',()=>{
 assert.equal(b.reader.length,908);assert.equal(Object.keys(b.pageImages).length,15);b.reader.forEach((p,n)=>assert.equal(p.pdf,n+1));assert.equal(b.reader[19].printed,2);assert.equal(b.reader[803].printed,786);
 for(const [pdf,img] of Object.entries(b.pageImages)){assert.ok(+pdf>=1&&+pdf<=908);assert.match(img,/^data:image\/webp;base64,/);}
});
test('Source inconsistencies and historical ethics are disclosed rather than silently corrected',()=>{
 assert.match(b.provenance,/5th Edition/);assert.match(b.coverage.scope,/not every paragraph/i);
 assert.match(lessons.find(t=>t.id==='C16.01').sourceNote,/inconsistency/);
 assert.ok(lessons.filter(t=>t.chapter===31).every(t=>t.sourceNote.includes('earlier Professional and Ethical Compliance Code')));
});
