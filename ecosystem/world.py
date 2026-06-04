import noise
import random
from ecosystem.field import Field
from ecosystem.cell import Cell
from ecosystem.entity import Prey
from config import LAPIN

class World:
    # Fonction pour créer le monde.
    # Le monde est divisé en 5 biomes :
    #       - Eaux profondes
    #       - Eaux
    #       - Terres
    #       - Herbes
    #       - Forêts
    def __init__(self, y: int, x: int, scale: float, octaves: int, max_prey: int) -> None:
        seed = random.randint(0, 10000)
        self.grid = [
             [self._create_cell(height=height, width=width, scale=scale, octaves=octaves, seed=seed) for width in range(x)]
             for height in range(y)
        ]
        self._add_prey(max_prey)
                
    def _create_cell(self, height: int, width:int, scale: float, octaves: int, seed: int) -> Cell:
        nx = width / scale + seed
        ny = height / scale + seed
        value = noise.pnoise2(ny, nx, octaves=octaves)
        if value < -0.36:
            return Cell(field=Field.EAU_PROFONDE)
        elif value < -0.16:
            return Cell(field=Field.EAU, resource=random.randint(0, 10))
        elif value < -0.06:
            return Cell(field=Field.TERRE)
        elif value < 0.2:
            return Cell(field=Field.HERBE, resource=random.randint(0, 10))
        else:
            return Cell(field=Field.FORET)

                
    def _add_prey(self, max_prey: int):
        prey = 0
        for row in self.grid:
             for cell in row:
                  if (cell.field == Field.HERBE or cell.field == Field.FORET or cell.field == Field.TERRE) and prey < max_prey:
                       if random.random() < 0.05:
                            prey += 1
                            cell.entities = Prey(**LAPIN)