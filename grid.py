import pygame
from colors import Colors
from block import *

#Creacion de la malla
class Grid:
    def __init__(self,dimen):
        self.num_rows=dimen
        self.num_cols=dimen
        self.cell_size=30
        self.grid=[[0 for j in range(self.num_cols)] for i in range (self.num_rows)]
        self.colors=Colors.get_cells_colors()

    #Imprimir la malla
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column],end=" ")
            print()
    
    #Comprobar que todas las posiciones de la pieza, esten en la malla
    def inside(self,row,column):
        if row>=0 and row<self.num_rows and column>=0 and column<self.num_cols:
            return True
        else:
            return False
    
    #Verificar si la celda esta vacia
    def empty(self,row,column):
        if self.grid[row][column]==0:
            return True
        return False

    #Verificar si una fila esta llena 
    def full_row(self,row):
        for column in range(self.num_cols):
            if self.grid[row][column]==0:
                return False
        return True

    #Eliminar fila
    def delete_row(self,row):
        for column in range(self.num_cols):
            self.grid[row][column]=0
    
    #Mover la fila de arriba hacia abajo
    def move_row(self,row,num_rows):
        for column in range(self.num_cols):
            self.grid[row+num_rows][column]=self.grid[row][column]
            self.grid[row][column]=0

    #Eliminar fila llena
    def delete_full_row(self):
        full=0
        valores=[]
        for row in range(self.num_rows-1,0,-1):
            if self.full_row(row):
                for column in range(self.num_cols):
                    valores.append(self.grid[row][column])
                self.delete_row(row)
                full+=1
            elif full>0:
                self.move_row(row, full)
        return full, valores

    #Restablecer juego
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column]=0            
    
    #Dibujar las piezas
    def draw(self,screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value=self.grid[row][column]
                cell_rect=pygame.Rect(column*self.cell_size +11,row*self.cell_size +11,self.cell_size -1,self.cell_size -1) #Creacion de las celdas
                pygame.draw.rect(screen,self.colors[cell_value],cell_rect) #Dibujar las celdas
        

        