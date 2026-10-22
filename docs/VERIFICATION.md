# Construction et vérification des données

> Licence : [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Produit non officiel, sans lien avec Tomkin Press.

Ce document explique d'où viennent `SF-01` à `SF-04`, comment ils ont été vérifiés, et ce qui reste à la charge d'une relecture humaine. Les scripts utilisés sont dans [`verification/`](../verification/) : toute personne possédant les livres peut refaire le contrôle.

## Principe

Chaque fichier est comparé à une **source indépendante de celle qui a servi à le construire** ; les désaccords sont ensuite examinés un par un :

| Fichier | Construit à partir de | Vérifié contre |
|---|---|---|
| SF-01 Moves | Datasworn (texte), tables du Reference Guide | **Livre de règles**, édition décembre 2025 (texte des moves et tables) |
| SF-02 Oracles | Reference Guide, juin 2024 | **Livre de règles**, édition décembre 2025, ligne par ligne |
| SF-03 Règles | Codex du Reference Guide | Reference Guide (résumé propre à ce livre) |
| SF-04 Assets | Datasworn | **Cartes d'assets** (*Asset Singles*, janvier 2023), capacité par capacité |

**En cas de désaccord entre deux livres, c'est le livre de règles qui est suivi.**

## Résultats (22 octobre 2026)

### SF-02 et tables de SF-01 — 4 009 lignes
- **3 868 lignes** retrouvées automatiquement sur la page du livre, avec la même plage sur la même ligne imprimée. Pour les matrices (Terminus/Outlands/Expanse, environnements, lifebearing/lifeless), la colonne est aussi contrôlée.
- **Les lignes restantes** appartiennent aux 13 tables dessinées en graphiques, illisibles automatiquement et **vérifiées visuellement page par page** :
  - Environment, et Creature Basic Form (5 colonnes) ;
  - Location des colonies, des épaves et des vaults ;
  - Derelict Zones (Starship et Settlement) ;
  - Planetary Class ;
  - Stellar Object.
- **Écarts corrigés au profit du livre de règles** :
  - *Make a Discovery* : le livre de règles 2025 conserve les plages d'origine (1–4, 5–8, 9–10…), alors que le Reference Guide 2024 en donne d'autres (1–4, 5–9, 10–12…) ;
  - *Rocky World › Atmosphere* : livre 1–65 / 66–85 / 86–90 / 91–100 (sans Breathable), contre 1–65 / 66–80 / 81–85 / 86–95 / 96–100 dans le Reference Guide ;
  - *Story Clue* : « impostor » (orthographe du livre) ;
  - *Vital World › Diversity* : « Garden world (five or more biomes) ».

### SF-01 — texte des 56 moves
Chaque move est aligné mot à mot sur le livre. **Écarts corrigés au profit du livre** :
- *Gather Information* (miss) : « you unearth a dire threat or reveal an unwelcome truth » ;
- *Ask the Oracle* : « resolve questions, discover details, reveal locations » ;
- *Secure an Advantage* (et sa version Scene Challenge) : « With strength, endurance, or aggression » ;
- *Sojourn* : « choose two recover moves » (le jeu de données portait « contents ») ;
- *Face Death* et *Face Desolation* : « death-bound », « soul-bound » ;
- *Finish the Scene* (miss) : « a dire turn of events » ;
- *Fulfill Your Vow*, *Finish an Expedition* : « (none for a troublesome quest / expedition) » ;
- *Test Your Relationship* : « If you refuse or fail, the connection is permanently undone ».

Résidus connus, propres à la mise en page : les tables de *Repair*, *Take Decisive Action* et *Ask the Oracle* sont contrôlées avec les tables. Un mot déplacé dans *Face Danger* est un artefact d'extraction.

### SF-04 — texte des 87 cartes
Chaque capacité est alignée sur la carte. **Écarts corrigés au profit des cartes** :
- *Heavy Cannons* : « Strafe » ;
- *Internal Refit* : « vehicle » (au lieu de « ship » / « vessel ») ;
- *Archer* : « On a miss, take +1 ammo and Sacrifice Resources (-1) » ;
- *Blademaster* : « When you Gain Ground… against a foe, choose one », « this blade », « your oathbound blade » ;
- *Devotant* : « Name it and choose » ;
- *Slayer* : « face your quarry on its own terms ».

Conservé volontairement : *Slayer*, « slay an inhuman foe ». La carte imprime « a inhuman », une coquille évidente.

### SF-03
Texte du Codex du Reference Guide, remis en forme. Les passages propres au jeu à plusieurs ont été omis et quelques redites du glossaire condensées, ce qui est signalé en tête du fichier.

## Contrôle du contrôleur

Pour s'assurer que le script de contrôle ne laisse rien passer, on lui a soumis **291 erreurs volontairement injectées** dans une copie de SF-02 : plage décalée d'une unité, mot remplacé n'importe où dans la ligne, ou deux lignes permutées. **Il les a toutes détectées (291/291).** Le test est reproductible : [`verification/self_test.py`](../verification/self_test.py).

Une relecture humaine ligne à ligne n'est donc pas nécessaire. Le seul risque qu'un script ne couvre pas est un écart entre la couche texte du PDF et ce qui est réellement imprimé. Une quinzaine de pages du livre (dont toutes les tables graphiques) ont été comparées visuellement à leur image, sans aucun écart. Pour un contrôle supplémentaire, [`ECHANTILLON-15.md`](ECHANTILLON-15.md) propose 15 lignes tirées au hasard, à vérifier en une dizaine de minutes (facultatif).

## Différences connues entre éditions (pour information)

Les jeux de données numériques les plus répandus (dont Datasworn 0.0.10) suivent le livre de 2022. Depuis, plusieurs tables ont été réordonnées ou modifiées : Settlement › First Look, Jovian World › Life, Derelict Zones › Settlement, Observed From Space de plusieurs planètes, Derelict › Community/Living › Area, Character Name › Given Name (entrée 99), Endure Harm (ligne 36–50). La bibliothèque suit les livres actuels.

## Limites

Un contrôle, même outillé, n'est pas une garantie absolue. **En cas d'écart avec vos livres, le livre fait foi** : merci de le signaler dans une *issue* (table, ligne, page).
