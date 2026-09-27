import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../dist');
const port = Number(process.env.PORT || 5173);
if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error('PORT must be an integer from 1 through 65535.');
const server = http.createServer(async (req,res) => {
  try {
    const url = new URL(req.url, 'http://localhost');
    const file = url.pathname === '/' ? 'index.html' : decodeURIComponent(url.pathname).replace(/^\/+/, '');
    const full = path.resolve(root, file);
    if (full !== root && !full.startsWith(root + path.sep)) {res.writeHead(403);res.end('Forbidden');return;}
    const data = await fs.readFile(full);
    const types = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.json':'application/json; charset=utf-8'};
    res.writeHead(200, {'Content-Type':types[path.extname(full)] || 'application/octet-stream','Cache-Control':'no-cache','X-Content-Type-Options':'nosniff'});
    res.end(data);
  } catch {res.writeHead(404);res.end('Not found. Run npm run build before starting.');}
});
server.on('error',error=>{console.error(error.message);process.exitCode=1;});
server.listen(port,'127.0.0.1',()=>console.log(`Study Studio: http://localhost:${port}`));
