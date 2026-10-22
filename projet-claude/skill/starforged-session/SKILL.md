---
name: starforged-session
description: Clôture de session de la campagne Ironsworn Starforged (End a Session) — nouvelle SYNTHÈSE du journal et liste des saisies à reporter dans Stargazer.
---

# Starforged — Kit de fermeture (End a Session)

> Licence : [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — méthode originale du dépôt Ironsworn-Starforged-AI-Guide. Conçu pour Ironsworn: Starforged (Shawn Tomkin) ; produit non officiel, sans lien avec Tomkin Press.

Ce skill ne contient que des procédures et des formats de sortie, jamais des faits de campagne. L'export Stargazer (JSON allégé joint à la discussion) reste la source de vérité ; l'utilisateur applique lui-même les changements dans Stargazer.

## 0. Avant de produire quoi que ce soit
Relis dans la connaissance du projet :
- le texte exact de **End a Session** (SF-01-moves.md, Session Moves) ;
- **Earn Experience** et **Advance** (SF-01, Legacy Moves) ;
- la section Legacy Tracks (SF-03-regles.md).

Rappel de ce que disent ces textes (à vérifier, pas à citer de mémoire) :
- End a Session ne donne **pas** d'XP directement. Le move demande de rattraper la progression oubliée (*Develop Your Relationship* si un lien avec une connection s'est renforcé, *Reach a Milestone* si une quête a avancé). Il donne **+1 momentum** si l'on note une quête, une connection ou une situation à mettre au premier plan la prochaine fois.
- L'XP vient **uniquement** des cases de legacy remplies (Earn Experience) : 2 XP par case, 1 XP par case sur une piste déjà effacée une fois (marqueur « 10 » / plus10).
- *Forsake Your Vow* ne donne aucune XP : le vœu est effacé et les coûts choisis s'appliquent.

## 1. Rattrapage End a Session (avec l'utilisateur)
Demande ou propose :
1. Une connection s'est-elle renforcée sans qu'on ait fait Develop Your Relationship ? Si oui, la nommer.
2. Une quête a-t-elle avancé sans Reach a Milestone ? Si oui, laquelle.
3. Quelle quête, connection ou situation mettre au premier plan la prochaine fois ? Si l'utilisateur en note une : +1 momentum.

## 2. Livrable (a) — nouvelle SYNTHÈSE à coller dans l'entrée de journal épinglée
Elle écrase la précédente. Garde le format du journal existant (HTML de Stargazer ou texte simple).

```
=== SYNTHÈSE (état courant — à réécrire à chaque fin de session) ===
Dernière MAJ : <date> (<n° ou titre de session>)
Lieu actuel : <position, avec la cellule de secteur si connue>
Ton / registre : <ton>
Flags (à éviter) : <flags actuels>

SCÈNE EN COURS (3-5 lignes) : <où on s'arrête exactement>

FOCUS PROCHAINE SESSION : <ce qui a été noté en fin de session, ou « aucun »>

PERSONNAGE (delta uniquement — stats, jauges et équipement vivent dans le JSON) :
<promesses, relations, secrets appris, objets gagnés ou perdus ; « aucun » si rien>

SECTEUR — <nom> (<région>) : <settlements, planètes, passages, troubles>

FILS OUVERTS : <vœux, mystères, menaces en cours>

PNJ CLÉS : <nom, lieu, questions-secrets (facile / difficile) et réponses déjà tranchées>

À REPORTER / DÉCISIONS EN ATTENTE :
<reprendre les items non résolus de la SYNTHÈSE précédente ; supprimer ceux qui sont traités, notamment les saisies Stargazer déjà faites>
```

## 3. Livrable (b) — saisies Stargazer, ligne par ligne
Format : `élément : ancienne valeur → nouvelle valeur (raison)`. N'inclure que ce qui change.

- **Legacy tracks** (quests / bonds / discoveries) : ticks ajoutés et leur origine (Fulfill Your Vow, Forge a Bond, Finish an Expedition, Make a Discovery, Confront Chaos, capacité d'asset…). Ticks avant → après.
- **XP** : pour chaque case de legacy nouvellement remplie, +2 XP (+1 si la piste a déjà été effacée), avec le total gagné. Rappeler de cocher les cases d'XP correspondantes dans Stargazer, et l'XP dépensée en Advance s'il y en a eu.
- **Momentum** final, y compris le +1 du focus de fin de session. Momentum max et reset s'ils ont changé (impacts).
- **Jauges** : health, spirit, supply, integrity du vaisseau, santé des companions.
- **Impacts** marqués ou effacés.
- **Vœux et progress tracks** : nom, rang, ticks avant → après, créés, accomplis ou abandonnés.
- **Clocks** : créées, avancées (y compris au Begin a Session) ou résolues.
- **Connections et factions** : rang, bond, changements de relation.
- **Assets** : achetés ou améliorés (avec le coût en XP), ou perdus.
- **Secteur** : éléments à consigner dans les cellules explorées (installations, planètes, épaves, vaults, PNJ, créatures, rencontres), avec la coordonnée de cellule (`h-x-y`).
- **Journal** : SYNTHÈSE à remplacer ; fiches PNJ créées ou mises à jour (questions-secrets, réponses tranchées, évolution de la relation).

## 4. Clôture
1. Demande si l'utilisateur veut consigner autre chose hors mécanique (impressions, pistes).
2. Rappelle l'étape technique : après saisie dans Stargazer, réexporter le JSON, en faire la copie allégée (outils du dépôt : `alleger-stargazer.html`, `alleger_export_stargazer.bat` ou `.py`) et la joindre à la prochaine discussion de session (pas dans la connaissance du projet), pour que la prochaine session parte du bon état.
