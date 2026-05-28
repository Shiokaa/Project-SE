import noise
import random
from ecosystem.field import Field

class World:
    # Fonction pour créer le monde.
    # Le monde est divisé en 5 biomes :
    #       - Eaux profondes
    #       - Eaux
    #       - Terres
    #       - Herbes
    #       - Forêts
    def __init__(self, y: int, x: int, scale: float, octaves: int) -> None:
        world = [[] for _ in range(y)]
        seed = random.randint(0, 10000)
        for height in range(y):
            for width in range(x):
                nx = width / scale + seed
                ny = height / scale + seed
                value = noise.pnoise2(ny, nx, octaves=octaves)
                if value < -0.36:
                    world[height].append(Field.EAU_PROFONDE)
                elif value < -0.16:
                    world[height].append(Field.EAU)
                elif value < -0.06:
                    world[height].append(Field.TERRE)
                elif value < 0.14:
                    world[height].append(Field.HERBE)
                else:
                    world[height].append(Field.FORET)
        self.grid = world