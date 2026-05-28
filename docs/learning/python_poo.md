# La POO en Python

## Une classe de base

```python
class Animal:
    def __init__(self, nom, energie):  # constructeur
        self.nom     = nom      # attribut d'instance
        self.energie = energie

    def manger(self, quantite):        # méthode
        self.energie += quantite

    def est_vivant(self) -> bool:
        return self.energie > 0
```

```python
a = Animal("Bob", 10)  # créer une instance
a.manger(5)            # appeler une méthode
print(a.energie)       # 15
```

## L'héritage

Une classe **enfant** hérite de tous les attributs et méthodes du **parent**.

```python
class Proie(Animal):
    def __init__(self, nom, energie, vitesse):
        super().__init__(nom, energie)  # appelle le __init__ du parent
        self.vitesse = vitesse          # attribut propre à Proie

    def fuir(self):
        print(f"{self.nom} fuit !")


class Predateur(Animal):
    def __init__(self, nom, energie, force):
        super().__init__(nom, energie)
        self.force = force

    def chasser(self, proie: Proie):
        self.energie += proie.energie
        proie.energie = 0
```

```python
lapin  = Proie("Lapin", 10, vitesse=3)
renard = Predateur("Renard", 8, force=5)

renard.chasser(lapin)
print(lapin.est_vivant())   # False  (méthode héritée de Animal)
print(renard.energie)       # 18
```

## Surcharger une méthode (override)

L'enfant peut **redéfinir** une méthode du parent.

```python
class Animal:
    def se_deplacer(self):
        print("je me déplace")

class Proie(Animal):
    def se_deplacer(self):      # override
        print("je fuis !")

class Predateur(Animal):
    def se_deplacer(self):      # override
        print("je chasse !")
```

## Méthodes abstraites

Forcer les enfants à implémenter une méthode :

```python
from abc import ABC, abstractmethod

class Entite(ABC):
    def __init__(self, energie, age=0):
        self.energie = energie
        self.age     = age

    @abstractmethod
    def agir(self):  # chaque enfant DOIT implémenter agir()
        pass

class Proie(Entite):
    def agir(self):
        print("je broute")

class Predateur(Entite):
    def agir(self):
        print("je chasse")
```

## Résumé

```
Entite (parent / classe abstraite)
├── energie
├── age
├── agir()  ← abstraite, chaque enfant l'implémente à sa façon
│
├── Proie (enfant)
│   ├── vitesse
│   └── agir() → brouter, fuir
│
└── Predateur (enfant)
    ├── force
    └── agir() → chasser, traquer
```

## À retenir

| Concept | Mot-clé | Usage |
|---------|---------|-------|
| Constructeur | `__init__` | Initialiser les attributs |
| Appeler le parent | `super()` | Dans `__init__` de l'enfant |
| Héritage | `class Enfant(Parent)` | Partager du code |
| Méthode abstraite | `@abstractmethod` | Forcer l'implémentation |
| Instance | `obj = MaClasse()` | Créer un objet |
