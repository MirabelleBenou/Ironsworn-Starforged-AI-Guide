"""Étape 2 — tables (SF-01, SF-02). Licence MIT.
Usage : python check_tables.py work/rulebook_words.json SF-01-moves.md SF-02-oracles.md
(le dossier work/rulebook_pages produit par extract.py doit être à côté du fichier json)
Contrôle ancré : pour chaque ligne de table SF, retrouve le texte sur la page du livre
(coordonnées des mots), puis lit la plage imprimée sur la même ligne, à gauche du texte."""
import json, re, sys, collections
W = {int(k): v for k, v in json.load(open(sys.argv[1])).items()}
RANGE = re.compile(r'^(\d{1,3})(?:[–-](\d{1,3}))?$')
def ntok(t):
    t = t.replace('’', "'").lower()
    return re.sub(r'[^a-z0-9]+', '', t)
def clean_sf(t):
    t = re.sub(r'\(RG p\.[^)]*\)', ' ', t)
    t = t.replace('→', ' ').replace('*', ' ')
    return t
PAGES = {}
for p, ws in W.items():
    ws = sorted(ws, key=lambda w: w[3]); lines = []; 
    for w in ws:
        if lines and w[3] - lines[-1][0][3] < 3.0: lines[-1].append(w)
        else: lines.append([w])
    ws = [w for l in lines for w in sorted(l, key=lambda w: w[1])]
    toks = [(ntok(w[0]), w) for w in ws]
    toks = [(t, w) for t, w in toks if t]
    PAGES[p] = toks
def anchors(p, words):
    toks = PAGES[p]; k = len(words); out = []
    for i in range(len(toks) - k + 1):
        if all(toks[i + j][0] == words[j] for j in range(k)): out.append(toks[i][1])
    return out
def ranges_left(p, w):
    top, x0 = w[3], w[1]
    cands = [x for x in W[p] if abs(x[3] - top) < 3.5 and x[2] <= x0 + 0.5 and (RANGE.match(x[0]) or x[0] in ('--', '–', '—'))]
    cands.sort(key=lambda x: x[1])
    res = []
    for c in cands:
        m = RANGE.match(c[0])
        res.append((int(m.group(1)), int(m.group(2) or m.group(1))) if m else None)
    return res

import os
RAW = {}
def rawpage(p):
    if p not in RAW:
        f = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), 'rulebook_pages', f'{p}.txt')
        t = open(f, encoding='utf-8', errors='ignore').read() if os.path.exists(f) else ''
        t = re.sub(r'(\w)-\n(\w)', r'\1\2', t)
        RAW[p] = ' ' + ' '.join(ntok(x) for x in t.split() if ntok(x)) + ' '
    return RAW[p]
def fulltext_ok(p, t):
    seq = ' '.join(ntok(x) for x in clean_sf(t).split() if ntok(x))
    return (' ' + seq + ' ') in rawpage(p)

def tables(md):
    out = []; title = []; lines = md.split('\n'); i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('#'):
            lvl = len(l) - len(l.lstrip('#')); title = title[:lvl - 1] + [l.lstrip('#').strip()]
        if l.startswith('| ') and i + 1 < len(lines) and lines[i + 1].startswith('|---'):
            rows = []; j = i + 2
            while j < len(lines) and lines[j].startswith('| '):
                c = [x.strip() for x in lines[j].split('|')[1:-1]]
                if c[0] != '—' and re.match(r'\d', c[0]):
                    a, _, b = c[0].partition('–'); rows.append((int(a), int(b or a), c[1]))
                j += 1
            out.append((' › '.join(t for t in title[1:] if t), rows)); i = j; continue
        i += 1
    return out
MATRIX = re.compile(r'(Terminus|Outlands|Expanse|Space|Interior|Land|Liquid|Air|Lifebearing|Lifeless|Planetside|Orbital|Deep Space|Starship|Settlement)\s*`', re.I)
results = []; stats = collections.Counter()
for f in sys.argv[2:]:
    for name, rows in tables(open(f, encoding='utf-8').read()):
        if not rows: continue
        keyw = [[ntok(x) for x in clean_sf(t).split() if ntok(x)][:3] for _, _, t in rows]
        score = collections.Counter()
        for kw in keyw:
            if not kw: continue
            for p in PAGES:
                if anchors(p, kw): score[p] += 1
        if not score:
            results.append((f, name, 'PAGE INTROUVABLE', rows)); stats['table_nopage'] += 1; continue
        hints = [int(h) + 1 for h in re.findall(r'Rulebook p\. (\d+)', name)]
        if hints:
            h = hints[-1]; cand = [p for p in (h, h + 1, h + 2, h - 1) if p in PAGES] + [q for q, _ in score.most_common(3)]
            p0 = max(cand, key=lambda p: (score.get(p, 0), -abs(p - h)))
        else:
            p0 = score.most_common(1)[0][0]
        pages = [p for p in (p0, p0 - 1, p0 + 1, p0 + 2) if p in PAGES]
        is_matrix = bool(MATRIX.search(name.split('›')[-1]))
        COLS = {'terminus':0,'outlands':1,'expanse':2,'space':0,'interior':1,'land':2,'liquid':3,'air':4,'lifebearing':0,'lifeless':1}
        leaf = name.split('›')[-1].split('`')[0].strip().lower()
        col = COLS.get(leaf)
        bad = []
        for (a, b, t), kw in zip(rows, keyw):
            stats['rows'] += 1
            found_text = False; ok = False; seen = []
            for p in (list(range(p0 - 3, p0 + 4)) if "Name" in name else [p0]):
                for w in anchors(p, kw):
                    found_text = True
                    rl = ranges_left(p, w)
                    seen.append(rl)
                    if ((is_matrix and col is not None and len(rl) > col and rl[col] == (a, b)) or (is_matrix and col is None and (a, b) in rl) or (not is_matrix and rl and rl[-1] == (a, b))) and fulltext_ok(p, t):
                        ok = True; break
                if ok: break
            if ok: stats['ok'] += 1; continue
            stats['text_missing' if not found_text else 'range_diff'] += 1
            bad.append((a, b, t, 'texte absent' if not found_text else f'plage livre: {seen[:3]}'))
        if bad: results.append((f, f'{name} (PDF p.{p0})', bad, rows))
print(dict(stats))
for f, name, bad, rows in results:
    print(f'\n## {f.split("/")[-1]} › {name}')
    if isinstance(bad, str): print('  ', bad); continue
    for a, b, t, why in bad[:12]: print(f'   {a}–{b} {t[:60]}  ⟶ {why}')
    if len(bad) > 12: print(f'   … +{len(bad) - 12}')
