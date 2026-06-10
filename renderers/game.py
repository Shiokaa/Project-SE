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
}

def render(grid: list[Cell], screen: pygame.Surface, pixel_size: int, font: pygame.font.Font):

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            pixel_y = y * pixel_size
            pixel_x = x * pixel_size
            rect = pygame.Rect(pixel_x, pixel_y, pixel_size, pixel_size)

            if cell.entities != None:
                screen.blit(COLORS_ENTITY.get(cell.entities.name), (rect))
            else:
                pygame.draw.rect(screen, COLORS_FIELD[cell.field], rect)
                if cell.resource != None:
                    text_surf = font.render(str(cell.resource)), True, (255,255,255)
                    text_rect = text_surf.get_rect(center=rect.center)
                    screen.blit(text_surf, text_rect)

def run(grid: list[Cell], pixel_size: int):
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1720, 960))

    img_lapin = pygame.image.load('images/lapin.png').convert_alpha()
    img_lapin_small = pygame.transform.scale(img_lapin, (pixel_size, pixel_size))
    COLORS_ENTITY["Lapin"] = img_lapin_small

    font = pygame.font.SysFont("Arial", 14, bold=True)

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

        render(grid, screen, pixel_size, font)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
