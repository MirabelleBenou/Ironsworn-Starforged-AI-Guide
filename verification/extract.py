"""Étape 1 : extraction depuis VOS PDF (non fournis, protégés).
Usage : python extract.py <Rulebook.pdf> <Asset-Singles.pdf> <dossier_sortie>
Produit : rulebook_pages/N.txt, assets_pages/N.txt, rulebook_words.json (mots + coordonnées)."""
import json, os, subprocess, sys
import pdfplumber

rb, assets, out = sys.argv[1], sys.argv[2], sys.argv[3]
for pdf, sub in ((rb, 'rulebook_pages'), (assets, 'assets_pages')):
    d = os.path.join(out, sub); os.makedirs(d, exist_ok=True)
    n = len(pdfplumber.open(pdf).pages)
    for p in range(1, n + 1):
        subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), pdf, os.path.join(d, f'{p}.txt')], check=True)
words = {}
with pdfplumber.open(rb) as pdf:
    for p, page in enumerate(pdf.pages, 1):
        ws = page.extract_words(x_tolerance=1.5, y_tolerance=2)
        words[p] = [(w['text'], round(w['x0'], 1), round(w['x1'], 1), round(w['top'], 1)) for w in ws]
        page.flush_cache()
json.dump(words, open(os.path.join(out, 'rulebook_words.json'), 'w'))
print('extraction terminée')
