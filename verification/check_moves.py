"""Étape 3 — texte des moves (SF-01) contre le livre de règles. Licence MIT.
Usage : python check_moves.py SF-01-moves.md <dossier rulebook_pages>
Les écarts « insert » contenant une table ou un mot déplacé par la mise en page sont des artefacts à vérifier à l'œil."""
import re, sys, difflib, glob
from common import norm
md = open(sys.argv[1], encoding='utf-8').read()
pages = {}
for f in glob.glob(sys.argv[2] + '/*.txt'):
    pages[int(f.split('/')[-1][:-4])] = re.sub(r'(\w)-\n(\w)', r'\1\2', open(f, encoding='utf-8').read())
# moves: split md by ### headings
blocks = re.split(r'\n### ', md)
report = []
for b in blocks[1:]:
    title = b.split('\n', 1)[0]
    name = re.sub(r'\s*(\(progress move\))?\s*—.*$', '', title).strip()
    body = b.split('\n', 1)[1]
    body = re.sub(r'\n\| .*', '', body)            # drop tables
    body = re.sub(r'\n(Odds|-{3,}|Small|Unlikely|50/50|Likely|Almost|Situation|At a|In the|Under).*', '', body)
    W = norm(body.replace('**', '').replace('*', '')).split()
    if not W: continue
    best = None
    for p, txt in pages.items():
        if not (140 <= p <= 240 or 2 <= p <= 140): pass
        R = norm(txt).split()
        # anchor on first 6 words
        anchor = ' '.join(W[:6]); full = ' '.join(R)
        i = full.find(anchor)
        if i < 0: continue
        start = len(full[:i].split())
        win = R[start:start + int(len(W) * 1.4) + 20]
        sm = difflib.SequenceMatcher(None, W, win, autojunk=False)
        r = sm.ratio()
        if not best or r > best[0]: best = (r, p, win, sm)
    if not best:
        report.append(f'### {name}: ANCRE INTROUVABLE'); continue
    r, p, win, sm = best
    diffs = []
    last = max((blk.a + blk.size for blk in sm.get_matching_blocks() if blk.size), default=0)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal' or i1 >= last: continue
        if op == 'insert' and i1 >= len(W) - 1: continue
        diffs.append(f"   {op}: SF «{' '.join(W[i1:i2])}» | livre «{' '.join(win[j1:j2])}»")
    if diffs:
        report.append(f'### {name} (PDF p.{p}, ratio {r:.2f})'); report += diffs
print('\n'.join(report) if report else 'aucun écart')
