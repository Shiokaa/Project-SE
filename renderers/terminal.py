from ecosystem.field import Field

COLORS = {
    Field.EAU: "💧",                # bleu océan
    Field.EAU_PROFONDE: "🌊",       # bleu foncé océan profond
    Field.HERBE: "🌿",              # vert clair herbe
    Field.FORET: "🌲",              # vert foncé forêt
    Field.TERRE: "🟫"               # marron foncé terre
}

def display(grid: list[list]):
    for row in grid:
        line = ""
        for cell in row:
            if cell.entity != None and cell.entity.name == "Lapin":
                line += "🟥"
            else:
                line += COLORS[cell.field]
        print(line) 
