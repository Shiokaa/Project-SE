# 🌿 Simulateur d'Écosystème — Document d'orientation

> Un monde vivant qui émerge de règles locales minimalistes.
> On ne programme pas le résultat — on programme les règles, et on observe ce qui en sort.

---

## 1. La vision en une phrase

Une grille = un territoire vu du ciel. On y dépose des proies et des prédateurs
qui suivent chacun trois ou quatre règles simples (manger, vieillir, se
reproduire, mourir). À grande échelle, ces règles produisent spontanément des
cycles de populations, des extinctions locales, des reconquêtes — sans qu'on
les ait jamais codés directement.

C'est un **projet d'observation autant que de construction** : une fois le
moteur en place, l'essentiel du temps se passe à poser des questions de biologie
et à regarder le monde y répondre.

---

## 2. Le principe directeur : l'émergence

La règle d'or du projet : **ne jamais coder le résultat global, seulement les
décisions locales d'un individu sur sa case et ses voisines.**

- ❌ « Quand il y a trop de renards, fais mourir 30 % d'entre eux. »
- ✅ « Un renard qui ne trouve pas de proie à portée perd de l'énergie ; à 0, il
  meurt. »

Le crash de la population de renards quand les lapins s'effondrent doit **émerger
tout seul** du second type de règle. C'est ça qui rend le projet fascinant (et
unique sur un GitHub).

---

## 3. Décision d'architecture centrale : moteur ≠ rendu

C'est le choix le plus important du projet, et il répond à ta question
« peut-on mélanger matplotlib et pygame ? » → **oui, justement parce qu'on les
sépare.**

```
┌─────────────────────────────────────────┐
│            MOTEUR (logique pure)          │
│  Monde, Grille, Cellules, Entités,        │
│  règles, boucle step() → un nouvel état   │
│  ⚠️  ne sait PAS qu'il est affiché          │
└───────────────────┬───────────────────────┘
                    │  expose un état lisible
        ┌───────────┼────────────┐
        ▼           ▼            ▼
   ┌─────────┐ ┌──────────┐ ┌──────────┐
   │ Terminal│ │Matplotlib│ │  Pygame  │
   │ (ASCII) │ │ (courbes)│ │ (animé)  │
   └─────────┘ └──────────┘ └──────────┘
```

Concrètement : le moteur expose une méthode `step()` qui fait avancer le monde
d'un tour, et un état (la grille + la liste des entités + des statistiques).
Chaque « renderer » lit cet état et le dessine à sa façon. On peut même en
brancher plusieurs en même temps (ex. pygame pour le monde + matplotlib pour les
courbes de population à côté).

**Règle pratique : aucun `import pygame` ou `import matplotlib` dans le code du
moteur. Jamais.** Si on respecte ça, passer de l'un à l'autre est gratuit.

---

## 4. Le monde

Une grille 2D. Chaque case (cellule) a :

| Attribut        | Description                                              |
|-----------------|----------------------------------------------------------|
| `terrain`       | `EAU`, `HERBE`, `FORET`, `DESERT`                        |
| `ressource`     | quantité de nourriture végétale disponible (0 → max)     |
| `occupant(s)`   | la ou les entités présentes                              |

**L'environnement évolue aussi**, ce ne sont pas que les bestioles qui bougent :
- une case d'herbe **surpâturée** (ressource épuisée trop souvent) → se
  désertifie ;
- une case herbe/désert **laissée tranquille** longtemps → se reforeste
  lentement ;
- l'herbe **repousse** un peu à chaque tour si la case n'est pas saturée.

Détail qui paye énormément : **l'eau crée des barrières naturelles**. Une zone
isolée par l'eau peut développer une population distincte qui évolue à part —
exactement comme une île.

---

## 5. Les habitants

Au minimum deux types, mais tous partagent le même squelette : **énergie, âge,
seuil de reproduction.** Ce sont les trois curseurs de vie/mort.

### Proie (ex. lapin)
- mange la **ressource végétale** de sa case → gagne de l'énergie ;
- **fuit** si un prédateur est dans son voisinage ;
- se **reproduit** si son énergie dépasse un seuil (et qu'une case voisine est libre) ;
- **meurt** si énergie = 0, si trop vieille, ou si mangée.

### Prédateur (ex. renard)
- **chasse** : se déplace vers la proie la plus proche dans son champ de vision ;
- mange une proie adjacente → gagne de l'énergie (et la proie meurt) ;
- se reproduit au-dessus d'un seuil d'énergie ;
- **meurt de faim** si énergie = 0 → c'est ce qui crée le cycle.

> Chaque tour, un individu **dépense un peu d'énergie juste pour exister**
> (métabolisme). Sans ça, rien ne meurt et il n'y a pas de cycle.

---

## 6. La boucle de simulation (un « tour »)

Un tour de monde, dans l'ordre :

1. **Environnement** : repousse des ressources, dé/reforestation des cases.
2. **Entités** (dans un ordre mélangé pour éviter les biais) : chacune
   *perçoit* son voisinage, puis *décide* une action (bouger / manger / fuir /
   chasser / se reproduire).
3. **Vieillissement & mort** : âge +1, retrait des entités à énergie nulle ou
   trop vieilles.
4. **Statistiques** : on enregistre le compte de chaque espèce, l'énergie
   moyenne, etc. → c'est ce que matplotlib trace.

⚠️ **Piège classique** : si tu modifies la grille pendant que tu la parcours,
une bestiole peut « jouer deux fois ». Solution simple au début : marquer chaque
entité comme « déjà agi ce tour-ci ».

---

## 7. Feuille de route (par paliers)

L'idée : à chaque palier, **quelque chose de visible et de jouable**, puis on
empile.

### Palier 0 — Le squelette
- [ ] Structures de base : `Monde`, `Cellule`, `Entite`, enum `Terrain`.
- [ ] Génération d'une grille aléatoire (ou par bruit de Perlin pour de jolis
      continents).
- [ ] Affichage **terminal en ASCII** (`~` eau, `.` herbe, `🌲` forêt, etc.).
- 🎯 *But : voir une carte statique s'afficher.*

### Palier 1 — La vie minimale
- [ ] Proies qui bougent, mangent l'herbe, se reproduisent, meurent.
- [ ] Boucle `step()` + affichage qui se rafraîchit dans le terminal.
- 🎯 *But : voir une population de lapins exploser puis se stabiliser sur les
  ressources.*

### Palier 2 — Le cycle proie-prédateur
- [ ] Ajout des prédateurs (chasse + faim).
- [ ] **Courbes matplotlib** : population de proies vs prédateurs dans le temps.
- 🎯 *But : observer les oscillations de Lotka-Volterra émerger toutes seules.
  C'est LE moment satisfaisant du projet.*

### Palier 3 — Le visuel temps réel
- [ ] Renderer **pygame** : grille colorée, entités animées, contrôles
      (pause, vitesse, clic pour inspecter une case).
- [ ] On garde matplotlib pour les courbes à côté.
- 🎯 *But : une vitrine agréable à regarder.*

### Palier 4 et au-delà — La profondeur (au choix, pioche selon l'envie)
- [ ] **Évolution** : les petits héritent des traits des parents avec une légère
      mutation (vitesse, vision, seuil de repro). Sur des milliers de tours, des
      traits se sélectionnent naturellement.
- [ ] **Mémoire animale** : une entité retient où elle a trouvé de la nourriture
      et y retourne.
- [ ] **Catastrophes** : sécheresse, incendie, et observer la résilience.
- [ ] **Espèce invasive** introduite en cours de route.
- [ ] **🌊 Bascule marine** : plancton (ressource dérivante), bancs de poissons
      (comportement de groupe), prédateurs apex, zones de lumière, courants.
      → Comme le moteur est agnostique, le marin = surtout de nouvelles règles et
      un nouveau set de terrains, pas une réécriture.

---

## 8. Les questions à se poser (le vrai cœur du projet)

À garder sous le coude — chacune est une mini-expérience à lancer et à
documenter (capture d'écran + courbe + une phrase de conclusion → ça fait un
super README) :

- Une espèce **trop spécialisée** (ne mange qu'une ressource rare) survit-elle ?
- Quel est l'effet d'une **ressource rare mais très nutritive** vs abondante mais
  pauvre ?
- Que se passe-t-il si j'introduis une **espèce invasive** à mi-parcours ?
- Une zone **isolée par l'eau** développe-t-elle une dynamique différente ?
- Quels traits l'**évolution** sélectionne-t-elle selon l'environnement ?

---

## 9. Structure de fichiers proposée

```
project-se/
├── docs/
│   └── CONCEPTION.md          ← ce document
├── ecosystem/                 ← le moteur (zéro dépendance de rendu)
│   ├── __init__.py
│   ├── world.py               ← Monde, boucle step()
│   ├── cell.py                ← Cellule, Terrain
│   ├── entities.py            ← Entite, Proie, Predateur
│   └── rules.py               ← repousse, dé/reforestation…
├── renderers/                 ← les afficheurs, interchangeables
│   ├── terminal.py            ← ASCII
│   ├── plots.py               ← courbes matplotlib
│   └── pygame_view.py         ← (palier 3)
├── config.py                  ← tous les curseurs réglables au même endroit
├── main.py                    ← assemble moteur + renderer choisi
└── README.md                  ← la vitrine (vient en dernier)
```

> **Conseil** : mets **tous les paramètres** (taille de grille, énergie de
> départ, coût du métabolisme, vitesse de repousse de l'herbe…) dans
> `config.py`. 90 % du plaisir d'observation vient de tourner ces curseurs et de
> relancer. Si tu dois fouiller dans 5 fichiers pour changer une valeur, tu ne le
> feras pas.

---

## 10. Premier pas concret

Le `main.py` actuel est un « Hello World » Tkinter — il a servi de test, on
peut le recycler. Le tout premier objectif réaliste :

> **Afficher une grille de terrains aléatoires dans le terminal, sans aucune
> bestiole.** (Palier 0)

Une fois que la carte s'affiche, ajouter UNE proie qui bouge au hasard. Puis la
faire manger. On avance toujours par tout petits incréments visibles — c'est ce
qui garde le projet motivant.

---

> Doc de conception rédigée avec l'aide de Claude, sur la base de mes choix de design