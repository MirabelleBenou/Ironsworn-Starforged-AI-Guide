# Scripts de vérification

> Licence : MIT (voir [`../outils/LICENSE`](../outils/LICENSE)).

Ces scripts permettent à toute personne possédant les livres de **refaire elle-même** la vérification de la bibliothèque (`SF-01`, `SF-02`, `SF-04`) contre ses propres PDF. Les PDF ne sont pas fournis : ils sont protégés et doivent être achetés.

## Prérequis
- Python 3.10+ et `pip install pdfplumber`
- `pdftotext` (paquet *poppler-utils* sous Linux, *poppler* via Homebrew sous macOS, ou [Xpdf/Poppler pour Windows](https://poppler.freedesktop.org/))
- Le PDF du livre de règles et celui des cartes d'assets (*Asset Singles*)

## Étapes

```bash
cd verification
python extract.py Ironsworn-Starforged-Rulebook.pdf Ironsworn-Starforged-Assets-Singles.pdf work
python check_tables.py work/rulebook_words.json ../projet-claude/connaissance/SF-01-moves.md ../projet-claude/connaissance/SF-02-oracles.md
python check_moves.py ../projet-claude/connaissance/SF-01-moves.md work/rulebook_pages
python check_assets.py ../projet-claude/connaissance/SF-04-assets.md work/assets_pages
python self_test.py work/rulebook_words.json ../projet-claude/connaissance/SF-02-oracles.md
```

## Lire les résultats

- **`check_tables.py`** : pour chaque ligne de table, retrouve le texte sur la page du livre, lit la plage imprimée sur la même ligne, et vérifie que le texte complet de la ligne figure sur la page. Signale « plage livre : … » (plage différente) ou « texte absent ». Les tables dessinées en graphiques (hexagones, schémas, matrices colorées) ne sont pas lisibles automatiquement et apparaissent toujours dans le rapport : elles se vérifient à l'œil (voir la liste dans [`../docs/VERIFICATION.md`](../docs/VERIFICATION.md)).
- **`check_moves.py`** : aligne le texte de chaque move sur le livre et affiche les écarts mot à mot. Les écarts qui ne sont qu'une table ou un mot déplacé par la mise en page sont des artefacts.
- **`self_test.py`** : injecte environ 300 erreurs connues (plage décalée, mot remplacé, lignes permutées) dans une copie en mémoire de SF-02 et vérifie que `check_tables.py` les détecte toutes.
- **`check_assets.py`** : même principe pour chaque carte d'asset. Les numéros de jauge et les libellés de champs (« Name », « Last of »…) sont ignorés.

Tout écart réel doit être confirmé sur la page imprimée, puis signalé dans une *issue*.
