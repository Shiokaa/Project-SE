# Les imports en Python

## Importer un fichier simple

```
projet/
├── main.py
└── utils.py
```

```python
# Dans main.py
import utils              # importe tout le module
utils.ma_fonction()

from utils import ma_fonction  # importe une fonction spécifique
ma_fonction()

from utils import *        # importe tout (déconseillé)
```

## Importer depuis un dossier (package)

Un dossier doit contenir un fichier `__init__.py` pour être reconnu comme un package Python.

```
projet/
├── main.py
├── ecosystem/
│   ├── __init__.py   ← obligatoire !
│   └── world.py
└── renderers/
    ├── __init__.py   ← obligatoire !
    └── image.py
```

```python
# Dans main.py
from ecosystem.world import world       # importe la fonction world
from renderers.image import render      # importe la fonction render
```

## Le fichier `__init__.py`

C'est un fichier vide (ou avec du code) qui dit à Python : "ce dossier est un package".

- Sans `__init__.py` → `import ecosystem` échoue
- Avec `__init__.py` vide → le package est importable
- Avec du code dedans → ce code s'exécute à l'import

```python
# __init__.py peut aussi réexporter des fonctions
from ecosystem.world import world   # permet d'écrire : from ecosystem import world
```

## Les différentes syntaxes d'import

```python
# 1. Import du module entier
import ecosystem.world
ecosystem.world.world(50, 100, 50, 1)  # long à écrire

# 2. Import direct de la fonction (recommandé)
from ecosystem.world import world
world(50, 100, 50, 1)  # plus lisible

# 3. Import avec alias
from ecosystem.world import world as create_world
create_world(50, 100, 50, 1)

# 4. Import multiple
from ecosystem.world import world, autre_fonction
```

## Erreurs courantes

### ModuleNotFoundError

```python
import ecosystem  # ❌ ecosystem est un dossier sans __init__.py
# → ModuleNotFoundError: No module named 'ecosystem'

# ✅ Solution : créer ecosystem/__init__.py
from ecosystem.world import world
```

### ImportError

```python
from ecosystem.world import monde  # ❌ la fonction s'appelle "world" pas "monde"
# → ImportError: cannot import name 'monde'

# ✅ Solution : vérifier le nom exact dans le fichier source
from ecosystem.world import world
```

### Import circulaire

```python
# ❌ a.py importe b.py, et b.py importe a.py → erreur
# Solution : restructurer le code pour éviter la dépendance circulaire
```

## Structure recommandée pour un projet

```
projet/
├── main.py           ← point d'entrée
├── ecosystem/
│   ├── __init__.py
│   └── world.py
├── renderers/
│   ├── __init__.py
│   └── image.py
└── docs/
```

```python
# main.py
from ecosystem.world import world
from renderers.image import render

carte = world(100, 200, 150, 1)
render(carte)
```
