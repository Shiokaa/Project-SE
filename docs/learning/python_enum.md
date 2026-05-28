# Les Enums en Python

Un enum = un ensemble de valeurs **nommées et fixes**.

## Créer un enum

```python
from enum import Enum

class Terrain(Enum):
    EAU    = 1
    HERBE  = 2
    FORET  = 3
    DESERT = 4
```

## Utiliser un enum

```python
# Accéder à une valeur
t = Terrain.HERBE

# Comparer
if t == Terrain.HERBE:
    print("c'est de l'herbe")

# Récupérer le nom et la valeur
print(t.name)   # "HERBE"
print(t.value)  # 2

# Boucler sur toutes les valeurs
for terrain in Terrain:
    print(terrain.name)  # EAU, HERBE, FORET, DESERT
```

## Auto() — valeurs automatiques

Si les valeurs numériques ne t'importent pas :

```python
from enum import Enum, auto

class Terrain(Enum):
    EAU    = auto()  # 1
    HERBE  = auto()  # 2
    FORET  = auto()  # 3
    DESERT = auto()  # 4
```

## Utiliser l'enum comme type

```python
def describe(terrain: Terrain) -> str:
    if terrain == Terrain.EAU:
        return "zone aquatique"
    elif terrain == Terrain.FORET:
        return "zone boisée"
    ...
```

## Résumé

| Quand utiliser un enum ? |
|--------------------------|
| Ensemble de valeurs fixes et nommées |
| Remplace les "magic strings" comme `"eau"`, `"herbe"` |
| Évite les fautes de frappe (`Terrain.HREBS` → erreur immédiate) |
