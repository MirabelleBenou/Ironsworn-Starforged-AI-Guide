"""Étape 4 — texte des assets (SF-04) contre les cartes. Licence MIT.
Usage : python check_assets.py SF-04-assets.md <dossier assets_pages>"""
import re, sys, glob, difflib
from common import norm
md = open(sys.argv[1], encoding='utf-8').read()
cards = {int(f.split('/')[-1][:-4]): re.sub(r'(\w)-\n(\w)', r'\1\2', open(f, encoding='utf-8').read()) for f in glob.glob(sys.argv[2] + '/*.txt')}
NOISE = set('0 1 2 3 4 5 6 out of action battered cursed name one two ideology linked stat expertise bond-mate bondmate identifier command vehicle module path companion deed support starship'.split())
def noise(ws): return all(w in NOISE for w in ws)
rep = []
for b in re.split(r'\n### ', md)[1:]:
    head, body = b.split('\n', 1)
    name = head.split('  _(')[0].strip()
    lines = []
    for l in body.split('\n'):
        if l.startswith('_champs') or l.startswith('_jauge'): continue
        l = re.sub(r'^_Requirement : (.*?)\.\.\._$', r'\1', l)
        l = re.sub(r'^\d+\. [●○] ', '', l); l = re.sub(r'^\s*\* ', '', l)
        lines.append(l)
    W = norm(' '.join(lines).replace('**', '').replace('*', '')).split()
    best = None
    for p, t in cards.items():
        tl = t.split('\n')
        if norm(name) in norm(' '.join(tl[:6])):
            C = norm(t.replace('[', ' ').replace(']', ' ').replace('✴', ' ')).split()
            # drop title words at start
            nn = norm(name).split()
            for i in range(min(12, len(C))):
                if C[i:i+len(nn)] == nn: C = C[i+len(nn):]; break
            r = difflib.SequenceMatcher(None, W, C, autojunk=False).ratio()
            if not best or r > best[0]: best = (r, p, C)
    r, p, C = best
    sm = difflib.SequenceMatcher(None, W, C, autojunk=False)
    issues = []
    Wj, Cj = ' ' + ' '.join(W) + ' ', ' ' + ' '.join(C) + ' '
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': continue
        sf, cd = W[i1:i2], C[j1:j2]
        if noise(sf) and noise(cd): continue
        if not cd and (' ' + ' '.join(sf) + ' ') in Cj: continue
        if not sf and (' ' + ' '.join(cd) + ' ') in Wj: continue
        issues.append(f"   SF «{' '.join(sf)[:140]}» | carte «{' '.join(cd)[:140]}»")
    if issues: rep.append(f'{name} (carte p.{p})'); rep += issues
print('\n'.join(rep))
