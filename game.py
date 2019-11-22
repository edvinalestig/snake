from snake import Snake, multiply, add, invert
import pygame, random, math
import settings

class Board():
    
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = settings.boardSize
        self.tileSize = settings.tileSize
        self.food = ()
        self.snake = Snake()
        self.spawnFood()


    def update(self):
        if not self.snake.dead:
            self.snake.move()
        if self.snake.headPos == self.food:
            self.eat()

        self.draw()

        # print(self.info())


    def draw(self):
        colour = (255,165,0) if self.snake.dead else (255,255,255)
        for p in self.snake.positions:
            r = pygame.Rect(add(multiply(p, self.tileSize), 
                multiply(self.tileSize, (0.1,0.1))), 
                multiply(self.tileSize, (0.8,0.8)))
            pygame.draw.rect(self.screen, colour, r)
        
        r = pygame.Rect(add(multiply(self.food, self.tileSize), 
            multiply(self.tileSize, (0.1,0.1))), 
            multiply(self.tileSize, (0.8,0.8)))
        pygame.draw.rect(self.screen, (150, 0, 0), r)


    def spawnFood(self):
        bx, by = settings.boardSize
        x = random.randint(0,bx-1)
        y = random.randint(0,by-1)
        self.food = (x, y)


    def eat(self):
        self.snake.grow()
        self.spawnFood()


    def info(self):
        foodx, foody = add(invert(self.snake.headPos), self.food)
        a = math.atan2(foody, foodx)

        # 0 - Food
        # 0.33 - Empty
        # 0.67 - Itself
        # 1 - Wall
        x, y = self.snake.headPos
        vision = []
        for i in range(-2,3):
            for j in range(-2,3):
                d = (i+x, j+y)
                for p in self.snake.positions:
                    if p == d:
                        vision.append(0.67)
                        break
                else:
                    if i+x < 0 or i+x >= self.width or j+y < 0 or j+y >= self.height:
                        vision.append(1)
                    elif d == self.food:
                        vision.append(0)
                    else:
                        vision.append(0.33)

        return {
            "food": a,
            "vision": vision, # 5x5 area
            "direction": self.snake.direction[0]
        }
        # 1 + 25 + 2 = 28 nodes required