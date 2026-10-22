# Ironsworn: Starforged — AI Guide (Claude)

> **Produit non officiel.** Ce dépôt n'est ni affilié, ni approuvé par Tomkin Press ou Shawn Tomkin. Il ne remplace pas les livres : il faut posséder *Ironsworn: Starforged* pour y jouer.
>
> This work is based on Ironsworn: Starforged, created by Shawn Tomkin, and licensed for our use under the Creative Commons Attribution 4.0 International License and the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license. Voir [Licences](#licences).

## English summary

A ready-to-use configuration for running a **solo Ironsworn: Starforged campaign with Claude** (Claude.ai *Projects* + a *skill*), with the player always keeping control:

- **The player rolls every die and every oracle.** The AI identifies the move or table, checks the range and interprets. It never simulates, picks or proposes a result.
- **The [Stargazer](https://nboughton.uk/apps/stargazer/#/) export (JSON) is the single source of truth** for the campaign state. The AI proposes changes, the player enters them.
- **A pinned "SYNTHÈSE" journal entry** is rewritten at the end of each session, so every new chat starts from a compact, reliable state.
- **A verified rules library** in Markdown: moves, oracles (ranges and order of the **2024 Reference Guide**, which reordered several tables compared to older digital datasets), core rules and assets. Built from CC BY 4.0 text.
- **A session-closing skill** (End a Session, XP from legacy tracks, list of Stargazer edits).
- **A preparation kit** for creating a new campaign (chapter 2 of the rulebook, CC BY-NC-SA 4.0).
- **Small tools** to strip embedded images from Stargazer exports (≈2.4 MB → ≈30 KB), including a browser page that works on Android.

The prompts and documentation are in **French**; the rules text is in English, as in the books. Licensing: rules library CC BY 4.0, preparation kit and setting summary CC BY-NC-SA 4.0, method files CC BY 4.0, tools MIT.

---

## Sommaire
1. [Pourquoi ce dépôt](#pourquoi-ce-dépôt)
2. [Principes de la méthode](#principes-de-la-méthode)
3. [Contenu du dépôt](#contenu-du-dépôt)
4. [Prérequis](#prérequis)
5. [Mise en place](#mise-en-place)
6. [Le cycle de jeu](#le-cycle-de-jeu)
7. [Conseils d'usage](#conseils-dusage)
8. [Vérification des données et limites](#vérification-des-données-et-limites)
9. [Adapter à votre campagne](#adapter-à-votre-campagne)
10. [Licences](#licences)
11. [Crédits](#crédits)

---

## Pourquoi ce dépôt

Utiliser une IA comme « Sworn Guide » (meneur de jeu) pour Starforged en solo pose toujours les mêmes problèmes :

- **les règles citées de mémoire**, souvent fausses (moves inventés, plages d'oracles approximatives, mécaniques d'autres jeux) ;
- **les dés « simulés » par l'IA**, qui ne sont pas du hasard ;
- **l'état de la campagne qui dérive** d'une discussion à l'autre ;
- **le contexte qui sature** avec des PDF de plusieurs dizaines de Mo.

Ce dépôt propose une configuration testée qui répond à chacun de ces points, et la méthode pour la reproduire.

## Principes de la méthode

| Principe | Mise en œuvre |
|---|---|
| Le texte fait foi, pas la mémoire de l'IA | Bibliothèque Markdown exacte (SF-01 à SF-04). Règle d'or : ne jamais citer un move, un oracle ou un asset sans l'avoir relu. |
| Les dés sont au joueur | L'IA annonce le move, la stat et les adds ; le joueur lance ; l'IA calcule et interprète. Même chose pour les oracles. |
| Une seule source de vérité | L'export Stargazer (JSON allégé), joint à chaque discussion de session. L'IA propose les changements, le joueur les saisit. |
| Un état compact et fiable | Une entrée de journal épinglée « SYNTHÈSE », réécrite à chaque fin de session. |
| Des secrets qui restent des secrets | Les secrets de PNJ sont notés comme des **questions**, tranchées à l'oracle au moment de la révélation. |
| Pas d'adoucissement systématique | Pay the Price suit le Reference Guide : la conséquence la plus évidente ou la plus intéressante, ou la table, ou l'oracle. |
| Un contexte maîtrisé | ≈ 88 000 tokens de bibliothèque, mis en cache par le Projet ; le kit de création n'est chargé que lorsqu'il sert. |

## Contenu du dépôt

```
projet-claude/
  instructions-projet.md          → à coller dans les instructions du Projet Claude
  connaissance/                   → à déposer dans la connaissance du Projet
    SF-00-sworn-guide.md          protocole de session (rôle, dés, Begin a Session, style)
    SF-01-moves.md                texte exact de tous les moves et de leurs tables
    SF-02-oracles.md              toutes les tables d'oracles (plages du Reference Guide 2024)
    SF-03-regles.md               règles de base, clocks, scene challenges, glossaire
    SF-04-assets.md               texte de toutes les cartes d'assets
    SF-05-lore.md                 synthèse du cadre de la Forge (en français)
  skill/starforged-session/
    SKILL.md                      skill de clôture de session
kit-preparation/                  → à joindre à une discussion lors de la création d'une campagne
  PREP-00-mode-preparation.md     protocole de création
  PREP-01-etapes-de-creation.md   résumé procédural et tables d'inspiration (français)
  PREP-02-rulebook-chap2.md       texte du chapitre 2 du livre (Launching Your Campaign)
outils/
  alleger-stargazer.html          page web : allège un export Stargazer (PC, Android, iOS)
  alleger_export_stargazer.bat    Windows : glisser-déposer l'export sur ce fichier
  alleger_export_stargazer.ps1    script PowerShell appelé par le .bat
  alleger_export_stargazer.py     alternative Python (multi-plateforme)
docs/
  VERIFICATION.md                 comment les données ont été construites et vérifiées
```

## Prérequis

- **Les livres** *Ironsworn: Starforged* (livre de règles, Reference Guide, assets) : [tomkinpress.com](https://tomkinpress.com/pages/ironsworn-starforged). Ce dépôt les complète, il ne les remplace pas.
- **[Stargazer](https://nboughton.uk/apps/stargazer/#/)**, application web de suivi de campagne Starforged qui exporte la campagne en JSON. La méthode repose sur cet export ; un autre outil exportant un état complet peut convenir en adaptant les fichiers.
- **Un abonnement Claude payant** (Pro ou supérieur) pour les Projets et une capacité de connaissance suffisante. Les skills nécessitent, à la date de rédaction, que l'exécution de code et la création de fichiers soient activées dans les réglages.

## Mise en place

1. **Créer un Projet** dans Claude, par exemple « Starforged — ma campagne ».
2. **Instructions du Projet** : coller le contenu de `projet-claude/instructions-projet.md` (la ligne de licence en tête peut être omise).
3. **Connaissance du Projet** : déposer les six fichiers de `projet-claude/connaissance/`. Ne pas y mettre les PDF des livres : ils dépassent souvent la limite de 30 Mo par fichier et leur extraction texte casse les tables en colonnes.
4. **Skill** : compresser le dossier `projet-claude/skill/starforged-session/` en `.zip`, puis l'ajouter dans les réglages de Claude, section Skills. Le skill se déclenche quand on demande la fin de session ; on peut aussi le nommer explicitement.
5. **Outil d'allègement** : garder `outils/alleger-stargazer.html` sur son appareil (ou le `.bat` + `.ps1` sous Windows).
6. **Personnaliser** `SF-00` si besoin (langue, ton, conventions). Le ton propre à une campagne se met plutôt dans la SYNTHÈSE.

## Le cycle de jeu

### 1. Créer une campagne (une seule fois)
1. Dans Stargazer, faire les choix de création (truths, personnage, secteur) au fil de l'eau.
2. Ouvrir une discussion **dans le Projet**, y joindre les trois fichiers de `kit-preparation/`, et l'export JSON allégé s'il existe déjà.
3. L'IA déroule les étapes du chapitre 2, une à la fois, et liste après chaque étape les saisies à faire dans Stargazer.
4. En fin de préparation : saisir dans Stargazer, épingler la première SYNTHÈSE dans le journal, exporter et alléger le JSON. Le kit n'est plus nécessaire.

### 2. Jouer une session
1. Exporter la campagne depuis Stargazer et l'alléger (voir [outils](#outils)).
2. Ouvrir une **nouvelle discussion** dans le Projet, joindre le `-light.json`, écrire **« Begin a Session »**.
3. L'IA confirme l'état, vérifie les flags, fait le recap, traite les campaign clocks, propose une vignette optionnelle et pose la scène.
4. Conventions : dialogue du personnage entre "guillemets", hors-jeu entre `<crochets>`, `<recap>` pour un point d'état.

### 3. Clore la session
1. Demander **« End a Session »**. Le skill de clôture rattrape la progression oubliée (Develop Your Relationship, Reach a Milestone), propose le focus de la prochaine session (+1 momentum), puis produit :
   - la nouvelle **SYNTHÈSE** à coller dans l'entrée de journal épinglée ;
   - la liste ligne par ligne des **saisies Stargazer** (legacy et XP, momentum, jauges, impacts, vœux, clocks, secteur, PNJ).
2. Saisir dans Stargazer, puis exporter et alléger pour la prochaine fois.

### Outils
Un export Stargazer pèse souvent plusieurs Mo à cause des images du journal encodées en base64. Les outils les retirent sans toucher à l'original :
- **`alleger-stargazer.html`** : ouvrir la page dans un navigateur (Android compris), choisir l'export, choisir la campagne à garder si le fichier en contient plusieurs, télécharger ou partager le résultat. Tout se fait localement.
- **Windows** : glisser l'export sur `alleger_export_stargazer.bat`.
- **Python** : `python alleger_export_stargazer.py export.json`.

## Conseils d'usage

- **Modèle** : un modèle rapide suffit pour jouer ; un modèle plus puissant, ou un effort de réflexion plus élevé, est préférable pour la clôture, la préparation et les arbitrages de règles délicats.
- **Discussions courtes** : une discussion par session. La SYNTHÈSE assure la continuité.
- **Un seul état de campagne** : ne pas laisser un ancien export dans la connaissance du Projet si un nouveau est joint à la discussion.
- **Une seule campagne par export** : supprimer les campagnes vides dans Stargazer (la page HTML permet aussi de n'en garder qu'une).
- **Mémoire de l'IA** : elle reste faillible. SF-00 lui demande de signaler toute incohérence ; vérifiez les calculs importants.

## Vérification des données et limites

- **Moves et assets** : textes issus de [Datasworn](https://github.com/rsek/datasworn) (données officielles sous CC BY 4.0), corrigés là où le Reference Guide 2024 diffère.
- **Oracles** : plages et ordre extraits du **Reference Guide (édition juin 2024)**, qui a réordonné plusieurs tables par rapport aux données de 2022 encore utilisées par certains outils. Les tables à mise en page complexe ont été contrôlées visuellement page par page, et un échantillon a été recoupé avec le livre de règles (édition décembre 2025).
- **Limites** : la vérification n'est pas une relecture humaine ligne à ligne de chaque table. Si vous trouvez un écart avec vos livres, **le livre fait foi** : ouvrez une *issue*.
- Détails et liste des différences connues : [`docs/VERIFICATION.md`](docs/VERIFICATION.md).

## Adapter à votre campagne

- Les fichiers ne contiennent aucune donnée de campagne : tout ce qui est propre à votre partie vit dans Stargazer (et donc dans le JSON).
- Le ton, les interdits et les flags se notent dans la SYNTHÈSE ; `SF-00` reste générique.
- Pour jouer dans une autre langue, traduire `SF-00`, `instructions-projet.md` et le skill ; garder les noms de moves, d'assets et d'oracles en anglais facilite la correspondance avec la bibliothèque.

## Licences

| Contenu | Licence | Raison |
|---|---|---|
| `projet-claude/connaissance/SF-01` à `SF-04` | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Texte du Reference Guide et des cartes d'assets, sous CC BY 4.0 |
| `projet-claude/connaissance/SF-05-lore.md`, `kit-preparation/` | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) | Dérivés du texte du livre de règles, sous CC BY-NC-SA 4.0 (usage non commercial, partage à l'identique) |
| `SF-00`, `instructions-projet.md`, `skill/`, `README.md`, `docs/` | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Méthode originale de ce dépôt |
| `outils/` | [MIT](outils/LICENSE) | Code |

Licences de Starforged : [Tomkin Press — Licensing](https://tomkinpress.com/pages/licensing). Ces licences ne couvrent que le texte : **aucune illustration, aucun logo ni élément graphique** des livres n'est inclus dans ce dépôt. Voir aussi [`LICENSE.md`](LICENSE.md).

## Crédits

- *Ironsworn: Starforged* © Shawn Tomkin — [Tomkin Press](https://tomkinpress.com).
- [Datasworn](https://github.com/rsek/datasworn) (rsek) pour la structure des données et les textes de base.
- [Stargazer](https://nboughton.uk/apps/stargazer/#/) (Nick Boughton), pour le suivi de campagne et l'export JSON.
- Fichiers assemblés et vérifiés avec l'aide de Claude (Anthropic).

*Dernière mise à jour : octobre 2026.*
