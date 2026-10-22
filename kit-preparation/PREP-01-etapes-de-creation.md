# Ironsworn: Starforged — Étapes de Création

> Licence : [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). This work is based on Ironsworn: Starforged, created by Shawn Tomkin, and licensed for our use under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license. Produit non officiel, sans lien avec Tomkin Press.

> Résumé procédural du Chapitre 2 (p. 82–135). Les **choix retenus** (Vérités, personnage, secteur) sont stockés dans le JSON de campagne — ce fichier ne décrit que la **méthode** et fournit des tables d'inspiration. Moves, oracles et textes d'assets : voir SF-01 (moves), SF-02 (oracles) et SF-04 (assets) dans la connaissance du projet. Texte intégral du chapitre : PREP-02.

---

## ⚠️ Règle des assets au démarrage (à ne pas tromper)

Un personnage de départ possède **4 assets** :

- **1 STARSHIP** (command vehicle, fourni d'office, 1re capacité active)
- **2 Paths** (choisis à l'étape 2)
- **1 asset final** au choix : Module, Support Vehicle, Companion **ou** Path (étape 6)

> Le livre dit « *three starting assets along with your STARSHIP* » = 2 Paths + 1 asset final = **3 assets + le STARSHIP**.
> ❌ Erreur fréquente : croire qu'on est limité à « 2 Paths + le STARSHIP ». **Non** — l'asset final de l'étape 6 s'ajoute.

- Les **Deeds** ne sont pas disponibles au départ (ils se gagnent en jeu, notamment via des triggers de legacy track).
- Seule la **1re capacité** de chaque asset est active au départ. *Le chapitre 2 ne l'énonce explicitement que pour le STARSHIP ; pour les autres assets, cela vient de la règle générale du Reference Guide (« la 1re capacité est activée à l'achat ») et des cartes (1re case pré-marquée).*

---

## 1. Choisir ses Vérités (univers)

*45-60 min. Pour chacune des 14 catégories (Cataclysme, Exode, Communautés, Fer, Lois, Religion, Magie, Communication & Données, Médecine, IA, Guerre, Formes de vie, Précurseurs, Horreurs) : chaque catégorie propose 3 options, chacune avec des quêtes de départ et des assets suggérés.*

**Trois méthodes possibles** (à mélanger librement) :
1. **Choisir** l'option qui inspire,
2. **Roller** 1d100 sur la catégorie,
3. **Inventer sa propre vérité** personnalisée.

- Certaines vérités incluent des **sous-choix** en tables oracles (ex. cause du cataclysme, origine des pouvoirs des paragons) : là aussi, choisir, roller ou personnaliser.
- **Catégorie sans intérêt ?** On peut l'ignorer pour l'instant et la décider **plus tard, en jeu** — le livre le permet explicitement.
- Les contradictions entre catégories peuvent être pliées au setting… ou gardées comme graines d'histoires.

**Hypothèses par défaut** (point de départ « généralement vrai », **ajustable via les Vérités** — pas des vérités gravées) : périlleux, les humains sont seuls dans la galaxie, divers, éparpillé, inexploré, merveilleux, rétro-futur, injuste, porteur d'espoir.

→ **Résultat à reporter dans le JSON.** Ne pas re-détailler ici.

---

## 2. Créer son Personnage

*20-30 min.*

1. Préparer les assets (écarter les Deeds)
2. **Choisir 2 Paths** (attention aux Vérités : sans magie, KINETIC/FIREBRAND/SEER peuvent être réinterprétés en tech ou ignorés)
3. **Backstory** — ce qui vous a séparé de votre foyer (simple, on peut la découvrir en jeu)
4. **Vœu de background** — motivation profonde, rang **ÉPIQUE**, déjà juré (pas de move). *On peut le laisser vide pour l'ajouter en jeu.*
5. **STARSHIP** — prendre l'asset, nommer le vaisseau, lui donner une histoire (table Origine) et une personnalité (table Particularités)
6. **Asset final** — Module / Support Vehicle / Companion / Path
7. **Stats** — répartir **3, 2, 2, 1, 1** dans Edge, Heart, Iron, Shadow, Wits
8. **Jauges** — Health=5, Spirit=5, Supply=5, Momentum=+2, Max=+10, Reset=+2 ; intégrité des véhicules et santé des companions à max
9. Envisager le personnage (apparence, comportement, tenue — 1-2 faits chacun suffit)
10. Nommer (nom, pronoms, callsign optionnel)
11. Équipement — spacer kit (combinaison étanche, lampes, outils, medkit, communicateur) + 4-5 items personnels au plus ; penser à l'**objet sur lequel on prête ses serments de fer** (histoire, importance)

### Inspiration — Backgrounds (2 Paths)
| d100 | Background | Paths |
|---|---|---|
| 1-5 | Médecin de guerre | HEALER ; VETERAN |
| 6-10 | Délégué | BANNERSWORN ; DIPLOMAT |
| 11-15 | Exobiologiste | LORE HUNTER ; NATURALIST |
| 16-20 | Commerçant interstellaire | NAVIGATOR ; TRADER |
| 21-25 | Chasseur de fugitifs | ARMORED ; BOUNTY HUNTER |
| 26-30 | Hacker | INFILTRATOR ; TECH |
| 31-35 | Pilote chevronné | ACE ; NAVIGATOR |
| 36-40 | Éclaireur interstellaire | EXPLORER ; VOIDBORN |
| 41-45 | Chasseur de monstres | GUNNER ; SLAYER |
| 46-50 | Occultiste | OUTCAST ; SHADE |
| 51-55 | Agent secret | INFILTRATOR ; BLADEMASTER |
| 56-60 | Hors-la-loi | FUGITIVE ; GUNSLINGER |
| 61-65 | Détective privé | BRAWLER ; SLEUTH |
| 66-70 | Prophète | DEVOTANT ; SEER |
| 71-75 | Psionique | KINETIC ; VESTIGE |
| 76-80 | Contrebandier | COURIER ; SCOUNDREL |
| 81-85 | Spiritualiste | HAUNTED ; EMPATH |
| 86-90 | Ingénieur de vaisseau | GEARHEAD ; TECH |
| 91-95 | Super-soldat | AUGMENTED ; MERCENARY |
| 96-100 | Pilleur de tombes | SCAVENGER ; SCOUNDREL |

### Inspiration — Backstory
| d100 | Backstory |
|---|---|
| 1-7 | Abandonné les vôtres après une vérité troublante |
| 8-13 | Guidé par une vision ou prophétie |
| 14-20 | Hanté par des actions/échecs passés |
| 21-27 | Fuit un passé criminel |
| 28-34 | Seul survivant d'une attaque/calamité |
| 35-40 | Échappé d'une situation abusive ou injuste |
| 41-46 | Aucun souvenir de sa vie antérieure |
| 47-53 | Rejeté un devoir ou une destinée |
| 54-60 | Banni de son foyer |
| 61-67 | Privé d'un héritage |
| 68-74 | Seul depuis toujours |
| 75-81 | Envoyé en mission prolongée |
| 82-87 | Enlevé ou attiré ailleurs par quelqu'un |
| 88-94 | Ambitions dépassant ses origines |
| 95-100 | Soif d'aventure |

### Inspiration — Origine du STARSHIP
| d100 | Origine |
|---|---|
| 1-8 | Échangé contre un héritage familial précieux |
| 9-17 | Construit en ferraille recyclée |
| 18-25 | Butin de guerre |
| 26-34 | Découvert abandonné, réparé |
| 35-42 | Gagné contre une promesse ou un vœu |
| 43-50 | Trouvé abandonné en parfait état |
| 51-58 | Accordé par une organisation ou communauté |
| 59-67 | Hérité d'un proche/mentor |
| 68-75 | Acheté à un prix suspect |
| 76-84 | Volé à un caïd notoire ou à une organisation criminelle |
| 85-92 | Pris en fuyant une attaque ou une catastrophe |
| 93-100 | Gagné à un pari |

### Inspiration — Particularités du STARSHIP
| d100 | Particularité |
|---|---|
| 1-5 | Salle des machines marquée de vieilles brûlures |
| 6-10 | Coque couverte de rouille et de crasse |
| 11-15 | Une musique fantôme résonne faiblement dans les couloirs |
| 16-20 | Générateur de gravité notoirement capricieux |
| 21-25 | Coque fusionnée avec des excroissances organiques |
| 26-30 | La coque tremble et gémit en vol atmosphérique |
| 31-35 | Intérieur encombré de câbles et conduits apparents |
| 36-40 | A l'air inoffensif, mais des panneaux s'ouvrent sur des armes |
| 41-45 | Journaux de bord avec des coordonnées de lieux inexistants — ou qui ne devraient pas exister |
| 46-50 | Une vieille tache de sang dans le sas réapparaît même repeinte |
| 51-55 | Fut un beau vaisseau, aujourd'hui marqué par une bataille |
| 56-60 | Une coque rapiécée couvre une brèche catastrophique récente |
| 61-65 | Plaques et étiquettes dans une langue peu courante |
| 66-70 | Ponts à plaques amovibles donnant accès à des caches |
| 71-75 | Train d'atterrissage segmenté qui se déplie comme des pattes d'araignée |
| 76-80 | Propulsé par un dispositif précurseur antique |
| 81-85 | Graffitis marqués sur la coque lors d'une récente escale |
| 86-90 | D'étranges symboles griffonnés sur le pont et les cloisons du couloir principal |
| 91-95 | Les objets disparaissent sans explication logique |
| 96-100 | Horloges et minuteurs toujours légèrement décalés |

---

## 3. Construire un Secteur de Départ

*30-45 min. Exercice **optionnel** : on peut utiliser le secteur pré-généré du livre (Devil's Maw, p. 127) ou jouer en galaxie free-form sans secteurs.*

1. **Région** — Terminus / Outlands / Expanse. *Jamais le Void.*
2. **Nombre de colonies** — Terminus 4 / Outlands 3 / Expanse 2
3. **Colonies** — pour chacune : Nom, Location, Population, Autorité, Projects (1-2 rolls). Ne pas roller les autres tables maintenant.
4. **Planètes** — type + nom (sample names) pour chaque colonie planetside **ou en orbite** ; ne pas roller les autres tables de planète
5. **Étoiles** (optionnel)
6. **Carte** — placer les colonies (abstrait, pas de distances littérales)
7. **Passages** — Terminus=3, Outlands=2, Expanse=1 (relient colonies entre elles ou au bord de carte)
8. **Zoom sur 1 colonie** — First Look (1-2), Settlement Trouble ; **si planetside ou en orbite** : Atmosphere, Observed from Space (1-2), Planetside Feature (1-2) ; si Vital World : Diversity + Biomes (ne pas roller la table Settlements de la planète)
9. **Connexion locale** — 1 connection (Make a Connection avec **hit fort automatique**) : Role, Rank (**troublesome ou dangereux conseillé** pour une connection de départ), Home, Name, caractéristiques (First Look 1-2, Character Goal, Revealed Character Aspect 1-2)
10. **Trouble du secteur** — inventer ou roller (table ci-dessous)
11. **Finaliser** — nommer le secteur (table Sector Name optionnelle), faction de contrôle optionnelle (garder ambigu si pas évident)

### Inspiration — Sector Trouble
| d100 | Trouble |
|---|---|
| 1-5 | Blocus commercial avec d'autres secteurs |
| 6-10 | Des chasseurs de primes traquent un fugitif notoire |
| 11-15 | Des brèches spatio-temporelles chaotiques se propagent comme une traînée de poudre |
| 16-20 | Faction criminelle corrompt les autorités |
| 21-25 | Superarme dévastatrice en mauvaises mains |
| 26-30 | Les tempêtes d'énergie font rage |
| 31-35 | Perturbations magnétiques des communications |
| 36-40 | Ressource découverte attire les chasseurs de fortune |
| 41-45 | Un clan de pirates notoire s'attaque aux vaisseaux |
| 46-50 | Des formes de vie parasites se répandent comme une peste |
| 51-55 | Sites précurseurs émettent des signaux étranges |
| 56-60 | Prophéties d'un réveil terrible imminent |
| 61-65 | Clan de raiders dominant sous un nouveau chef |
| 66-70 | Des zélotes religieux envahissent le secteur |
| 71-75 | IA rogue infiltre les systèmes |
| 76-80 | Colonies/factions au bord de la guerre |
| 81-85 | Vaisseaux disparaissent régulièrement |
| 86-90 | La maladie se propage parmi les vaisseaux et les colonies |
| 91-95 | Supernova imminente |
| 96-100 | Une forme de vie spatiale titanesque rôde sur les routes spatiales |

---

## 4. Commencer l'Aventure

*10-20 min.*

1. **Incident déclencheur** — doit être : personnel, persistant, urgent (ticking clock), à forts enjeux, de portée limitée. Rang du vœu initial : **troublesome** ou **dangereux**. Pistes : truths et leurs quest starters, paths, backstory, vaisseau, colonies (projets, troubles), connection, trouble du secteur ; sinon oracles Action + Theme, Character Goal, ou la table ci-dessous.
2. **Poser la scène** — prologue (vie quotidienne, l'incident arrive ensuite) ou in medias res (action directe)
3. **Swear an Iron Vow** — roll +heart (+1 si juré à une connection ; +2 si bond partagé — inapplicable au départ puisqu'aucun bond n'existe encore)

### Inspiration — Incident déclencheur
| d100 | Idée |
|---|---|
| 1-5 | Aider un vaisseau pris dans une fracture spatio-temporelle |
| 6-10 | Négocier la paix entre deux colonies rivales |
| 11-15 | Cartographier un nouveau passage entre des colonies isolées |
| 16-20 | Colonie à défendre contre des raiders |
| 21-25 | Découvrir qui a saboté les épurateurs d'air |
| 26-30 | Escorter un vaisseau de commerce et sa cargaison précieuse |
| 31-35 | Conduire une équipe de secours vers un site sinistré |
| 36-40 | Infiltrer une base fortifiée pour voler des données |
| 41-45 | Enquêter sur des manifestations terrifiantes dans une colonie isolée |
| 46-50 | Libérer des prisonniers d'un camp de travail |
| 51-55 | Retrouver un spationaute échoué sur une planète inhabitée |
| 56-60 | Protéger un fugitif d'un chasseur impitoyable |
| 61-65 | Récupérer un artefact pré-Exode précieux à un ennemi |
| 66-70 | Équipage à libérer de mutins |
| 71-75 | Récupérer une cache d'armes volées sur un vaisseau pirate |
| 76-80 | Installation ennemie à saboter |
| 81-85 | Expédition perdue dans un vault précurseur |
| 86-90 | Protéger une forme de vie merveilleuse de ceux qui veulent la détruire |
| 91-95 | Bête ravageuse à traquer et abattre |
| 96-100 | Peuple déplacé à transporter |

---

## 5. Mécaniques express (rappel)

- **Action roll** : `d6 + stat + adds` vs `2d10`. Strong = bat les 2 ; Weak = bat 1 ; Miss = bat 0 (égalité = échec). Score max 10. **Match** (2d10 identiques) = twist ou opportunité.
- **Momentum** : -6 à +10. Burn = remplacer le score par le momentum puis reset. Reset +2 (réduit par impacts).
- **Progress** : Troublesome 3 cases · Dangereux 2 · Formidable 1 · Extrême 2 ticks · Épique 1 tick. 4 ticks = 1 case. Progress move = cases complètes vs 2d10, sans momentum (ni burn, ni momentum négatif).
- **Stats** : Edge (agilité/distance) · Heart (courage/empathie) · Iron (force/proche) · Shadow (ruse) · Wits (savoir/observation).
- **Assets** : achat 3 XP (1re capacité) · upgrade 2 XP (2e/3e, dans n'importe quel ordre). Ne s'appliquent **pas** aux progress moves sauf mention explicite.
- **XP** : 2 par case de legacy track remplie ; **une fois la 10e case remplie, la piste est vidée et ne rapporte plus que 1 XP par case** (et compte comme 10 sur un progress roll). Legacy tracks : Quests / Bonds / Discoveries.
- **Impacts** : -1 max momentum chacun. Reset réduit (1 impact → +1, 2+ → 0). Les troubles véhicules ne comptent que si on est à bord.
- **Oracles** : Yes/No (Small Chance ≤10, Unlikely ≤25, 50/50 ≤50, Likely ≤75, Almost Certain ≤90) · d100 = 2d10 (dizaines/unités décidés avant le jet) · match = twist.

---

## 📋 Changelog (v3)

Vérification stricte contre le Chapitre 2 (PDF p. 82–135) :

1. **Plages** des 6 tables d'inspiration (Backgrounds, Backstory, Origine, Particularités, Sector Trouble, Incident) : toutes conformes, aucune modification.
2. **Traductions** corrigées ou complétées quand le sens dérivait : Particularités 56-60 (« coche » → coque rapiécée) ; Sector Trouble 6-10, 11-15, 26-30 (« rampantes » = contresens), 41-45, 46-50, 66-70, 86-90, 96-100 ; Origine 76-84 ; Incident 11-15, 41-45, 86-90.
3. **Secteur** renuméroté en 11 étapes comme le livre (le nombre de colonies est une étape à part) ; ajout « ne pas roller les autres tables de planète / la table Settlements de la planète ».
4. **Équipement** : contenu du spacer kit et objet de serment ajoutés.
5. **Incident** : sources d'inspiration du livre ajoutées.

## 📋 Changelog (v2)

Corrections par rapport à la v1, après confrontation au Chapitre 2 (p. 82–135) :

1. « Hypothèses fixes (toujours vraies) » → reformulées en **hypothèses par défaut ajustables** (le livre dit « generally true », avec exceptions identifiées via les Vérités).
2. **Vérités** : ajout de la 3e méthode (inventer sa vérité), des sous-oracles, et de la possibilité de **différer** une catégorie en jeu.
3. **Étape 3 du secteur** : « si planetside » → « si planetside **ou en orbite** » (bug jouable corrigé).
4. Ajout de la table **Particularités du STARSHIP** (20 entrées, p. 109).
5. Mention du **secteur pré-généré** (Devil's Maw) et de l'option free-form.
6. **Connection** : rang conseillé (troublesome/dangereux) et détail des caractéristiques ajoutés ; formulation « hit fort automatique » précisée.
7. **Vœu de background** : possibilité de le laisser vide ajoutée.
8. **Table des incidents** : 21-25 (re-sabotage → enquête « découvrir qui »), 71-75 (« cache d'armes volées »), et quelques autres entrées re-traduites fidèlement.
9. **Règle « 1re capacité active »** : sourcée correctement (explicite pour le STARSHIP dans le chap. 2 ; générale via le Reference Guide).
10. **Swear an Iron Vow** : ajout du +2 si bond partagé (inapplicable au départ).
11. **XP legacy** : clarification — après la 10e case, la piste est **vidée** et rapporte 1 XP/case (pas seulement « après la 10e ») ; + précision sur les troubles véhicules et le d100 (dizaines/unités).

---
*Textes complets : SF-01 (moves), SF-02 (oracles), SF-04 (assets) ; chapitre 2 intégral : PREP-02.*