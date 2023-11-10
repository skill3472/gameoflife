import pygame
import random

resoultion = {
    "width": 800,
    "height": 800
}

rect_size = 40;
columns = 20;
rows = 20;
grid_w = resoultion["width"] // columns
grid_h = resoultion["height"] // rows
gap = 1

ALIVE_COLOR = (0,0,0)
DEAD_COLOR = (255,255,255)

class Cell:
    def __init__(self, i, j, alive):
        self.x = i
        self.y = j
        self.rect_size = 40
        self.alive = alive
        self.neighbours = []

    def draw(self, window, color):
        pygame.draw.rect(window, color, (self.x * grid_w, self.y * grid_h, grid_w - gap, grid_w - gap))

    def getNeighbours(self):
        pass

def arrays_setup(rows, cols):
    grid = []
    for i in range(cols):
        arr = []
        for j in range(rows):
            arr.append(Cell(i, j, bool(random.getrandbits(1))))
        grid.append(arr)
    return grid

def draw_grid(array, screen):
    for i in range(columns):
        for j in range(rows):
            box = array[i][j]
            if box.alive:
                color = ALIVE_COLOR
            else:
                color = DEAD_COLOR
            box.draw(screen, color)

grid_array = arrays_setup(20, 20)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((resoultion["width"], resoultion["height"]))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray")

    draw_grid(grid_array, screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()