from ecosystem.world import World
from renderers.image import render
from renderers.terminal import display
from renderers.game import run

w = World(50, 100, 10, 1, 200)

run(w.grid, 20)
render(w.grid)
display(w.grid)