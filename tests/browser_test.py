"""UI integration tests using Chromium.
The execution environment blocks file:// and loopback navigation. We therefore
render the exact built HTML with set_content and use a standards-shaped in-memory
Storage double. This exercises save/restore logic, not native file-origin storage.
No changes are made to the delivered app.
"""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
HTML=(ROOT/'dist/index.html').read_text()
DATA=json.loads((ROOT/'src/content.json').read_text())['courses'][0]
STORE_JS="""() => {
  const values = new Map();
  const storage = {getItem:k=>values.has(String(k))?values.get(String(k)):null,
    setItem:(k,v)=>values.set(String(k),String(v)), removeItem:k=>values.delete(String(k)),
    clear:()=>values.clear(), key:i=>[...values.keys()][i]??null,
    get length(){return values.size}};
  Object.defineProperty(window,'localStorage',{value:storage,configurable:true});
}"""
results=[]
def record(name):
    results.append(name)
    print('PASS',name)
def settle(page):page.wait_for_timeout(350)
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1512,'height':1080},device_scale_factor=1)
    errors=[]; requests=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.on('request',lambda r:requests.append(r.url))
    page.evaluate(STORE_JS)
    page.set_content(HTML,wait_until='load');settle(page)
    assert page.locator('.lesson-heading').inner_text()=='Description, Prediction, Control'
    assert page.locator('#all-count').inner_text()=='104'
    assert '220 cards' in page.locator('#mode-tabs').inner_text()
    assert '104 cases' in page.locator('#mode-tabs').inner_text()
    assert 'Saved on this device' in page.locator('#save-status').inner_text()
    assert not page.locator('.storage-warning').count()
    record('Initial render: 104 topics / 220 cards / 104 scenarios')
    page.evaluate('window.scrollTo(0,0)');page.screenshot(path=str(ROOT/'docs/preview-outline.png'),full_page=True)
    page.locator('[data-action="next"]').click();assert 'Philosophical Assumptions' in page.locator('.lesson-heading').inner_text()
    page.keyboard.press('ArrowLeft');assert page.locator('.lesson-heading').inner_text()=='Description, Prediction, Control'
    record('Previous, next, and keyboard outline navigation')
    page.locator('[data-action="reviewed"]').click()
    assert '1 of 104' in page.locator('#sidebar-progress').inner_text()
    page.locator('[data-action="bookmark"]').click()
    page.locator('#personal-note').fill('My example: an association is not a causal test.')
    saved=page.evaluate("JSON.parse(localStorage.getItem('study-studio:v1'))")
    assert saved['progress']['bcba-6']['reviewed']==['A.1']
    assert saved['progress']['bcba-6']['bookmarks']==['A.1']
    assert 'causal test' in saved['progress']['bcba-6']['notes']['A.1']
    record('Review marks, bookmarks, and personal notes saved')
    page.locator('#topic-search').fill('B.4')
    assert page.locator('.lesson-heading').inner_text()=='Positive and Negative Reinforcement Contingencies'
    page.locator('#topic-search').fill('no such topic xyz')
    assert 'No matching topics' in page.locator('#workspace').inner_text()
    page.locator('[data-action="clear-filters"]').last.click()
    page.locator('#domain-select').select_option('C')
    assert 'Operational Definitions' in page.locator('.lesson-heading').inner_text()
    assert page.locator('#filtered-count').inner_text()=='12 shown'
    page.locator('[data-action="all-topics"]').click()
    page.locator('[data-action="filter-bookmarks"]').click()
    assert page.locator('#filtered-count').inner_text()=='1 shown'
    assert 'Description, Prediction' in page.locator('.lesson-heading').inner_text()
    page.locator('[data-action="filter-bookmarks"]').click()
    record('Search, empty results, domain filter, bookmarked filter')
    page.locator('#mode-tabs [data-mode="flashcards"]').click()
    assert 'description' in page.locator('.card-question').inner_text().lower()
    page.locator('.deck-card').click()
    assert 'Systematically observe' in page.locator('.card-answer').inner_text()
    page.locator('[data-rating="known"]').click()
    assert 'prediction' in page.locator('.card-question').inner_text().lower()
    page.keyboard.press('Space');assert page.locator('.card-answer').count()==1
    page.locator('[data-rating="again"]').click()
    page.locator('#scope-select').select_option('review')
    assert 'prediction' in page.locator('.card-question').inner_text().lower()
    page.locator('#scope-select').select_option('topic')
    assert '/ 3' in page.locator('.deck-card').inner_text()
    page.locator('[data-action="shuffle"]').click()
    assert len(page.locator('.deck-card').inner_text())>20
    record('Flashcard flipping, confidence ratings, review deck, scope, shuffle')
    page.locator('#scope-select').select_option('all')
    settle(page);page.evaluate('window.scrollTo(0,0)');page.screenshot(path=str(ROOT/'docs/preview-flashcards.png'),full_page=True)
    page.locator('#mode-tabs [data-mode="scenarios"]').click()
    assert page.locator('[data-action="check-answer"]').is_disabled()
    current=page.locator('.pill').all_inner_texts()
    # Active topic remains A.1 after three-card same-topic shuffle.
    correct=DATA['topics'][0]['scenario']['correctIndex']
    wrong=(correct+1)%4
    page.locator(f'[data-action="choose-answer"][data-index="{wrong}"]').click()
    page.locator('[data-action="check-answer"]').click()
    assert 'Not quite' in page.locator('.feedback').inner_text()
    assert page.locator('.choice.correct').count()==1
    page.locator('[data-action="retry-scenario"]').click()
    page.locator(f'[data-action="choose-answer"][data-index="{correct}"]').click()
    page.locator('[data-action="check-answer"]').click()
    assert 'That’s right' in page.locator('.feedback').inner_text()
    result=page.evaluate("JSON.parse(localStorage.getItem('study-studio:v1')).progress['bcba-6'].scenarios['A.1-s1']")
    assert result['correct'] is True and result['firstCorrect'] is False and result['attempts']==2
    settle(page);page.evaluate('window.scrollTo(0,0)');page.screenshot(path=str(ROOT/'docs/preview-scenarios.png'),full_page=True)
    record('Scenario selection, grading, rationale, retry, immutable first-attempt score')
    page.locator('#mode-tabs [data-mode="outline"]').click()
    assert 'causal test' in page.locator('#personal-note').input_value()
    page.set_content(HTML,wait_until='load');settle(page)
    assert '1 of 104' in page.locator('#sidebar-progress').inner_text()
    assert 'causal test' in page.locator('#personal-note').input_value()
    record('Saved state restored on app initialization (Storage test double)')
    page.locator('[data-action="sources"]').first.click()
    assert 'not represented as scraped' in page.locator('#app-dialog').inner_text()
    page.locator('[data-action="close-dialog"]').click()
    record('Provenance disclosure and dialog close')
    page.locator('#course-select').select_option('my-material')
    assert 'Make this space yours' in page.locator('#workspace').inner_text()
    page.locator('#workspace [data-action="add-topic"]').click()
    page.locator('#edit-title').fill('My test topic')
    page.locator('#edit-summary').fill('This is a test of custom study material.')
    page.locator('#edit-concepts').fill('Testing | Checking behavior against expectations.')
    page.locator('#edit-question').fill('What does the app store locally?')
    page.locator('#edit-answer').fill('Study progress and notes.')
    page.locator('#edit-scenario').fill('A learner wants to save notes. Where are they stored?')
    for i,value in enumerate(['In this browser','On a remote server','Inside a textbook','Nowhere']):page.locator(f'#edit-option-{i}').fill(value)
    page.locator('#edit-explanation').fill('The app uses local browser storage.')
    page.locator('#topic-form button[type="submit"]').click()
    assert page.locator('.lesson-heading').inner_text()=='My test topic'
    assert '2 cards' in page.locator('#mode-tabs').inner_text()
    page.locator('#mode-tabs [data-mode="flashcards"]').click()
    assert 'testing' in page.locator('.card-question').inner_text().lower()
    page.locator('#mode-tabs [data-mode="scenarios"]').click()
    assert 'A learner wants to save notes' in page.locator('#workspace').inner_text()
    record('Curriculum dropdown and custom topic/card/scenario creation')
    page.locator('[data-action="settings"]').click()
    with page.expect_download() as d:page.locator('[data-action="export-backup"]').click()
    backup=d.value;backup.save_as(str(ROOT/'tests/_test_backup.json'))
    payload=json.loads((ROOT/'tests/_test_backup.json').read_text())
    assert payload['type']=='study-studio-backup'
    assert payload['data']['customTopics'][0]['title']=='My test topic'
    record('Backup export includes custom material and progress')
    page.locator('[data-action="close-dialog"]').click()
    testpack={'schemaVersion':1,'courses':[{'id':'import-test','title':'Imported subject','description':'Import test','domains':[{'id':'X','title':'Test domain'}],'topics':[{'id':'X.1','domain':'X','title':'<img src=x onerror="alert(1)"> safe title','summary':'Imported overview','concepts':[{'term':'Test','definition':'A definition.'}],'cards':[{'id':'x1card','question':'Imported question?','answer':'Imported answer.'}],'scenario':None}]}]}
    page.locator('#import-file').set_input_files({'name':'pack.json','mimeType':'application/json','buffer':json.dumps(testpack).encode()})
    page.wait_for_timeout(150)
    assert page.locator('#course-select').input_value()=='import-test'
    assert '<img src=x' in page.locator('.lesson-heading').inner_text()
    assert page.locator('.lesson-heading img').count()==0
    record('Study-pack import, new dropdown entry, HTML injection escaped')
    page.locator('#import-file').set_input_files({'name':'bad.json','mimeType':'application/json','buffer':b'{"courses":[{"id":"bad"}]}'})
    page.wait_for_timeout(150);assert 'Import failed' in page.locator('#toast').inner_text()
    record('Invalid study pack rejected without losing current content')
    page.on('dialog',lambda dialog:dialog.accept())
    page.locator('#import-file').set_input_files(str(ROOT/'tests/_test_backup.json'))
    page.wait_for_timeout(150)
    assert page.locator('#course-select').input_value()=='my-material'
    assert page.locator('#course-select option[value="import-test"]').count()==0
    record('Backup restoration with confirmation')
    # Ensure every built-in topic and scenario can render, without JavaScript errors.
    page.locator('#course-select').select_option('bcba-6')
    page.locator('#mode-tabs [data-mode="outline"]').click()
    for domain in 'ABCDEFGHI':
        page.locator('#domain-select').select_option(domain)
        assert page.locator('.lesson-heading').inner_text()
        page.locator('#mode-tabs [data-mode="scenarios"]').click()
        assert page.locator('.choice').count()==4
        page.locator('#mode-tabs [data-mode="outline"]').click()
    page.locator('#domain-select').select_option('all')
    record('All nine domains render in outline and scenario modes')
    # Phone-sized layout with real mode interactions.
    phone=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1,is_mobile=True,has_touch=True)
    phone.on('pageerror',lambda e:errors.append(str(e)))
    phone.evaluate(STORE_JS);phone.set_content(HTML,wait_until='load');settle(phone)
    assert phone.evaluate('document.documentElement.scrollWidth')==390
    phone.locator('[data-action="open-menu"]').click()
    assert 'open' in phone.locator('#sidebar').get_attribute('class')
    phone.locator('[data-action="topic"][data-id="A.2"]').click()
    assert 'open' not in phone.locator('#sidebar').get_attribute('class')
    phone.locator('#mode-tabs [data-mode="flashcards"]').click()
    phone.locator('.deck-card').click()
    assert phone.locator('.card-answer').count()==1
    assert phone.evaluate('document.documentElement.scrollWidth')==390
    settle(phone);phone.evaluate('window.scrollTo(0,0)');phone.screenshot(path=str(ROOT/'docs/preview-mobile.png'),full_page=True)
    record('390px mobile layout, drawer, flashcard tap, no horizontal overflow')
    phone.set_viewport_size({'width':320,'height':740});settle(phone)
    assert phone.evaluate('document.documentElement.scrollWidth')==320,phone.evaluate('document.documentElement.scrollWidth')
    record('320px layout has no horizontal overflow')
    # Graceful operation if browser storage is blocked.
    blocked=browser.new_page(viewport={'width':900,'height':800})
    blocked.set_content(HTML,wait_until='load')
    assert blocked.locator('.storage-warning').count()==1
    blocked.locator('[data-action="reviewed"]').click()
    assert '1 of 104' in blocked.locator('#sidebar-progress').inner_text()
    record('Storage-blocked mode remains usable with explicit warning')
    assert not errors,errors
    assert not requests,requests
    record('No JavaScript errors or network requests during main application tests')
    report={'passed':len(results),'tests':results,'javascriptErrors':errors,'networkRequests':requests,'storageNote':'Storage behavior tested with an in-memory Storage double; native file:// storage was not testable because this runner blocks file and loopback navigations.'}
    (ROOT/'tests/browser-results.json').write_text(json.dumps(report,indent=2))
    browser.close()
print('PASS TOTAL',len(results))
