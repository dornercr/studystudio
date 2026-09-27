# Study Studio — Tailwind study app

An offline, responsive study workspace. Select a curriculum, then move between **Outline**, **Flashcards**, and **Scenarios** while keeping the selected topic in view.

## Open it immediately

Open **`dist/index.html`** in a modern browser. All application code, compiled Tailwind CSS, and the study pack are embedded in that one file. There are no runtime dependencies, API keys, CDN requests, logins, or installation steps. External article/resource links require internet only when opened.

If a chat/file preview displays source text instead of executing it, save the HTML file and open it directly with your browser.

## Included study pack

| Component | Included |
|---|---:|
| Domains | 9, A–I |
| Outline topics | 104 |
| Question-and-answer cards | 220 |
| Original multiple-choice scenarios | 104 |

The topic IDs, titles, sequence, domains, and article links come from the user-supplied AllDayABA index. **The article bodies were not retrieved.** The notes, definitions, flashcards, and hypothetical scenarios are original supplemental study material. They are not scraped AllDayABA lessons, official BACB questions, retired questions, or a validated exam bank. The pack has not been independently reviewed for clinical or examination completeness and is not endorsed by BACB or AllDayABA. Use it alongside professional training and current official materials. The app also discloses this distinction in its content/source dialog.

The concise notes introduce the topics; they are not a replacement for a full textbook, graduate coursework, or supervised practice. Scenario scores and card confidence ratings do not predict exam results. No clinical protocols or jurisdiction-specific legal determinations are supplied.

## Using the app

**Curriculum dropdown.** Start with `6th Edition BCBA Outline`. Choose `My study material` to create your own subject matter, or import a JSON curriculum to add another entry.

**Outline.** Use the topic sidebar or Previous/Next controls. Review each overview, key idea, and distinction; mark a topic reviewed when ready. Navigating does not automatically mark it reviewed.

**Flashcards.** Attempt an answer, then click the card or Reveal answer. Choose Got it or Review again. Scope the deck to all filtered topics, the current topic, its domain, bookmarked topics, or cards marked for another look. Shuffle preserves your recorded progress.

**Scenarios.** Select one of four choices and check the answer. Review the rationale and retry when useful. First-attempt accuracy remains based on the first answer to each unique scenario; a retry does not rewrite the first attempt.

Search topics, filter domains, bookmark material, write private topic notes, and increase reading text size. Layout adapts to desktop and phone screens. The same topic carries across study modes.

### Keyboard shortcuts

| Key | Action |
|---|---|
| Left / Right | Previous / next topic or practice item |
| Space | Flip the flashcard |
| O / F / S | Outline / Flashcards / Scenarios |
| / | Focus topic search |
| 1–4 | Select a scenario answer |
| Enter | Check the scenario answer |
| Escape | Close dialog or mobile navigation |

Text inputs retain normal typing behavior.

## Local storage and backups

Progress, notes, bookmarks, and custom curricula are saved under `study-studio:v1` in your browser's local storage, where the browser permits it. No data is sent to a server.

**Local-file storage behavior depends on the browser and file location.** Clearing browser data, switching devices/browsers, private browsing, or moving/renaming the HTML file can make saved work unavailable. If storage is blocked or full, the app warns that it is running in session-only mode. Export a backup before closing or moving your work.

Open the settings button at the top right:

- **Export backup** saves your progress, notes, bookmarks, and custom curricula.
- **Export study pack** saves only the current curriculum, without private progress or notes.
- **Import / restore** accepts a study pack or a backup. Restore asks for confirmation before replacing saved work.
- **Reset learning progress** asks for confirmation and keeps your notes, bookmarks, and custom material.

Backups are unencrypted JSON files. Store them appropriately if your notes contain personal information. Do not add identifiable client records to study notes without appropriate authorization and safeguards.

## Add or import a curriculum

Use **My study material → Add a topic** to enter a title, overview, key ideas, an extra Q&A card, and an optional four-choice scenario. Key ideas use the format `Term | Definition`, one per line, and also become flashcards. If you provide no key ideas or extra card, the overview becomes a basic recall card.

For larger packs, use **`docs/example-study-pack.json`** as a template. Import it from Settings. Curriculum IDs, topic IDs, and practice-item IDs must be unique in their respective scopes. Imported curriculum IDs that already exist are renamed rather than overwriting an existing course. Topic domain IDs must match a declared domain. A scenario needs four distinct choices, `correctIndex` from 0 to 3, and an explanation. `scenario: null` is valid.

The app validates imports, rejects malformed content, blocks unsafe link protocols, and escapes imported/user-authored text before rendering. Imports are limited to 5 MB and 30 added curricula; a course supports up to 1,000 topics, 40 domains, and 100 cards per topic. Browser storage capacity can impose a lower practical limit.

## Project structure

```text
src/
  app.js                  Application behavior and UI templates
  content.json            Complete bundled curricula and original study content
  index.html              Single-file HTML build template
  theme.css               Tailwind theme tokens
  styles.css              Component/responsive CSS
scripts/
  build.mjs               Compiles Tailwind and embeds assets into dist/index.html
  serve.mjs               Optional dependency-free local Node server
  make_content.py         Rebuilds the original content pack from the index + authored notes
docs/
  supplied-outline.json   Preserved topic metadata from the supplied index
  example-study-pack.json Importable example curriculum
  CONTENT_NOTES.md        Scope and provenance details
  preview-*.png           Browser-rendered screenshots
tests/
  content.test.mjs        Node built-in test suite
  browser_test.py         Playwright UI integration checks
  browser-results.json    Recorded UI test results and limitations
dist/
  index.html              Ready-to-open, self-contained app
  tailwind.css            Compiled Tailwind CSS, also embedded in index.html
```

## Develop or rebuild

This is **plain JavaScript with Tailwind CSS 4.1.10**. No React dependency is needed.

For the ready-built app, you need only a browser. To rebuild, use Node.js 20 or later:

```bash
npm install
npm run build
npm test
```

The only npm dependency is pinned to `tailwindcss` 4.1.10. The build uses Tailwind's compiler to generate utilities from the literal class names in the source. It then embeds that CSS, the custom stylesheet, the app, and the content into one HTML file.

To serve the existing build on your own computer instead of opening it directly:

```bash
npm start
```

Then open `http://localhost:5173`. Set `PORT` to change the default. The local server binds to loopback only. Stop it with Ctrl+C. `npm run dev` rebuilds once and serves; it is not a live-reloading watcher.

Modify `src/content.json` directly to revise study content; run `npm run build` afterward. Running `scripts/make_content.py` regenerates `content.json` from its authored source and will replace manual edits to that JSON file.

## Tests and limitations

`npm test` uses Node's built-in runner. It checks all supplied topic metadata and order, domain counts, nonempty content, card and scenario IDs, balanced answer positions, disclosures, and the self-contained build.

The browser integration suite exercises navigation, filters, bookmarks, note saving, flashcard feedback, scenario grading/retry, mode/topic synchronization, custom content creation, export/import/restore, unsafe-HTML handling, empty/error states, all nine domains, and 390px/320px mobile layouts. Main-app tests produced no JavaScript errors or network requests.

**Runner limitation:** this environment blocks file and loopback navigation. Browser tests render the exact output HTML with Playwright `set_content`. Save/restore logic is exercised with an in-memory Storage test double; native browser persistence for a `file://` origin was not independently verified here. A separate blocked-storage test verifies the visible fallback warning and in-session functionality. Test details are in `tests/browser-results.json`.

To repeat browser checks in an environment with Python, Playwright, and Chromium installed:

```bash
python tests/browser_test.py
```

The script currently uses `/usr/bin/chromium`; adjust that executable path for another platform. Normal app use has no Python or Playwright dependency.

## Technology attribution

Tailwind CSS is distributed under its MIT license. The license is included under `docs/licenses/TAILWIND-LICENSE.txt`. No font files are included; the UI uses system fonts. Topic/source metadata and any third-party trademarks remain subject to their respective owners' rights.
