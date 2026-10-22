"""Crée une copie allégée d'un export Stargazer (images du journal retirées).
L'export original n'est pas modifié.  Usage : python alleger_export_stargazer.py export.json"""
import json, re, sys, pathlib

src = pathlib.Path(sys.argv[1])
data = json.loads(src.read_text(encoding="utf-8"))
img = re.compile(r'<img[^>]*src="data:image[^"]*"[^>]*>', re.I)
n = 0
for campagne in data if isinstance(data, list) else [data]:
    for entree in campagne.get("journal", []):
        entree["content"], k = img.subn("[image retirée]", entree["content"])
        n += k
dst = src.with_name(src.stem + "-light.json")
dst.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{n} image(s) retirée(s) : {src.stat().st_size//1024} Ko -> {dst.stat().st_size//1024} Ko ({dst.name})")
