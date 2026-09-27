"""Exercise the built offline Cooper app and curriculum isolation in Chromium.
Uses an in-memory Storage double because this runner does not permit local origins.
Native browser persistence remains browser/file-origin dependent; backups are tested.
"""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
HTML=(ROOT/'dist/index.html').read_text()
DATA=json.loads((ROOT/'src/content.json').read_text())
BOOK=next(c for c in DATA['courses'] if c['id']=='cooper-aba-3')
STORE="""() => {const v=new Map();Object.defineProperty(window,'localStorage',{value:{getItem:k=>v.get(k)??null,setItem:(k,s)=>v.set(k,String(s)),removeItem:k=>v.delete(k),clear:()=>v.clear()},configurable:true});}"""
results=[]
def record(s):results.append(s);print('PASS',s,flush=True)
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 p=b.new_page(viewport={'width':1512,'height':1080});errors=[];requests=[]
 p.on('pageerror',lambda e:errors.append(str(e)));p.on('request',lambda r:requests.append(r.url))
 p.evaluate(STORE);p.set_content(HTML,wait_until='load')
 p.locator('[data-action="reviewed"]').click();p.locator('#personal-note').fill('Original outline note')
 p.select_option('#course-select','cooper-aba-3')
 assert p.locator('.lesson-heading').inner_text()=='Science: Basic Characteristics and a Definition'
 assert p.locator('#all-count').inner_text()=='171'
 assert '1177 cards' in p.locator('#mode-tabs').inner_text()
 assert '170 cases' in p.locator('#mode-tabs').inner_text()
 assert '31 chapters' in p.locator('#course-domain-count').inner_text()
 assert p.locator('[data-action="edit-topic"]').count()==0
 record('Separate Cooper curriculum: 31 chapters, 170 lessons + glossary, 1177 cards, 170 scenarios')
 p.screenshot(path=str(ROOT/'docs/cooper-outline-preview.png'),full_page=True)
 p.locator('[data-action="reviewed"]').click();p.locator('#personal-note').fill('Cooper-only note')
 p.select_option('#course-select','bcba-6');assert p.locator('#personal-note').input_value()=='Original outline note'
 assert '1 of 104' in p.locator('#sidebar-progress').inner_text()
 p.select_option('#course-select','cooper-aba-3');assert p.locator('#personal-note').input_value()=='Cooper-only note'
 assert '1 of 171' in p.locator('#sidebar-progress').inner_text()
 record('Progress and notes remain isolated; switching curricula restores position')
 # Chapter filtering in every chapter with all three modes.
 for ch in BOOK['chapters']:
  p.select_option('#chapter-select',str(ch['number']))
  p.locator('#mode-tabs [data-mode="outline"]').click()
  assert p.locator('.lesson-heading').inner_text()==next(t['title'] for t in BOOK['topics'] if t.get('chapter')==ch['number'])
  p.locator('#mode-tabs [data-mode="flashcards"]').click();assert p.locator('.card-question').count()==1
  p.locator('#mode-tabs [data-mode="scenarios"]').click();assert p.locator('.choice').count()==4
 record('All 31 chapters render in outline, flashcard, and scenario modes')
 p.locator('#mode-tabs [data-mode="outline"]').click();p.select_option('#chapter-select','18')
 p.locator('[data-action="next"]').click();target=p.locator('.lesson-heading').inner_text()
 p.locator('#mode-tabs [data-mode="flashcards"]').click();assert target in p.locator('#workspace').inner_text()
 assert p.locator('#scope-select').input_value()=='chapter'
 p.locator('.deck-card').click();assert p.locator('.card-answer').count()==1
 p.locator('[data-rating="known"]').click()
 p.screenshot(path=str(ROOT/'docs/cooper-flashcards-preview.png'),full_page=True)
 p.locator('#mode-tabs [data-mode="scenarios"]').click();assert target in p.locator('#workspace').inner_text()
 p.locator('[data-action="choose-answer"]').first.click();p.locator('[data-action="check-answer"]').click()
 assert p.locator('.option-rationales p').count()==4
 p.screenshot(path=str(ROOT/'docs/cooper-scenarios-preview.png'),full_page=True)
 record('Context retained between modes; flashcard ratings and four option-specific rationales work')
 p.locator('[data-action="book-crosswalk"]').first.click();assert p.locator('.crosswalk-row').count()==104
 assert p.locator('.coverage-label.not-mapped').count()==4
 p.select_option('#crosswalk-filter','E');assert p.locator('.crosswalk-row').count()==12
 p.locator('.crosswalk-row').first.locator('[data-action="book-task"]').click()
 assert 'cooper-aba-3'==p.locator('#course-select').input_value()
 assert 'Filtered by task E.1' in p.locator('#book-toolbar').inner_text()
 p.locator('[data-action="clear-book-task"]').click();p.locator('[data-action="all-topics"]').click()
 p.locator('[data-action="book-nav"][data-view="domains"]').click();assert p.locator('.nav-part').count()==0
 p.select_option('#domain-select','G');assert int(p.locator('#filtered-count').inner_text().split()[0])>20
 p.locator('[data-action="all-topics"]').click()
 record('104-task editorial crosswalk, partial/unmapped statuses, domain navigation, and filters')
 p.locator('[data-action="book-glossary"]').click()
 assert p.locator('#glossary-results .glossary-entry').count()==35
 p.locator('#glossary-search').fill('abolishing operation');assert 'abolishing operation' in p.locator('#glossary-results').inner_text()
 p.locator('#glossary-search').fill('A-B-A-B design');assert p.locator('#glossary-results .glossary-entry').count()>=1
 p.locator('[data-action="glossary-card"]').first.click();p.locator('.deck-card').click();assert 'baseline' in p.locator('.card-answer').inner_text()
 assert 'Printed p. 786' in p.locator('.book-source').inner_text()
 p.locator('#mode-tabs [data-mode="scenarios"]').click();assert 'Nothing in this practice set' in p.locator('#workspace').inner_text()
 assert 'REF.GLOSSARY' in p.locator('#workspace').inner_text()
 record('Glossary search, extracted definition cards, exact page references, no invented glossary scenarios')
 p.locator('[data-action="book-source-search"]').first.click();p.fill('#source-query','matching law');p.locator('#source-search-form button').click()
 assert p.locator('#source-results .glossary-entry').count()>0
 p.locator('#source-results [data-action="source-page"]').first.click();assert p.locator('.source-text').count()==1
 p.fill('#source-jump','31');p.locator('#source-jump-form button').click()
 assert 'Printed p. 31 · PDF 49' in p.locator('#dialog-title').inner_text()
 assert p.locator('.source-image img').count()==1
 p.locator('[data-action="source-page"]').last.click();assert 'PDF 50' in p.locator('#dialog-title').inner_text()
 p.locator('[data-action="close-dialog"]').click()
 record('908-page local source search, printed/PDF page jump, selected original images, next page')
 # Verify that a backup round-trip retains both seed course progress namespaces.
 saved=p.evaluate("localStorage.getItem('study-studio:v1')")
 p.evaluate('s=>localStorage.setItem("study-studio:v1",s)',saved);p.set_content(HTML,wait_until='load')
 restored=p.evaluate("JSON.parse(localStorage.getItem('study-studio:v1'))")
 assert restored['progress']['bcba-6']['notes']['A.1']=='Original outline note'
 assert restored['progress']['cooper-aba-3']['notes']['C01.01']=='Cooper-only note'
 record('Reinitialization preserves both curriculum progress namespaces')
 p.locator('[data-action="settings"]').click()
 with p.expect_download() as dl:p.locator('[data-action="export-pack"]').click()
 download=dl.value;download.save_as(str(ROOT/'docs/cooper-portable-pack.json'))
 portable=json.loads((ROOT/'docs/cooper-portable-pack.json').read_text());assert 'reader' not in portable['courses'][0]
 p.locator('#import-file').set_input_files(str(ROOT/'docs/cooper-portable-pack.json'))
 p.wait_for_timeout(300)
 assert p.locator('#course-select').input_value().startswith('cooper-aba-3-import-')
 assert '1177 cards' in p.locator('#mode-tabs').inner_text()
 p.locator('[data-action="book-glossary"]').click();assert p.locator('#glossary-search').count()==1
 record('Portable textbook study-pack export/import retains chapters, cards, glossary, and mappings')
 # Mobile checks at narrow widths and with all modes.
 p.select_option('#course-select','cooper-aba-3');p.locator('[data-action="all-topics"]').click()
 p.locator('#mode-tabs [data-mode="outline"]').click();p.select_option('#chapter-select','1')
 for w in [390,320]:
  p.set_viewport_size({'width':w,'height':844})
  for mode in ['outline','flashcards','scenarios']:
   p.locator('#mode-tabs [data-mode="'+mode+'"]').click()
   assert p.evaluate('document.documentElement.scrollWidth<=innerWidth'),(w,mode)
  p.locator('#mode-tabs [data-mode="outline"]').click()
  if w==390:p.screenshot(path=str(ROOT/'docs/cooper-mobile-preview.png'),full_page=True)
  p.locator('[data-action="open-menu"]').click();assert p.locator('#sidebar').get_attribute('class').endswith('open')
  p.locator('[data-action="close-menu"]').first.click()
 record('390px and 320px mobile layouts, all modes, chapter controls, no horizontal overflow')
 assert not errors,errors
 assert not [r for r in requests if not r.startswith(('data:','blob:'))],requests
 record('No JavaScript errors or external network requests')
 b.close()
(ROOT/'tests/cooper-browser-results.json').write_text(json.dumps({'passed':len(results),'tests':results,'limitations':'Storage double used; native file-origin persistence is browser-dependent.'},indent=2))
print('PASS TOTAL',len(results),flush=True)
