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
        self.length = 3
        self.headPos = (25,25)
        self.positions = [(25,25), (24,25), (23,25)]
        self.lastPos = (22,25)
        self.pos = 5
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
        if x < 0 or x >= 50 or y < 0 or y >= 50:
            return True
        
        # Itself
        for p in self.positions:
            if p == head:
                return True

        return False
