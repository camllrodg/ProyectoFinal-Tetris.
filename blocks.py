from block import Block
from position import Position

#Clases de cada pieza, con herencia de la clase pieza.
class block_1(Block): 
    def __init__(self):
        super().__init__(id=1)
        self.cells={
            0: [Position(0,0), Position(0,1), Position(0,2)],
            1: [Position(0,1),Position(1,1),Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(1,2)],
        }
        self.move(0,3)

class block_2(Block):
    def __init__(self):
        super().__init__(id=2)
        self.cells={
            0: [Position(0,0), Position(1,0), Position(2,0)],
            1: [Position(1,0), Position(1,1), Position(1,2)],
            2: [Position(0,1), Position(1,1), Position(2,1)],
        }
        self.move(0,3)

class block_3(Block):
    def __init__(self):
        super().__init__(id=3)
        self.cells={     
            0: [Position(0,0), Position(1,0), Position(2,0), Position (2,1)],
            1: [Position(1,0), Position(1,1), Position(1,2), Position(2,0)],
            2: [Position(0,0), Position(0,1), Position(1,1), Position(2,1)],
            3: [Position(1,0), Position(1,1), Position(1,2), Position(0,2)],
        }
        self.move(0,3)

class block_4(Block): 
    def __init__(self):
        super().__init__(id=4)
        self.cells={    
            0: [Position(2,0), Position(2,1), Position(1,1), Position (0,1)],
            1: [Position(1,0), Position(2,0), Position(2,1), Position(2,2)],
            2: [Position(0,0), Position(1,0), Position(2,0), Position(0,1)],
            3: [Position(1,0), Position(1,1), Position(1,2), Position(2,2)],
        }
        self.move(0,3)

class block_5(Block):
    def __init__(self):
        super().__init__(id=5)
        self.cells={     
            0: [Position(0,0), Position(0,1), Position(1,1), Position (1,2)],
            1: [Position(0,2), Position(1,2), Position(1,1), Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(2,1), Position(2,2)],
            3: [Position(0,1), Position(1,1), Position(1,0), Position(2,0)],
        }
        self.move(0,3)

class block_6(Block):
    def __init__(self):
        super().__init__(id=6)
        self.cells={     
            0: [Position(0,0), Position(0,1), Position(1,1), Position (2,1)],
            1: [Position(0,2), Position(1,0), Position(1,1), Position(1,2)],
            2: [Position(0,1), Position(1,1), Position(2,1), Position(2,2)],
            3: [Position(1,0), Position(1,1), Position(1,2), Position(2,0)],
        }
        self.move(0,3)

class block_7(Block):
    def __init__(self):
        super().__init__(id=7)
        self.cells={    
            0: [Position(0,0), Position(0,1), Position(1,0), Position (1,1)],
        }
        self.move(0,4)

class block_8(Block):
    def __init__(self):
        super().__init__(id = 8)
        self.cells={
            0: [Position(0,1), Position(1,1), Position(2,0), Position (2,1), Position(2,2)],
            1: [Position(0,0), Position(1,0), Position(2,0), Position(1,1), Position(1,2)],
            2: [Position(0,0), Position(0,1), Position(0,2), Position(1,1), Position(2,1)],
            3: [Position(1,0), Position(1,1), Position(0,2), Position(1,2), Position(2,2)],
        }
        self.move(0,3)

class block_9(Block):
    def __init__(self):
        super().__init__(id=9)
        self.cells={    
            0: [Position(0,0), Position(0,1), Position(0,2), Position (1,1), Position(2,1)],
            1: [Position(1,0), Position(1,1), Position(0,2), Position(1,2), Position(2,2)],
            2: [Position(0,1), Position(1,1), Position(2,0), Position (2,1), Position(2,2)],
            3: [Position(0,0), Position(1,0), Position(2,0), Position(1,1), Position(1,2)],
        }
        self.move(0,3)