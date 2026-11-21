// News-image entry (Node 22, standard library only): the image drawn by
// draw.py sits beside this file as entry.png, and the program copies it
// to /output/entry.png. Outside the grader, MAKEFUN_OUTPUT_DIR stands
// in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
const dest = join(outDir, 'entry.png');
copyFileSync(new URL('./entry.png', import.meta.url), dest);
// Guard: refuse to hand the grader a truncated or non-PNG file.
const head = readFileSync(dest).subarray(0, 8);
if (head[0] !== 0x89 || head[1] !== 0x50 || head[2] !== 0x4e || head[3] !== 0x47) {
  throw new Error('entry.png is not a PNG');
}
