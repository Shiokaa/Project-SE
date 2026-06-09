# Généré par IA et adapté par moi-même
from PIL import Image
from ecosystem.field import Field
from ecosystem.cell import Cell
from config import LAPIN

COLORS_FIELD = {
    Field.EAU: (65, 105, 225),              # bleu océan
    Field.EAU_PROFONDE: (10, 25, 71),       # bleu foncé océan profond
    Field.HERBE: (124, 185, 116),           # vert clair herbe
    Field.FORET: (34, 102, 34),             # vert foncé forêt
    Field.TERRE: (87, 50, 42),              # marron foncé terre
}

COLORS_ENTITY = {
    "Lapin": (255, 44, 44)                    # rouge pour lapin
}

CELL = 4  # taille d'un pixel en pixels

def render(grid: list[Cell]):
    h = len(grid)
    w = len(grid[0])
    img = Image.new("RGB", (w * CELL, h * CELL))
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell.entities != None:
                color = COLORS_ENTITY[cell.entities.name]
            else:
                color = COLORS_FIELD[cell.field]
            for dy in range(CELL):
                for dx in range(CELL):
                    img.putpixel((x * CELL + dx, y * CELL + dy), color)
    img.save("world.png")
    print("Image sauvegardée : world.png")
