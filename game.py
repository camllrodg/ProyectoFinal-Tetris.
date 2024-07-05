from grid import Grid
from blocks import *
from block import Block
import random

#Cabeza del juego
class Game:
    def __init__(self):
        self.grid=Grid()
        self.blocks=[block_1(),block_2(),block_3(),block_4(),block_5(),block_6(),block_7(),block_8(),block_9()]
        self.current_block=self.get_random_block()
        self.next_block=self.get_random_block()
        self.game_over=False
        self.score=0
        #self.row=row
        #elf.column=column
    
    #Puntaje
    def update_score(self,lines_clear,move_down_points):
        if lines_clear==1:
            self.score+=100
        elif lines_clear==2:
            self.score+=300
        elif lines_clear==3:
            self.score+=500
        self.score+=move_down_points

    #Metodo para tomar una pieza random
    def get_random_block(self):
        if len(self.blocks)==0: #Si ya se mostraron todas las piezas
            self.blocks=[block_1(),block_2(),block_3(),block_4(),block_5(),block_6(),block_7(),block_8(),block_9()]
        block=random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    #Mover a la izquierda
    def move_left(self):
        self.current_block.move(0,-1)
        if self.block_inside()==False or self.block_fits()==False:
            self.current_block.move(0,1)

    #Mover a la derecha
    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside()==False or self.block_fits()==False:
            self.current_block.move(0,-1)
    
    #Mover hacia abajo
    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside()==False or self.block_fits()==False:
            self.current_block.move(-1,0)
            self.lock()
    
    #Quitar la opcion de mover la pieza, cuando este en el tope inferior de la malla
    def lock(self):
        tiles=self.current_block.get_cells_position()
        for position in tiles:
            self.grid.grid[position.row][position.column]=self.current_block.id
        self.current_block=self.next_block
        self.next_block=self.get_random_block()
        rows_clear=self.grid.delete_full_row()
        self.update_score(rows_clear,0)
        if self.block_fits()==False:
            self.game_over=True
    
    #Restablecer juego
    def reset(self):
        self.grid.reset()
        self.blocks=[block_1(),block_2(),block_3(),block_4(),block_5(),block_6(),block_7(),block_8(),block_9()]
        self.current_block=self.get_random_block()
        self.next_block=self.get_random_block()
        self.score=0
    
    #Verificar si la celda esta ocupada
    def block_fits(self):
        tiles=self.current_block.get_cells_position()
        for tile in tiles:
            if self.grid.empty(tile.row,tile.column)==False:
                return False
        return True

    #Rotaciones
    def rotate(self):
        self.current_block.rotate()     
        if self.block_inside()==False or self.block_fits()==False:
            self.current_block.not_rotate()
    
    #Comprobar que la pieza este fuera de la malla
    def block_inside(self):
        tiles=self.current_block.get_cells_position()
        for tile in tiles:
            if self.grid.inside(tile.row,tile.column)==False:
                return False
        return True

    #Metodo para dibujar las piezas
    def draw(self,screen):
        self.grid.draw(screen)
        self.current_block.draw(screen,11,11)

        #Centrar algunas piezas
        if self.next_block.id==1:
            self.next_block.draw(screen,255,290)
        elif self.next_block.id==7:
            self.next_block.draw(screen,255,280)
        else:
            self.next_block.draw(screen,270,270)