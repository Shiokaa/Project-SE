# Perlin Noise - Comment ça fonctionne

## Concept de base

Le Perlin noise est une fonction qui génère des valeurs **pseudo-aléatoires continues**. Contrairement au bruit complètement aléatoire, le Perlin noise produit des valeurs qui changent **progressivement** et **naturellement**, idéal pour créer des terrains, des nuages, etc.

## Les étapes du Perlin Noise

### 1. Gradient Noise (Bruit de Gradient)

Le Perlin noise fonctionne en divisant l'espace en **grille de carrés** avec des **vecteurs de gradient aléatoires** aux coins.

```
Exemple d'une grille 2D :

  (0,0) -------- (1,0)
   |  \          |
   |    \    P   |     P = Point à évaluer
   |      \      |
  (0,1) -------- (1,1)
```

Chaque coin a un **vecteur gradient** aléatoire (une direction).

### 2. Distance et Produit scalaire

Pour trouver la valeur au point P, on :
1. Calcule la **distance** entre P et chaque coin
2. Calcule le **produit scalaire** entre le vecteur du coin et le vecteur distance
3. Combine les 4 résultats avec une **interpolation lisse**

```
Pseudo-code :
- Pour chaque coin de la grille :
    - Vecteur distance = P - coin
    - Produit scalaire = gradient[coin] · distance
- Interpoler ces 4 valeurs de façon lisse
```

### 3. Interpolation lisse (Smoothstep)

Au lieu d'une interpolation linéaire qui serait saccadée, on utilise une courbe lisse :

```python
def smoothstep(t):
    # t va de 0 à 1
    return t * t * (3 - 2 * t)  # Courbe en S
```

Cela crée des transitions **fluides** entre les valeurs.

## Exemple simple en pseudo-code

```python
def perlin_2d(x, y):
    # 1. Trouver la grille du point
    grid_x = floor(x)
    grid_y = floor(y)
    
    # 2. Position relative dans la cellule (0 à 1)
    local_x = x - grid_x
    local_y = y - grid_y
    
    # 3. Récupérer les 4 gradients des coins
    g00 = gradient(grid_x,     grid_y)
    g10 = gradient(grid_x + 1, grid_y)
    g01 = gradient(grid_x,     grid_y + 1)
    g11 = gradient(grid_x + 1, grid_y + 1)
    
    # 4. Calculer les produits scalaires
    d00 = (local_x - 0) * g00_x + (local_y - 0) * g00_y
    d10 = (local_x - 1) * g10_x + (local_y - 0) * g10_y
    d01 = (local_x - 0) * g01_x + (local_y - 1) * g01_y
    d11 = (local_x - 1) * g11_x + (local_y - 1) * g11_y
    
    # 5. Interpoler les valeurs
    u = smoothstep(local_x)
    v = smoothstep(local_y)
    
    # Interpoler horizontalement
    n0 = mix(d00, d10, u)
    n1 = mix(d01, d11, u)
    
    # Interpoler verticalement
    result = mix(n0, n1, v)
    
    return result
```

## Octaves et Fractional Brownian Motion (FBM)

Pour obtenir plus de **détails** et une apparence plus naturelle, on combine plusieurs niveaux de Perlin noise :

```python
def fbm(x, y, octaves=4):
    result = 0
    amplitude = 1.0
    frequency = 1.0
    max_value = 0
    
    for i in range(octaves):
        # Ajouter une couche de bruit
        result += amplitude * perlin(x * frequency, y * frequency)
        
        # Augmenter la fréquence (plus de détails)
        frequency *= 2.0  # lacunarity
        
        # Diminuer l'amplitude (moins d'influence)
        amplitude *= 0.5  # persistence
        
        max_value += amplitude
    
    return result / max_value
```

**Explication :**
- **1er octave** : grandes formes (low frequency)
- **2e octave** : détails moyens (fréquence × 2)
- **3e octave** : petits détails (fréquence × 4)
- **4e octave** : texture fine (fréquence × 8)

## Paramètres clés

### Scale (Échelle)

C'est le **zoom** sur le bruit. Contrôle la **taille des formes**.

```python
# Scale PETIT (ex: 10)
value = noise.pnoise2(x / 10, y / 10)
# → Bruit DÉTAILLÉ, formes petites, changements rapides
# Résultat : 🌊🌿🪨🌊🌿🪨🌊  (alternances rapides)

# Scale MOYEN (ex: 50)
value = noise.pnoise2(x / 50, y / 50)
# → Bruit ÉQUILIBRÉ, formes moyennes
# Résultat : 🌊🌊🌊🌿🌿🌿🪨🪨🪨  (zones cohérentes)

# Scale GRAND (ex: 200)
value = noise.pnoise2(x / 200, y / 200)
# → Bruit LISSÉ, grandes formes, changements lents
# Résultat : 🌊🌊🌊🌊🌿🌿🌿🌿  (grandes zones unies)
```

**Résumé :** Scale = taille des "continents"

### Octaves (Couches)

C'est le **nombre de couches de bruit** qu'on superpose. Chaque couche ajoute des **détails**.

```python
# 1 octave
value = noise.pnoise2(x/50, y/50, octaves=1)
# → Bruit LISSÉ et simple
# Résultat : 🌊🌊🌊🌊🌊🌿🌿🌿🌿  (peu de détails)

# 4 octaves
value = noise.pnoise2(x/50, y/50, octaves=4)
# → 1er niveau : grandes formes
# + 2e niveau : détails moyens (2× plus rapide)
# + 3e niveau : petits détails (4× plus rapide)
# + 4e niveau : texture fine (8× plus rapide)
# Résultat : NATUREL, plein de variation
# Visualisation : 🌊🌊🌿💧🪨🌿🌊🪨🌿🌊  (beaucoup de détails)

# 8 octaves
value = noise.pnoise2(x/50, y/50, octaves=8)
# → ENCORE PLUS de détails, très complexe
```

**Résumé :** Octaves = nombre de couches de détails

### Persistence (Persistance)

C'est l'**influence des petits détails**. Contrôle combien chaque octave affecte le résultat final.

```python
# Persistence BAS (0.3)
# Les petites couches ont peu d'influence
# Résultat : lissé, détails discrets
# Visualisation : 🌊🌊🌊🌿🌿🌿🌿🌿  (lisses transitions)

# Persistence MOYEN (0.5)
# Équilibre entre grandes formes et petits détails
# Résultat : naturel et varié
# Visualisation : 🌊🌿💧🌿🌿🪨🌿🌊  (bon mélange)

# Persistence HAUT (0.8)
# Les petites couches ont BEAUCOUP d'influence
# Résultat : très chaotique et détaillé
# Visualisation : 🌊🪨💧🌿⛰️💧🌊🪨🌿  (très fragmenté)
```

**Résumé :** Persistence = poids des détails fins

### Lacunarity (Lacunarité)

C'est le **multiplicateur de fréquence** entre les octaves. Contrôle la **vitesse** des détails.

```python
# Lacunarity = 2.0 (standard)
# Chaque octave est 2× plus rapide que la précédente
# 1er : grande (fréquence × 1)
# 2e : 2× plus rapide (fréquence × 2)
# 3e : 4× plus rapide (fréquence × 4)
# 4e : 8× plus rapide (fréquence × 8)
# Résultat : détails bien espacés
# Visualisation : 🌊🌊🌿🌿🌿🪨  (hiérarchie claire)

# Lacunarity = 3.0
# Chaque octave est 3× plus rapide
# Résultat : détails très fins, serrés
# Visualisation : 🌊🌿💧🌿🪨💧🌊🪨  (très compact)

# Lacunarity = 1.5
# Chaque octave est 1.5× plus rapide
# Résultat : détails moins extrêmes
# Visualisation : 🌊🌊🌿🌿🌿🌿🌿🌿  (transitions graduelles)
```

**Résumé :** Lacunarity = vitesse des changements entre octaves

## Tableau récapitulatif

| Paramètre | Petit | Moyen | Grand | Effet |
|-----------|-------|-------|-------|-------|
| **Scale** | 10 | 50 | 200 | Détail ← → Lissé |
| **Octaves** | 1 | 4 | 8 | Simple ← → Complexe |
| **Persistence** | 0.3 | 0.5 | 0.8 | Lissé ← → Chaotique |
| **Lacunarity** | 1.5 | 2.0 | 3.0 | Graduel ← → Rapide |

## Exemples d'ajustement

```python
# Terrain montagneux avec grandes chaînes
world(50, 100, scale=100, octaves=6, persistence=0.6, lacunarity=2.0)

# Archipel fragmenté
world(50, 100, scale=20, octaves=8, persistence=0.8, lacunarity=2.5)

# Terrain lisse et fluide
world(50, 100, scale=150, octaves=3, persistence=0.3, lacunarity=2.0)
```

## Visualisation pratique

```python
import noise

# Bas de gamme : grandes formes fluides
for y in range(10):
    row = ""
    for x in range(20):
        value = noise.pnoise2(x / 100, y / 100)  # Scale très grand
        row += "█" if value > 0 else " "
    print(row)

print("\n")

# Haute fréquence : beaucoup de détails
for y in range(10):
    row = ""
    for x in range(20):
        value = noise.pnoise2(x / 5, y / 5)  # Scale petit
        row += "█" if value > 0 else " "
    print(row)
```

## Pièges courants

### Le problème de l'origine (0,0)

`pnoise2(0, 0) = 0` par définition. Échantillonner près de l'origine donne des valeurs très petites (entre -0.03 et 0.03), ce qui rend les seuils difficiles à calibrer.

```python
# ❌ Problème : valeurs minuscules près de l'origine
value = noise.pnoise2(height / 300, width / 300)
# → toutes les valeurs proches de 0, difficile à distinguer

# ✅ Solution : se déplacer loin de l'origine
offset = random.randint(0, 10000)
value = noise.pnoise2(height / scale + offset, width / scale + offset)
# → valeurs bien réparties entre -0.5 et 0.5
```

### La relation taille du monde / scale

Avec un monde de 50×100 et `scale=300`, les coordonnées explorées sont `[0, 0.17]` — une infime portion du bruit où tout est presque plat.

```
Monde 50×100, scale=300 → coordonnées [0, 0.17] → quasi-plat ❌
Monde 50×100, scale=50  → coordonnées [0, 1.0]  → variation complète ✅
```

**Règle :** `scale` doit être du même ordre de grandeur que la taille du monde pour avoir une bonne couverture.

### octaves=1 pour des biomes propres

Avec plusieurs octaves, les hautes fréquences créent des fragments autour des seuils (eau perdue au milieu de la forêt). Pour des zones nettes type Minecraft, `octaves=1` est la meilleure approche.

```python
# ❌ octaves=4 : fragments parasites autour des seuils
value = noise.pnoise2(ny, nx, octaves=4)

# ✅ octaves=1 : zones parfaitement propres
value = noise.pnoise2(ny, nx, octaves=1)
```

### Seed : addition vs multiplication

```python
# ❌ Multiplication : change le scale effectif (biomes plus grands/petits selon seed)
nx = width / scale * seed

# ✅ Addition : déplace la position sur la carte (biomes de taille constante)
nx = width / scale + seed * 100
```

## Cas d'usage

- **Terrain** : utiliser la valeur pour la hauteur (eau/terre/montagne)
- **Texture** : utiliser pour la couleur
- **Génération procédurale** : cavernes, îles, nuages
- **Animation** : mouvement fluide et naturel

## Ressources

- [Perlin noise visually explained](https://rtouti.github.io/graphics/perlin-noise-2d)
- Libraires : `noise`, `perlin-numpy`, `opensimplex`
