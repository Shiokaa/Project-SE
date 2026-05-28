# L'append en Python

## Tableaux à une dimension

```python
ma_liste = [1, 2, 3]
ma_liste.append(4)
print(ma_liste)  # [1, 2, 3, 4]
```

**Points clés :**
- `.append()` modifie la liste **en place** (ne retourne rien)
- Ajoute l'élément à la **fin** de la liste
- Fonctionne avec n'importe quel type d'objet

```python
fruits = ["pomme", "banane"]
fruits.append("orange")  # Ajoute une chaîne
fruits.append([1, 2])    # Ajoute une liste comme élément unique

nombres = []
nombres.append(10)
nombres.append(20)
```

## Tableaux à deux dimensions

### Ajouter une nouvelle ligne (liste)

```python
tableau = [[1, 2, 3], [4, 5, 6]]
tableau.append([7, 8, 9])
print(tableau)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Ajouter un élément à une ligne spécifique

```python
tableau = [[1, 2, 3], [4, 5, 6]]
tableau[0].append(4)  # Ajoute à la première ligne
print(tableau)
# [[1, 2, 3, 4], [4, 5, 6]]
```

### Initialiser et remplir un tableau 2D

```python
tableau = []
tableau.append([1, 2, 3])
tableau.append([4, 5, 6])
print(tableau)
# [[1, 2, 3], [4, 5, 6]]
```

### Cas courant : ajouter une ligne avec des valeurs spécifiques

```python
tableau = []
for i in range(3):
    tableau.append([0] * 3)  # Ajoute une ligne de 3 zéros
print(tableau)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

## Ajouter plusieurs éléments à la fois

Utilisez `.extend()` pour ajouter plusieurs éléments :

```python
ma_liste = [1, 2, 3]
ma_liste.extend([4, 5, 6])
print(ma_liste)  # [1, 2, 3, 4, 5, 6]
```
