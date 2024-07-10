import pygame
from colors import Colors
from position import Position

#Una sola clase base llamada Block, con el código común y sus características.
class Block:
    def __init__(self, id):
        self.id=id 
        self.cells= {}  #diccionario
        self.cell_size=30 #el tamaño de la celda
        self.row_offset=0 #Nueva posicion de las filas de la pieza
        self.column_offset=0 #Nueva posicion de las columnas de la pieza
        self.rotation_state=0 #la rotación la configuramos en 0.
        self.colors=Colors.get_cells_colors()
    
    #Movilidad de las piezas
    def move(self,rows,columns):
        self.row_offset+=rows
        self.column_offset+=columns
    
    #Obtener la posicion de celdas ocupadas
    def get_cells_position(self):
        tiles=self.cells[self.rotation_state]
        move_tiles=[]
        for position in tiles:
            pos=Position(position.row+self.row_offset,position.column+self.column_offset)
            move_tiles.append(pos)
        return move_tiles
    
    #Rotacion de las piezas
    def rotate(self):
        self.rotation_state+=1
        if self.rotation_state==len(self.cells):
            self.rotation_state=0
    
    #Verificar si es posible la rotacion
    def not_rotate(self):
        self.rotation_state-=1
        if self.rotation_state==0:
            self.rotation_state=len(self.cells)-1

    
    #Dibujar las piezas en la malla
    def draw(self, screen, offset_x, offset_y):
        tiles=self.get_cells_position() #Esta línea recupera la lista de las posiciones para la rotación actual de las piezas.
        for tile in tiles:
            f=pygame.font.SysFont("Impact",20)
            cell=f.render(str(self.id),True,Colors.white)
            tile_rect=pygame.Rect(offset_x+tile.column * self.cell_size,offset_y+tile.row * self.cell_size,self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect) #El valor del color de la celda es obtenida de la lista de colores
            screen.blit(cell,cell.get_rect(centerx=tile_rect.centerx, centery=tile_rect.centery))  