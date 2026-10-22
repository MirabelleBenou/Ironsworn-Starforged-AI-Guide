# Construction et vérification des données

> Licence : [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Produit non officiel, sans lien avec Tomkin Press.

Ce document explique d'où viennent les fichiers `SF-01` à `SF-04` et comment ils ont été contrôlés, pour que chacun puisse juger de leur fiabilité et signaler les erreurs.

## Sources

| Fichier | Source principale | Référence de contrôle |
|---|---|---|
| SF-01 Moves | [Datasworn](https://github.com/rsek/datasworn) `@datasworn/starforged` 0.0.10 (texte), tables des moves remplacées par celles du Reference Guide | Reference Guide, édition juin 2024 |
| SF-02 Oracles | Plages, ordre et textes extraits du Reference Guide, édition juin 2024 ; structure (noms, hiérarchie) issue de Datasworn | Contrôle visuel des pages à mise en page complexe ; échantillon recoupé avec le livre de règles, édition décembre 2025 |
| SF-03 Règles | Section « Codex » du Reference Guide (rules summary, clocks, scene challenges, glossaire), remise en forme | Reference Guide |
| SF-04 Assets | Datasworn (texte des cartes) | Texte des Asset Sheets |

## Pourquoi ne pas se contenter d'un jeu de données existant

Les jeux de données numériques de Starforged les plus répandus suivent le texte du livre de **2022**. Le **Reference Guide de 2024** (et le livre de règles réédité depuis) a modifié plusieurs tables : plages différentes, entrées réordonnées (souvent par ordre alphabétique), ou formulations corrigées. Un même jet de d100 peut donc donner un résultat différent selon la source. La bibliothèque suit l'édition 2024.

## Différences constatées entre Datasworn 0.0.10 et le Reference Guide 2024

### Plages modifiées
- Make a Discovery (table du move)
- Settlement › First Look (une entrée ajoutée, « Prominent emblems or signage », plages revues)
- Jovian World › Life
- Rocky World › Atmosphere
- Derelict Zones › Settlement (Living 31–55, Medical 56–65, Operations 66–75, Production 76–90)

### Ordre ou texte des entrées modifié (plages identiques)
- Observed From Space : Grave, Ice, Jungle, Shattered, Tainted et Vital World (entrées réordonnées)
- Derelict › Community › Area et Derelict › Living › Area (entrées réordonnées)
- Character Name › Given Name (entrée 99)
- Endure Harm, ligne 36–50 (formulation)
- Vital World › Diversity (formulation)

### Texte des moves corrigé
- Fulfill Your Vow : « make the legacy reward one rank lower (none for a troublesome quest) »
- Finish an Expedition : « (none for a troublesome expedition) »
- Test Your Relationship : « If you refuse or fail, the connection is permanently undone. »

### Coquilles du jeu de données corrigées
- Callsign 48 : « Ironclad »
- « impassable »

## Méthode d'extraction et de contrôle

1. Extraction des lignes « plage + texte » du PDF du Reference Guide avec leurs coordonnées, reconstitution des colonnes et des tables multi-colonnes (Terminus / Outlands / Expanse, environnements des créatures, lifebearing / lifeless).
2. Association de chaque table extraite à la table Datasworn correspondante (similarité des textes, page attendue).
3. Contrôles automatiques : plages continues de 1 à 100 sans trou ni chevauchement, cohérence des textes avec la table de référence.
4. Contrôle visuel, page par page, des tables à mise en page particulière (cartes de zones, matrices, listes de noms) et des tables que l'extraction ne lisait pas correctement.
5. Recoupement d'un échantillon de points avec le livre de règles (édition décembre 2025) : concordant.

Les lignes « -- » du Reference Guide (résultat impossible pour ce type de planète ou de région) sont omises des tables. Les « Sample Names » des planètes et les « name tags » des colonies sont des listes dans le Reference Guide : ils sont présentés comme des listes, sans jet.

## Limites

Ce contrôle n'est pas une relecture humaine ligne à ligne des quelque 240 tables. **En cas d'écart avec vos livres, le livre fait foi.** Merci de signaler toute erreur dans une *issue* en indiquant la table, la ligne et la page du livre.
