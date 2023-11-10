import pygame
import random
import sys

resoultion = {
    "width": 800,
    "height": 800
}


if len(sys.argv) > 1:
    args = sys.argv[1]
    size = int(args)
else:
    size = 20

columns = size
rows = size
grid_w = resoultion["width"] // columns
grid_h = resoultion["height"] // rows
gap = 1

ALIVE_COLOR = (0,0,0)
DEAD_COLOR = (255,255,255)

class Cell:
    def __init__(self, i, j, alive):
        self.x = i
        self.y = j
        self.alive = alive
        self.neighboursCount = 0
        # if self.x == 0 or self.x == rows - 1 or self.y == 0 or self.y == columns - 1:
        #     self.is_border = True
        #     self.alive = False
        # else:
        #     self.is_border = False

    def draw(self, window, color):
        pygame.draw.rect(window, color, (self.x * grid_w, self.y * grid_h, grid_w - gap, grid_w - gap))

    def getNeighboursCount(self):
        self.neighboursCount = 0
        for i in range(-1, 2):
            for j in range(-1, 2):

                self.col = (self.x+i + columns) % columns
                self.row = (self.y+j + rows) % rows 

                self.neighboursCount += int(grid_array[self.col][self.row].alive)
        self.neighboursCount -= int(self.alive)
        return self.neighboursCount

def arrays_setup(rows, cols):
    grid = []
    for i in range(rows):
        arr = []
        for j in range(cols):
            arr.append(Cell(i, j, bool(random.getrandbits(1))))
        grid.append(arr)
    return grid

def draw_grid(array, screen):
    for i in range(rows):
        for j in range(columns):
            box = array[i][j]
            if box.alive:
                color = ALIVE_COLOR
            else:
                color = DEAD_COLOR
            box.draw(screen, color)

def simulate(new_grid, old_grid):
    for i in range(rows):
        for j in range(columns):
            #print(i, j) # DEBUG
            count = old_grid[i][j].getNeighboursCount()
            #print(f"x:{i},y:{j}, n:{count}") # DEBUG
            if old_grid[i][j].alive: # IF IS ALIVE
                if count < 2 or count > 3:
                    new_grid[i][j] = Cell(i, j, False)
                else:
                    new_grid[i][j] = old_grid[i][j]
            else: # IF WAS DEAD
                if count == 3:
                    new_grid[i][j] = Cell(i, j, True)
                else:
                    new_grid[i][j] = old_grid[i][j]
    return new_grid


grid_array = arrays_setup(columns, rows)
new_grid_array = grid_array

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
    new_grid_array = simulate(new_grid_array, grid_array)
    grid_array = new_grid_array
    draw_grid(new_grid_array, screen)

    pygame.display.flip()

    clock.tick(10)

pygame.quit()