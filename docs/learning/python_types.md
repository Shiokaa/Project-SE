# Les types en Python

## Type hints (annotations)

Python est dynamique — les types ne sont pas obligatoires. Mais on peut les annoter pour la lisibilité et l'aide de l'IDE.

```python
# Sans type hints
def world(y, x, scale):
    pass

# Avec type hints
def world(y: int, x: int, scale: float) -> list:
    pass
```

Les type hints **n'empêchent pas** de passer le mauvais type à l'exécution — c'est indicatif.

## Types de base

```python
x: int     = 5
y: float   = 3.14
nom: str   = "lapin"
vivant: bool = True
```

## Types complexes

```python
from typing import Optional

# Liste
grille: list[list[str]] = []

# Optionnel (peut être None)
occupant: Optional[str] = None  # ou : str | None

# Valeur de retour None
def agir(self) -> None:
    pass
```

## Sur une classe

```python
class Entite:
    def __init__(self, energie: int, age: int = 0) -> None:
        self.energie: int = energie
        self.age: int     = age

    def est_vivant(self) -> bool:
        return self.energie > 0

    def vieillir(self) -> None:
        self.age += 1
```

## Forcer les types à l'exécution

Si tu veux vraiment bloquer les mauvais types :

```python
def __init__(self, y: int, x: int) -> None:
    if not isinstance(y, int):
        raise TypeError(f"y doit être un int, reçu {type(y).__name__}")
    if not isinstance(x, int):
        raise TypeError(f"x doit être un int, reçu {type(x).__name__}")
    self.y = y
    self.x = x
```

## Avec les enums

```python
from ecosystem.field import Field

class Cellule:
    def __init__(self, terrain: Field, ressource: int) -> None:
        self.terrain:   Field = terrain
        self.ressource: int   = ressource
```

## Résumé

| Approche | Enforcement | Complexité |
|----------|-------------|------------|
| Type hints seuls | ❌ indicatif | Faible |
| `isinstance` + `raise` | ✅ runtime | Moyenne |
| Pydantic | ✅ automatique | Élevée |

Pour un projet d'apprentissage → **type hints + isinstance sur les cas critiques**.
