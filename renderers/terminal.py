from ecosystem.field import Field

COLORS_FIELD = {
    Field.EAU: "💧",                # bleu océan
    Field.EAU_PROFONDE: "🌊",       # bleu foncé océan profond
    Field.HERBE: "🌿",              # vert clair herbe
    Field.FORET: "🌲",              # vert foncé forêt
    Field.TERRE: "🟫"               # marron foncé terre
}

COLORS_ENTITY = {
    "Lapin": "🟥"                   # rouge pour lapin
}


def display(grid: list[list]):
    for row in grid:
        line = ""
        for cell in row:
            if cell.entities != None:
                line += COLORS_ENTITY[cell.entities.name]
            else:
                line += COLORS_FIELD[cell.field]
        print(line) 
