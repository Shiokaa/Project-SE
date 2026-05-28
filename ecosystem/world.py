import noise
import random
from ecosystem.field import Field
from ecosystem.cell import Cell
from ecosystem.entity import Prey

class World:
    # Fonction pour créer le monde.
    # Le monde est divisé en 5 biomes :
    #       - Eaux profondes
    #       - Eaux
    #       - Terres
    #       - Herbes
    #       - Forêts
    def __init__(self, y: int, x: int, scale: float, octaves: int) -> None:
        seed = random.randint(0, 10000)
        self.grid = [
             [self._create_cell(height=height, width=width, scale=scale, octaves=octaves, seed=seed) for width in range(x)]
             for height in range(y)
        ]
                
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