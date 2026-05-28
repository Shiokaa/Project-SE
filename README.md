# Project-SE

Le but de ce projet est un entrainement sur python ainsi que la réalisation d'un projet de recherche plutôt qu'une orientation 100% codage.

> Un monde vivant qui émerge de règles locales minimalistes.
> On ne programme pas le résultat — on programme les règles, et on observe ce qui en sort.

---

## Concept

Une grille 2D générée par bruit de Perlin. On y dépose des proies et des prédateurs qui suivent chacun quelques règles simples (manger, vieillir, se reproduire, mourir). À grande échelle, ces règles produisent spontanément des cycles de populations, des extinctions locales, des reconquêtes — sans qu'on les ait jamais codés directement.

Le principe directeur : **ne jamais coder le résultat global, seulement les décisions locales d'un individu.**

---

## Architecture

```
project-se/
├── ecosystem/          ← moteur (zéro dépendance de rendu)
│   ├── world.py        ← génération du monde (Perlin noise)
│   ├── cell.py         ← cellule : terrain + ressource + entité
│   ├── entity.py       ← Entity, Prey, Predator
│   └── field.py        ← enum des terrains
├── renderers/          ← afficheurs interchangeables
│   ├── image.py        ← rendu PNG (Pillow)
│   └── terminal.py     ← rendu ASCII
├── docs/
│   ├── CONCEPTION.md   ← document d'orientation du projet
│   └── learning/       ← notes d'apprentissage Python
└── main.py             ← point d'entrée
```

Le moteur ne sait pas qu'il est affiché. Les renderers lisent l'état du monde et le dessinent à leur façon — on peut en brancher plusieurs simultanément.

---

## Terrains

| Terrain | Description |
|---------|-------------|
| `EAU_PROFONDE` | Barrière naturelle, isole les populations |
| `EAU` | Zone aquatique peu profonde |
| `TERRE` | Zone aride, peu de ressources |
| `HERBE` | Nourriture pour les proies |
| `FORET` | Zone dense |

---

## Feuille de route

- [x] Génération du monde par bruit de Perlin
- [x] Terrains différenciés (5 biomes)
- [x] Cellules avec ressources et entités
- [x] Rendu image PNG et terminal ASCII
- [ ] Proies : déplacement, alimentation, reproduction
- [ ] Prédateurs : chasse, faim, cycle proie-prédateur
- [ ] Courbes de population (matplotlib)
- [ ] Rendu temps réel (pygame)
- [ ] Évolution et mutations

---

## Lancer le projet

```bash
# Installer le venv et les dépendances
make install

# Afficher la commande d'activation du venv
make activate

# Supprimer le venv
make uninstall

# Lancer le projet
python main.py
```
