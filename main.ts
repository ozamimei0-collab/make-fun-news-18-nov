// World News — 18 November 2026: one-image entry for make.fun.
// Hands in entry.png: copies it to the output directory the grader reads.
// Run it with `node main.ts`, or point it elsewhere with MAKEFUN_OUTPUT_DIR.
import { copyFileSync, existsSync, mkdirSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const ENTRY = 'entry.png';
const MAX_BYTES = 1048576; // the bounty caps the image at 1 MiB

const here = fileURLToPath(new URL('.', import.meta.url));
const out = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const entry = join(here, ENTRY);
if (!existsSync(entry)) {
  throw new Error(`${ENTRY} is missing next to main.ts`);
}
const size = statSync(entry).size;
if (size > MAX_BYTES) {
  throw new Error(`${ENTRY} is ${size} bytes, over the 1 MiB cap`);
}

mkdirSync(out, { recursive: true });
copyFileSync(entry, join(out, ENTRY));
console.log(`World News — 18 November 2026: handed in ${ENTRY} (${size} bytes) to ${out}`);
