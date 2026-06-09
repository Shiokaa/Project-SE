import pygame
from ecosystem.cell import Cell
from ecosystem.field import Field


COLORS_FIELD = {
    Field.EAU: (65, 105, 225),              # bleu océan
    Field.EAU_PROFONDE: (10, 25, 71),       # bleu foncé océan profond
    Field.HERBE: (124, 185, 116),           # vert clair herbe
    Field.FORET: (34, 102, 34),             # vert foncé forêt
    Field.TERRE: (87, 50, 42),              # marron foncé terre
}

COLORS_ENTITY = {
    "Lapin": (255, 44, 44)                  # rouge pour lapin
}

def render(grid: list[Cell], screen: pygame.Surface):
    pixel_size = 20
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            pixel_y = y * pixel_size
            pixel_x = x * pixel_size
            rect = pygame.Rect(pixel_x, pixel_y, pixel_size, pixel_size)

            if cell.entities != None:
                pygame.draw.rect(screen, COLORS_ENTITY[cell.entities.name], rect)
            else:
                pygame.draw.rect(screen, COLORS_FIELD[cell.field], rect)

def run(grid: list[Cell]):
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE

        render(grid, screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
