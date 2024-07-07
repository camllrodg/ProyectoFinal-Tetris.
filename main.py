import pygame
import sys
import random
import time
from game import Game
from colors import Colors
from datetime import datetime

#Solicitar dimensiones de la matriz
flag=True
while flag:
    n=int(input("Ingrese la dimension del tablero (12/15)): " ))
    if n==12 or n==15:
        flag=False
    else:
        print("Ingrese una dimension valida")

#Generar las frases de los ODS
def random_frase():
        frases=["El fin de la pobreza es nuestro desafío","¡No desperdiciemos la comida!","El ejercicio es la clave para la salud física","El conocimiento es poder."
        "La igualdad de género es libertad.","Agua limpia para todos","La energía solar ilumina el camino.","Elige un trabajo que te guste","La mejor manera de predecir el futuro es inventándolo.",
        "No importa de dónde venimos, si no a dónde vamos.","¡Mantén limpia a tu ciudad!","Compra menos, elige bien, hazlo durar.","El clima está cambiando.","El agua pertenece al océano, la botella no.","¡Cuida el medio ambiente!", 
        "Sin justicia solo hay divisiones","Juntos creamos el cambio:)"]
        if len(frases)==0: #Si ya se mostraron todas las piezas
            frases=["El fin de la pobreza es nuestro desafío","¡No desperdiciemos la comida!","El ejercicio es la clave para la salud física","El conocimiento es poder."
        "La igualdad de género es libertad.","Agua limpia para todos","La energía solar ilumina el camino.","Elige un trabajo que te guste","La mejor manera de predecir el futuro es inventándolo.",
        "No importa de dónde venimos, si no a dónde vamos.","¡Mantén limpia a tu ciudad!","Compra menos, elige bien, hazlo durar.","El clima está cambiando.","El agua pertenece al océano, la botella no.","¡Cuida el medio ambiente!", 
        "Sin justicia solo hay divisiones","Juntos creamos el cambio:)"]
        frase=random.choice(frases)
        frases.remove(frase)
        return frase

#Inicio del juego
pygame.init()

#Fuente del titulo y dibujar el texto en pantalla
def texto(texto,x,y):
        fuente=pygame.font.SysFont("Impact",30)
        text=fuente.render(texto,True,Colors.white)
        screen.blit(text,(x,y))

#Recuadros para mostrar el puntaje y la pieza siguiente
score_rect=pygame.Rect(520,80,170,60)
ods_rect=pygame.Rect(510,215,200,160)

#Crear pantalla del juego
screen=pygame.display.set_mode((750,500))

#Titulo de la pantalla
pygame.display.set_caption("Epic Tetris")

#Velocidad del juego
clock=pygame.time.Clock()

game=Game(n)

#Evento para actualizar las posiciones de las piezas
GAME_UPDATE=pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,200) #Crea un temporizador que dispara GAME_UPDATE cada 200miliseg.

flag=True
while flag:
    for event in pygame.event.get(): #Verificar que el evento del ciclo actual no sea salir
        if event.type==pygame.QUIT: #Salir del juego
            pygame.quit()
            sys.exit() #Cerrar el programa
        if event.type==pygame.KEYDOWN:
            if game.game_over==True:
                game.game_over=False
                game.reset()
            if event.key==pygame.K_LEFT and game.game_over==False:
                game.move_left()
            if event.key==pygame.K_RIGHT and game.game_over==False:
                game.move_right()
            if event.key==pygame.K_DOWN and game.game_over==False:
                game.move_down()
            if event.key==pygame.K_UP and game.game_over==False:
                game.rotate()
        if event.type==GAME_UPDATE and game.game_over==False : #La posicion se actualiza solo cuando se dispara
            game.move_down() 
        
    frase=random_frase()
    
    #Dibujar la pantalla
    screen.fill(Colors.d)
    texto("Puntaje",550,20)
    f=pygame.font.SysFont("Impact",30)
    score_value=f.render(str(game.score),True,Colors.white)
    texto(frase,550,180)   

    if game.game_over==True:
        texto("GAME OVER",520,400)    
    
    pygame.draw.rect(screen,Colors.light_blue,score_rect,0,10) #Dibujar recuadro
    screen.blit(score_value,score_value.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))   


    """
    screen.blit(score_surface,(550,20,50,50)) #Mostrar el texto
    screen.blit(next_surface, (535,180,50,50))

    if game.game_over==True:
        screen.blit(game_over_surface,(530,450,50,50))

    pygame.draw.rect(screen,Colors.light_blue,score_rect,0,10) #Dibujar recuadro
    screen.blit(score_value,score_value.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen,Colors.light_blue,next_rect,0,10)
    """
    game.draw(screen)

    pygame.display.update() #Actualiza los cambios en los objetos del juego e imprime una imagen de ellos
    clock.tick(60) #Numero de frames por segundo
 