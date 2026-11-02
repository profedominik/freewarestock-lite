// Rasterise every SVG in images/svg to a 512x512 PNG in images/png.
// Usage: node scripts/render_png.cjs [size]   (needs Playwright + Chromium)
const { chromium } = require('playwright');
const { readdirSync, readFileSync, mkdirSync } = require('node:fs');
const { join } = require('node:path');

const root = join(__dirname, '..');
const size = Number(process.argv[2] || 512);
const src = join(root, 'images', 'svg');
const out = join(root, 'images', 'png');
mkdirSync(out, { recursive: true });

(async () => {
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: size, height: size } });
for (const f of readdirSync(src).filter((f) => f.endsWith('.svg')).sort()) {
  const svg = readFileSync(join(src, f), 'utf8').replace(/width="512" height="512"/, `width="${size}" height="${size}"`);
  await page.setContent(`<html><body style="margin:0;background:transparent">${svg}</body></html>`);
  await page.locator('svg').screenshot({ path: join(out, f.replace('.svg', '.png')), omitBackground: true });
}
await browser.close();
console.log('rendered PNGs at', size);
})();
