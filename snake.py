import settings
from math import floor

NORTH = (0,-1)
EAST = (1,0)
SOUTH = (0,1)
WEST = (-1,0)

def add(v1, v2):
    return (v1[0]+v2[0], v1[1]+v2[1])

def multiply(v1, v2):
    return (v1[0]*v2[0], v1[1]*v2[1])

def invert(v1):
    return (-v1[0], -v1[1])

def combine(pos, d):
    t = []
    for i in range(len(pos)):
        t.append(add(pos[i], d[i]))
    return t

class Snake():
    def __init__(self):
        middleX = floor(settings.boardSize[0]/2)
        middleY = floor(settings.boardSize[1]/2)
        self.length = 3
        self.headPos = (middleX,middleY)
        self.positions = [self.headPos, (middleX-1,middleY), (middleX-2,middleY)]
        self.lastPos = (middleX-3,middleY)
        self.direction = [EAST,EAST,EAST,EAST]
        self.turned = False
        self.dead = False

    def move(self):
        if self.hit(add(self.headPos,self.direction[0])):
            self.dead = True
            return

        self.lastPos = self.positions[-1]
        self.positions = combine(self.positions, self.direction)
        self.direction = [self.direction[0]] + self.direction[:-1]
        self.headPos = self.positions[0]
        self.turned = False

    def turn(self, direction):
        if self.direction[0] != invert(direction) and not self.turned:
            self.direction = [direction] + self.direction[1:]
            self.turned = True

    def grow(self):
        self.length += 1
        self.positions.append(self.lastPos)
        self.direction.append(self.direction[-1])

    def hit(self, head):
        # Wall
        x, y = head
        bx, by = settings.boardSize
        if x < 0 or x >= bx or y < 0 or y >= by:
            return True
        
        # Itself
        for p in self.positions:
            if p == head:
                return True

        return False
