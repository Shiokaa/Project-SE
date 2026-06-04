# L'itération en Python

## `range` — générer une séquence de nombres

```python
range(stop)                # 0 → stop-1
range(start, stop)         # start → stop-1
range(start, stop, step)   # avec un pas
```

Exemples :

```python
for i in range(5):         # 0 1 2 3 4
for i in range(2, 8, 2):   # 2 4 6
for i in range(5, 0, -1):  # 5 4 3 2 1 (compte à rebours)
```

> `range` ne crée pas de liste en mémoire — il génère les valeurs à la demande.

---

## `enumerate` — index + valeur en même temps

Évite de faire `range(len(lst))` pour avoir l'index.

```python
fruits = ["pomme", "poire", "cerise"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 pomme
# 1 poire
# 2 cerise

for i, fruit in enumerate(fruits, start=1):  # commence à 1
    print(i, fruit)
```

---

## `zip` — itérer plusieurs séquences en parallèle

```python
noms   = ["Alice", "Bob"]
scores = [10, 20]

for nom, score in zip(noms, scores):
    print(nom, score)
# Alice 10
# Bob 20
```

> S'arrête à la séquence la plus courte.  
> Pour continuer jusqu'à la plus longue : `itertools.zip_longest`.

---

## `map` — appliquer une fonction à chaque élément

```python
list(map(str, [1, 2, 3]))        # ['1', '2', '3']
list(map(lambda x: x * 2, [1, 2, 3]))  # [2, 4, 6]
```

---

## `filter` — garder les éléments qui passent un test

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))  # [2, 4]
```

---

## `itertools` — outils avancés

```python
from itertools import product, combinations, permutations, chain, zip_longest
```

| Fonction | Description | Exemple |
|---|---|---|
| `product(a, b)` | Produit cartésien | `(1,3)(1,4)(2,3)(2,4)` |
| `combinations(lst, n)` | Combinaisons sans répétition | `(1,2)(1,3)(2,3)` |
| `permutations(lst, n)` | Permutations | `(1,2)(2,1)(1,3)…` |
| `chain(a, b)` | Concatène des itérables | `1 2 3 4` |
| `zip_longest(a, b)` | `zip` jusqu'au plus long | remplit avec `None` |

---

## Compréhensions — syntaxe concise

```python
# Liste
[x**2 for x in range(5)]                      # [0, 1, 4, 9, 16]

# Liste avec filtre
[x for x in range(10) if x % 2 == 0]          # [0, 2, 4, 6, 8]

# Imbriqué (nested)
[(i, j) for i in range(3) for j in range(3)]

# Dictionnaire
{k: v for k, v in zip(["a", "b"], [1, 2])}    # {'a': 1, 'b': 2}

# Set
{x % 3 for x in range(9)}                     # {0, 1, 2}
```

---

## Résumé

| Outil | Cas d'usage |
|---|---|
| `range` | Boucle numérique simple |
| `enumerate` | Index + valeur sur une liste |
| `zip` | Parcourir plusieurs listes ensemble |
| `map` | Transformer chaque élément |
| `filter` | Filtrer des éléments |
| `itertools` | Combinatoire, chaînage |
| Compréhension | Créer une liste/dict/set en une ligne |
