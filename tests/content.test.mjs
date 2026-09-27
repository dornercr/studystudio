import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const content=JSON.parse(fs.readFileSync(path.join(root,'src/content.json'),'utf8'));
const supplied=JSON.parse(fs.readFileSync(path.join(root,'docs/supplied-outline.json'),'utf8'));
const course=content.courses.find(c=>c.id==='bcba-6');
test('Preserves every supplied topic ID, title, domain, link, and order',()=>{
  assert.equal(course.topics.length,104);
  assert.deepEqual(course.topics.map(({id,title,domain,source})=>({id,title,domain,source})),supplied.topics);
  assert.deepEqual(course.domains,supplied.domains);
});
test('Has the exact nine supplied domain sizes',()=>{
  const counts=Object.fromEntries(course.domains.map(d=>[d.id,course.topics.filter(t=>t.domain===d.id).length]));
  assert.deepEqual(counts,{A:5,B:24,C:12,D:9,E:12,F:8,G:19,H:8,I:7});
});
test('Contains 220 nonempty flashcards with unique IDs',()=>{
  const cards=course.topics.flatMap(t=>t.cards);
  assert.equal(cards.length,220);assert.equal(new Set(cards.map(c=>c.id)).size,220);
  for(const c of cards){assert.ok(c.question.trim());assert.ok(c.answer.trim());}
});
test('All 104 topics have a valid original scenario and rationale',()=>{
  const ids=new Set();
  for(const t of course.topics){const s=t.scenario;assert.ok(s?.prompt?.trim());assert.ok(s.explanation.trim());assert.equal(s.options.length,4);assert.equal(new Set(s.options).size,4);assert.ok(Number.isInteger(s.correctIndex)&&s.correctIndex>=0&&s.correctIndex<4);assert.ok(!ids.has(s.id));ids.add(s.id);}
  assert.equal(ids.size,104);
});
test('Correct-answer positions are balanced, not always option A',()=>{
  const counts=[0,0,0,0];for(const t of course.topics)counts[t.scenario.correctIndex]++;
  assert.deepEqual(counts,[26,26,26,26]);
});
test('Notes are substantial and provenance is explicit',()=>{
  assert.match(course.provenance,/article bodies were not retrieved/);
  assert.match(course.provenance,/original supplemental/);
  for(const t of course.topics){assert.equal(t.origin,'original-supplement');assert.ok(t.summary.length>40);assert.ok(t.concepts.length>=2);assert.ok(t.takeaway.length>20);}
});
test('Built app embeds content, Tailwind, and application code with no external runtime',()=>{
  const html=fs.readFileSync(path.join(root,'dist/index.html'),'utf8');
  assert.match(html,/tailwindcss v4\.1\.10/);assert.match(html,/study-studio:v1/);
  assert.ok(!html.includes('/*__CONTENT__*/'));assert.ok(!html.includes('/*__APP_JS__*/'));
  assert.ok(!/<script[^>]+src=/i.test(html));assert.ok(!/<link[^>]+rel=["']stylesheet/i.test(html));
});
test('Personal material starts empty, not with misleading demo progress',()=>{
  const custom=content.courses.find(c=>c.id==='my-material');assert.ok(custom);assert.equal(custom.topics.length,0);
});
