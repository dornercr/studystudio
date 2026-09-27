# Study Studio · Cooper textbook edition

A self-contained **Tailwind CSS 4.1.10 + plain JavaScript** study app. The original BCBA outline remains unchanged. The Cooper textbook is a **separate curriculum in the library dropdown**, with its own progress, notes, bookmarks, and practice history.

## Open the app

Open **`dist/index.html`** in Chrome or another modern browser. No installation, server, login, API key, or CDN is required. When a chat preview shows source text, save the HTML and open that file in the browser.

The library contains:

| Curriculum | Study material |
|---|---|
| 6th Edition BCBA Outline | Original 104 topics, 220 cards, and 104 scenarios; content unchanged |
| Cooper, Heron & Heward — Applied Behavior Analysis, 3rd Edition | 31 chapters; 170 section lessons; 661 concept cards; 170 original application scenarios |
| Cooper glossary appendix | 521 searchable entries and 516 extracted definition cards; included in the book’s 1,177-card total |
| My study material | Your own editable topics, cards, and scenarios |

Five glossary entries are cross-reference-only entries, not definition cards. The book appears as 171 navigable items: 170 lessons plus the glossary reference appendix. The appendix is **not** a 32nd chapter or a tenth BACB domain.

## Study the book

Choose the Cooper entry in **Study library**. Use **Chapters** for book order or **6th Edition domains** for the editorial mapping. The chapter and domain controls filter the book without changing the original curriculum.

**Outline:** Read each section’s overview, key ideas, important distinction, and source references. Previous/Next follows the filtered set. Review marks are deliberate, not automatic.

**Flashcards:** Answer before revealing. Mark Got it or Review again. Scope practice to this chapter, this section, a domain, bookmarked sections, the full filtered set, or items needing another look. Every card has a source-page range. Glossary cards refer to their own glossary pages.

**Scenarios:** Choose an answer and check it. Each book scenario explains all four options. Retry without changing the first-attempt record. Scenarios are newly written hypothetical applications, not copied book cases, an instructor test bank, or secure BACB items.

**Glossary:** Search terms and definitions. Open the source page or practice one definition. There are no fabricated glossary scenarios; use chapter scenarios for application practice.

**Coverage & task crosswalk:** All 104 task rows are visible, with 79 related, 21 partial, and 4 unmapped rows. “Related” is not a claim of full exam-task coverage. Each mapping links to book sections and printed pages. E.9, E.10, F.2, and I.3 have no mapped sections. Domain I and historical ethics topics are deliberately limited.

## Source reader and original PDF

The app embeds extracted text for all **908 PDF pages**, including chapter summaries, the epilogue, glossary, bibliography, and indexes. Search the book locally or jump to a printed page. **Printed page + 18 = PDF page.** Fifteen selected original page images are included for direct visual consultation.

The source reader is not a new PDF viewer. The original 235 MB PDF is not bundled. Choose **Connect original PDF** inside the reader to associate your own local copy. An original-page link opens the browser’s PDF viewer at the selected PDF page. The file is not uploaded, and the association lasts for the current session only.

Source-text extraction can misorder columns or damage mathematical symbols. Use the original image/PDF for authoritative layout, figures, tables, and ambiguous wording. Source page ranges include a shared boundary page when sections begin on the same page.

## Coverage and provenance

The book lessons are paraphrases derived from the uploaded third edition. Glossary and reader text are extracted from that copy. All chapters and substantive table-of-contents sections have study material, but **not every paragraph, worked example, citation, or figure has a separately authored lesson or question**. This is a section-level study companion with full-source lookup, not a substitute for reading the book or supervised training.

The book’s own task mappings reference the **5th Edition**, and its ethics chapter discusses the older **Professional and Ethical Compliance Code**. The app’s 6th Edition tags are separate editorial work, not renamed printed codes. Current ethics, law, certification requirements, and gaps in cultural responsiveness or supervision should be studied separately. No clinical or examination-completeness validation is claimed. There is no endorsement by Pearson, the textbook authors, BACB, or AllDayABA.

Chapter 16 includes an explicit note about conflicting source wording on the behavior-altering effect. It identifies the passages followed and does not claim a verified publisher erratum. The glossary retains historical language; visible spacing and obvious text-layer errors were cleaned. Bibliographic/reference material is retained in the reader rather than converted into filler practice questions.

The original outline’s notes and scenarios remain original supplemental content based on the supplied AllDayABA *index*, not scraped AllDayABA article bodies. See `docs/CONTENT_NOTES.md`.

## Preserve existing progress

In the old app, open **Settings → Export backup**. In this app, choose **Settings → Import / restore**, select that backup, and confirm. The built-in Cooper curriculum remains available even when restoring an older backup with no Cooper progress.

Storage uses the same `study-studio:v1` schema, with a separate progress object per curriculum. Local-file browser storage is not guaranteed to transfer between filenames or browser profiles. Clearing browser data or using private browsing can remove it. The app warns when storage is blocked/full; export before closing in that case.

Backups contain private notes and are unencrypted JSON. They contain progress plus custom/imported curricula, not duplicate copies of the built-in book archive. Keep backups somewhere appropriate and avoid identifiable client records in study notes.

**Export study pack** creates portable lesson/card/scenario/glossary/crosswalk data without your personal progress. For the Cooper pack, the large source text and page images stay in the standalone app to avoid duplicating them in browser storage. Import Cooper packs into this updated version; the original app’s older import limits do not support the full glossary appendix. Conflicting imported IDs get new names rather than overwriting curricula.

## Development

Ready-built use needs only a browser. Rebuilding requires Node.js 20+:

```bash
npm install
npm run build
npm test
npm start
```

`npm start` optionally serves the app at `http://localhost:5173`; Ctrl+C stops it. No backend database or cloud service is involved. Tailwind is pinned to **4.1.10**. If it is already installed outside the project, `TAILWIND_DIR=/path/to/tailwindcss npm run build` is supported.

Edit `src/content.json` for study content and `src/app.js` / `src/styles.css` for the interface, then rebuild. `scripts/make_content.py` rebuilds only the original outline while preserving other bundled curricula; it does not generate the Cooper content. The bundled JSON is the source of truth for this release.

Key files:

- `src/content.json`: all bundled study materials, crosswalk, source text, and selected source images.
- `src/app.js`: escaped-text UI, navigation, progress, import/export, book extension.
- `scripts/build.mjs`: compile Tailwind and embed all runtime assets into `dist/index.html`.
- `docs/cooper-coverage.json`: chapter/section/source-page inventory.
- `docs/cooper-crosswalk.json`: editorial mapping and limitations for all 104 tasks.
- `tests/*.test.mjs`: structural integrity and original-curriculum preservation checks.
- `tests/browser_test.py`, `tests/cooper_browser_test.py`: Chromium integration tests.

Imports allow up to 25 MB, 30 added curricula, 1,000 topics per course, 40 domains, and 1,000 cards per topic. Browser storage capacity may impose a much lower practical limit. Imported values are validated, unsafe link protocols are rejected, and user text is HTML-escaped before display.

## Verification

Run `npm test` for both the original and textbook content suites. With Python, Playwright, and Chromium installed:

```bash
python tests/browser_test.py
python tests/cooper_browser_test.py
```

The browser scripts use `/usr/bin/chromium`; adjust for your environment. Tests exercise all 31 chapters in all three modes, source references, crosswalk filters, glossary lookup, source search/page jumps, separate progress, export/import, original app regressions, and 390 px / 320 px layouts. No runtime network requests or JavaScript errors were observed.

**Runner limitation:** the tests render the actual output HTML through Playwright `set_content`. Save/restore is tested with an in-memory Storage double; native `file://` persistence and native browser PDF-viewer behavior are not independently verified here. Original-PDF link creation is separate from the offline source-text reader. No pass-rate or exam-readiness guarantee is implied by software tests.

## Attribution and personal use

Tailwind’s MIT license is in `docs/licenses/TAILWIND-LICENSE.txt`. The interface uses system fonts; no font files are bundled. Textbook material is derived from the copy supplied for this personal-study task. The source text and images retain their underlying copyright; this bundle does not grant redistribution rights to third-party material.
