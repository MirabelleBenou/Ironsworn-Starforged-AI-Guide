"""Étape 5 — test du contrôleur (licence MIT). Injecte 300 erreurs connues dans une copie en mémoire de SF-02
(plage décalée, mot remplacé, lignes permutées) et vérifie que check_tables.py les détecte.
Usage : python self_test.py work/rulebook_words.json ../projet-claude/connaissance/SF-02-oracles.md"""
import sys, random, re, json, collections
import os
WORDS, SF02 = sys.argv[1], sys.argv[2]
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'check_tables.py'), encoding='utf-8').read()
sys.argv = ['x', WORDS]
exec(src.split('results = []')[0])
COLS = {'terminus':0,'outlands':1,'expanse':2,'space':0,'interior':1,'land':2,'liquid':3,'air':4,'lifebearing':0,'lifeless':1}
PAGECACHE = {}
def page_for(name, rows):
    if name in PAGECACHE: return PAGECACHE[name]
    keyw = [[ntok(x) for x in clean_sf(t).split() if ntok(x)][:3] for _, _, t in rows]
    score = collections.Counter()
    for kw in keyw:
        if kw:
            for p in PAGES:
                if anchors(p, kw): score[p] += 1
    hints = [int(h) + 1 for h in re.findall(r'Rulebook p\. (\d+)', name)]
    if not score: p0 = None
    elif hints:
        h = hints[-1]; cand = [p for p in (h, h + 1, h + 2, h - 1) if p in PAGES] + [q for q, _ in score.most_common(3)]
        p0 = max(cand, key=lambda p: (score.get(p, 0), -abs(p - h)))
    else: p0 = score.most_common(1)[0][0]
    PAGECACHE[name] = p0; return p0
def row_ok(name, p0, a, b, t):
    kw = [ntok(x) for x in clean_sf(t).split() if ntok(x)][:3]
    leaf = name.split('›')[-1].split('`')[0].strip().lower(); col = COLS.get(leaf)
    is_matrix = bool(MATRIX.search(name.split('›')[-1]))
    for p in (list(range(p0 - 3, p0 + 4)) if 'Name' in name else [p0]):
        if p not in PAGES: continue
        for w in anchors(p, kw):
            rl = ranges_left(p, w)
            if ((is_matrix and col is not None and len(rl) > col and rl[col] == (a, b)) or (is_matrix and col is None and (a, b) in rl) or (not is_matrix and rl and rl[-1] == (a, b))) and fulltext_ok(p, t):
                return True
    return False
md = open(SF02, encoding='utf-8').read()
T = [(n, r) for n, r in tables(md) if r]
pool = []
for n, rows in T:
    p0 = page_for(n, rows)
    if p0 is None: continue
    for k, (a, b, t) in enumerate(rows):
        if row_ok(n, p0, a, b, t): pool.append((n, p0, rows, k))
random.seed(7)
picked = random.sample(pool, 300)
kinds = collections.Counter(); caught = collections.Counter(); missed = []
for n, p0, rows, k in picked:
    a, b, t = rows[k]
    kind = ['plage', 'mot', 'permutation'][len(kinds) % 3] if False else random.choice(['plage', 'mot', 'permutation'])
    if kind == 'plage':
        b2 = b + 1 if b < 100 else b - 1
        if b2 == b or b2 < a: continue
        mut = [(a, b2, t)]
    elif kind == 'mot':
        ws = t.split(); j = random.randrange(len(ws)); ws[j] = 'Zorblax'; mut = [(a, b, ' '.join(ws))]
    else:
        if k + 1 >= len(rows) or rows[k + 1][2] == t: continue
        a2, b2, t2 = rows[k + 1]; mut = [(a, b, t2), (a2, b2, t)]
    kinds[kind] += 1
    if any(not row_ok(n, p0, *m) for m in mut): caught[kind] += 1
    else: missed.append((kind, n, rows[k], mut))
print('lignes conformes éligibles :', len(pool))
print('erreurs injectées :', dict(kinds), '— détectées :', dict(caught), f'— total {sum(caught.values())}/{sum(kinds.values())}')
for m in missed: print('NON DÉTECTÉ', m)
