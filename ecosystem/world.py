import noise
import random

# Fonction pour créer le monde.
# Le monde est divisé en 5 biomes :
#       - Eaux profondes
#       - Eaux
#       - Terres
#       - Herbes
#       - Forêts
def world(y, x, scale, octaves):
    world = [[] for _ in range(y)]
    seed = random.randint(0, 10000)
    for height in range(y):
        for width in range(x):
            nx = width / scale + seed
            ny = height / scale + seed
            value = noise.pnoise2(ny, nx, octaves=octaves)
            if value < -0.36:
                world[height].append("ep")
            elif value < -0.16:
                world[height].append("e")
            elif value < -0.06:
                world[height].append("t")
            elif value < 0.14:
                world[height].append("h")
            else:
                world[height].append("f")
    return world
