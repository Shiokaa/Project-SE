# Généré par IA
from PIL import Image

COLORS = {
    "e": (65, 105, 225),    # bleu océan
    "ep": (10, 25, 71),     # bleu foncé océan profond
    "h": (124, 185, 116),   # vert clair herbe
    "f": (34, 102, 34),     # vert foncé forêt
    "t": (87, 50, 42)       # marron foncé terre
}

CELL = 4  # taille d'un pixel en pixels

def render(grid):
    h = len(grid)
    w = len(grid[0])
    img = Image.new("RGB", (w * CELL, h * CELL))
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            color = COLORS[cell]
            for dy in range(CELL):
                for dx in range(CELL):
                    img.putpixel((x * CELL + dx, y * CELL + dy), color)
    img.save("world.png")
    print("Image sauvegardée : world.png")
