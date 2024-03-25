
import pygame 
import math
import random
import sys
import pygame.font



pygame.init()
width, height = 400, 400
size = 20
g_width, g_height = 20, 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Temuujin lab2")
a_color = (120, 201, 20)
font = pygame.font.SysFont(None, 36)  


class Home:
    def __init__(self):
        self.value = 0

class Agent:
    def __init__(self, x, y, item):
        self.x = x
        self.y = y
        self.item = item

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def findNear(self, grid, check):
        min_dis = float("inf")
        n_x, n_y = None, None
        for y in range(g_height):
            for x in range(g_width):
                if grid[y][x] == 1:
                    check = True
                    dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
                    if dis < min_dis:
                        min_dis = dis
                        n_x, n_y = x, y
        return n_x, n_y, check

    def go_shape(self, dirt_x, dirt_y):
        hi=True
        while hi:
            if self.x < dirt_x:
                self.move_right()
            elif self.x > dirt_x:
                self.move_left()
            elif self.y < dirt_y:
                self.move_down()
            elif self.y > dirt_y:
                self.move_up()
            if self.x == dirt_x and self.y==dirt_y:
                hi=False
            for y in range(g_height):
                for x in range(g_width):
                    if grid[y][x] == 0:
                        pygame.draw.rect(screen, ((255,255,255)), (x * size, y * size, size, size))
                    else: 
                        pygame.draw.rect(screen, ((123,123,123)), (x * size, y * size, size, size))
            pygame.draw.rect(screen,((255,0,0)),(0,0,size,size))
            agent.draw()
            pygame.display.flip()
            pygame.time.wait(10)
        

    def get(self, grid):
        self.item = True
        grid[self.y][self.x] = 0

    def home(self, home_obj):
        if self.x == 0 and self.y == 0:
            home_obj.value += 1
            self.item=False

    def draw(self):
        pygame.draw.rect(screen, a_color, (self.x * size, self.y * size, size, size))

grid = [[random.randint(0, 1) for _ in range(g_width)] for _ in range(g_height)]


run = True
home = Home()  
agent = Agent(random.randint(0, g_width - 1), random.randint(0, g_height - 1), False)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    check = False
    shape_x, shape_y,check = agent.findNear(grid,check)
    if check==False:
        run=False
        break
    agent.go_shape(shape_x,shape_y)
    agent.get(grid)
    agent.go_shape(0,0)
    agent.home(home)
    for y in range(g_height):
        for x in range(g_width):
            if grid[y][x] == 0:
                pygame.draw.rect(screen, ((255,255,255)), (x * size, y * size, size, size))
            else: 
                pygame.draw.rect(screen, ((123,123,123)), (x * size, y * size, size, size))
    pygame.draw.rect(screen,((255,0,0)),(0,0,size,size))
    agent.draw()
    
    pygame.display.flip()
    pygame.time.wait(10)
text = font.render("Items collected: {}".format(home.value), True, (255, 3, 3))
screen.blit(text, (10, 10))
pygame.display.flip()

pygame.time.wait(2500)
pygame.quit()
sys.exit()