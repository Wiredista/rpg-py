from ctypes import Structure
import os
import random
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



def chance(percentage):
    return random.randint(0, 100) <= percentage


class Direction(float):
    def __init__(self, dir: float):
        self.angle = float(dir) % 360
    

    def __str__(self):
        return f"{self.angle}°"

    def __int__(self):
        return int(self.angle)
    
    def __float__(self):
        return self.angle

    def __repr__(self):
        return f"Direction({int(self)})"

    def __add__(self, value: float):
        if type(value) == Direction:
            return Direction(self.angle + value.angle)
        else:
            value = float(value) 
            return Direction(self.angle + value)

    def Coordinates(self, x, y, map):
        
        angle = self.angle
        if angle == 270: # North
            return (x, y-1 if y-1 >= 0 else y)
        elif angle == 90: # South
            return (x, y+1 if y+1 <= map.size()[1] else y)
        elif angle == 0: # East
            return (x+1 if x+1 <= map.size()[0] else x, y)
        elif angle == 180: # West
            return (x-1 if x-1 >= 0 else x, y)
        else:
            raise NotImplementedError

class MapCell:
    passable = True
    icon = " "
    def __init__(self, rand=False):
        if rand:
            self.contents = list()
            self.contentsIndex = dict()
            self.icon = random.choice([" ", "~", "+", "^"])
    def __str__(self):
        return self.icon
    
    def geticon(self) -> str:
        for item in self.contents:
            if type(item) == Player:
                return "X"
        else:
            return self.icon
    def enter(self, who):
        self.contents.append(who)
        self.contentsIndex[who] = len(self.contents) - 1 
        return self.passable
    def exit(self, who):
        del self.contents[  self.contentsIndex[who]  ]
        del self.contentsIndex[who]
        return True
class Map:
    def __init__(self, x, y):
        self.grid = [ list(MapCell(True) for _ in range(y)) for _ in range(x) ]
 
    
    def __str__(self):
        string = "╔═" + "═" * self.grid.__len__() * 2 + "╗\n"

        for col in self.grid:
            string += "║ "
            for cell in col:
                string += cell.geticon() + " "
            string += '║\n'
        string += "╚═" + "═" * self.grid.__len__() * 2+ "╝"
        return string
    
    def __getitem__(self, item: tuple):
        x, y = item[0], item[1]
        return self.grid[y][x]

    def size(self) -> tuple:
        return (len(self.grid), len(self.grid[0]))


class Player:
    classe = "Farmer"
    name = "Joe"
    x = 0
    y = 0
    mapa: Map = None
    turf: MapCell = None
    def __init__(self, loc: Map, x=0, y=0):
        self.loc = loc
        self.x = x
        self.y = y
        self.turf = self.loc[self.x, self.y]
        self.turf.enter(self)
    def __str__(self):
        return f"{self.classe} {self.name}"

    def move(self, dir: Direction):
        goto = dir.Coordinates(self.x, self.y, self.loc)
        if goto != (self.x, self.y):
            if self.loc[self.x,self.y].exit(self):
                if self.loc[goto].enter(self):
                    self.x, self.y = goto
                    self.turf = self.loc[(self.x, self.y)]
                    return True
        return False
                

                



north = Direction(270)
south = Direction(90)
east  = Direction(0)
west  = Direction(180)