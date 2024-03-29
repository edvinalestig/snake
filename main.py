import pygame, sys, time
from game import Board
from snake import NORTH, EAST, SOUTH, WEST
import settings

pygame.init()
bx, by = settings.boardSize
tx, ty = settings.tileSize
screen = pygame.display.set_mode((bx*tx,by*ty))
game = Board(screen)
clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == 273:
                game.snake.turn(NORTH)
            elif e.key == 274: 
                game.snake.turn(SOUTH)
            elif e.key == 275:
                game.snake.turn(EAST)
            elif e.key == 276:
                game.snake.turn(WEST)

    screen.fill((0,0,0))
    game.update()
    pygame.display.flip()
    clock.tick(5)