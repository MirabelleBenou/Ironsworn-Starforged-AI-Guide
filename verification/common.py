"""Fonctions communes aux scripts de vérification (licence MIT)."""
import re

def norm(s):
    """Normalise un texte pour la comparaison (casse, ponctuation, guillemets, liens Markdown)."""
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('ﬁ', 'fi').replace('ﬂ', 'fl')
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    s = s.replace('—', ' ').replace('–', '-').lower()
    s = re.sub(r'[^a-z0-9+\-]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

def read_page(path):
    """Texte d'une page extraite par pdftotext, césures recollées."""
    return re.sub(r'(\w)-\n(\w)', r'\1\2', open(path, encoding='utf-8', errors='ignore').read())
