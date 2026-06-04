from ecosystem.world import World
from renderers.image import render
from renderers.terminal import display

w = World(50, 100, 10, 1, 200)

render(w.grid)
display(w.grid)