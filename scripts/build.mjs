import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const require = createRequire(import.meta.url);
let compile, tailwindDir;
try {
  ({ compile } = require('tailwindcss'));
  tailwindDir = path.dirname(require.resolve('tailwindcss/package.json'));
} catch (error) {
  // Optional build-time location for environments with Tailwind installed globally.
  if (!process.env.TAILWIND_DIR) throw new Error('Tailwind is not installed. Run npm install, then npm run build.', {cause:error});
  tailwindDir = process.env.TAILWIND_DIR;
  ({ compile } = require(path.join(tailwindDir, 'dist/lib.js')));
}
const read = name => fs.readFile(path.join(root, 'src', name), 'utf8');
const [template, app, data, styles, theme, base] = await Promise.all([
  read('index.html'), read('app.js'), read('content.json'), read('styles.css'), read('theme.css'),
  fs.readFile(path.join(tailwindDir, 'index.css'), 'utf8')
]);
JSON.parse(data); // Fail rather than ship an invalid study pack.
// All utility classes are literal strings. Collect a superset of candidate tokens;
// Tailwind ignores tokens that do not identify valid utilities.
const candidates = new Set((template + '\n' + app).match(/[A-Za-z0-9_!@#.%:/\[\](),=-]+/g) || []);
const compiler = await compile(base + '\n' + theme);
const css = compiler.build([...candidates]);
const inlineScript = value => value.replace(/<\/script/gi, '<\\/script');
const html = template
  .replace('/*__TAILWIND__*/', () => css)
  .replace('/*__CUSTOM_CSS__*/', () => styles)
  .replace('/*__CONTENT__*/', () => inlineScript(data))
  .replace('/*__APP_JS__*/', () => inlineScript(app));
await fs.mkdir(path.join(root, 'dist'), {recursive:true});
await fs.writeFile(path.join(root, 'dist/index.html'), html);
await fs.writeFile(path.join(root, 'dist/tailwind.css'), css);
console.log(`Built dist/index.html (${(Buffer.byteLength(html)/1024).toFixed(0)} KB). All application assets are embedded; no CDN or server is required.`);
