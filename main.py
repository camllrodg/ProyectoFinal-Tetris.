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

codigo_juego=000 #Codigo del juego
time=datetime.now() #Fecha actual

#Generar las frases de los ODS
def random_frase():
        frases=["Fin de la pobreza","¡No desperdiciemos la comida!","El ejercicio es clave para la salud","El conocimiento es poder.",
        "La igualdad de género es libertad.","Agua limpia para todos","La energía solar ilumina el camino.","Elige un trabajo que te guste","El futuro se predice inventándolo.",
        "No importa de dónde venimos.","¡Mantén limpia a tu ciudad!","Elige bien, hazlo durar.","El clima está cambiando.","La botella no pertenece al océano.","¡Cuida el medio ambiente!", 
        "Sin justicia solo hay divisiones","Juntos creamos el cambio:)"]
        if len(frases)==0: #Si ya se mostraron todas las piezas
            frases=["Fin de la pobreza","¡No desperdiciemos la comida!","El ejercicio es clave para la salud","El conocimiento es poder.",
        "La igualdad de género es libertad.","Agua limpia para todos","La energía solar ilumina el camino.","Elige un trabajo que te guste","El futuro se predice inventándolo.",
        "No importa de dónde venimos.","¡Mantén limpia a tu ciudad!","Elige bien, hazlo durar.","El clima está cambiando.","La botella no pertenece al océano.","¡Cuida el medio ambiente!", 
        "Sin justicia solo hay divisiones","Juntos creamos el cambio:)"]
        frase=random.choice(frases)
        frases.remove(frase)
        return frase

#Registro de las jugadas
def registro(codigo,iden,score):
    fecha=f"{time.day}-{time.month}-{time.year}"
    hora=f"{time.hour}:{time.minute}"
    f=open("JUEGOS.bin","ab")
    cad=f"{codigo}/{iden}/{score}/{fecha}/{hora}\n"
    f.write(cad.encode())
    f.close()

#Inicio del juego
pygame.init()

tiempo=60

#Fuente del titulo y dibujar el texto en pantalla
def dibujar_texto(texto,color,x,y):
        fuente=pygame.font.SysFont("Impact",30)
        text=fuente.render(texto,True,color)
        screen.blit(text,(x,y))

#Recuadros para mostrar el puntaje y la pieza siguiente
score_rect=pygame.Rect(520,80,170,60)
ods_rect=pygame.Rect(510,215,200,160)

#Crear pantalla del juego
screen=pygame.display.set_mode((950,550))

#Titulo de la pantalla
pygame.display.set_caption("Epic Tetris")

#Velocidad del juego
clock=pygame.time.Clock()

game=Game(n)

#Evento para actualizar las posiciones de las piezas
GAME_UPDATE=pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,200) #Crea un temporizador que dispara GAME_UPDATE cada 200miliseg.

frase=random_frase()
ultima_frase=pygame.time.get_ticks()
while True:
    for event in pygame.event.get(): #Verificar que el evento del ciclo actual no sea salir
        if event.type==pygame.QUIT: #Salir del juego
            pygame.quit()
            sys.exit() #Cerrar el programa
        if event.type==pygame.KEYDOWN:
            if game.game_over==True:
                codigo_juego+=1
                registro(codigo_juego,50,game.score)
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
    tiempo_act=pygame.time.get_ticks()
    if tiempo_act-ultima_frase>=3000:  # 30 segundos
        frase=random_frase()
        ultima_frase=tiempo_act
    
    #Dibujar la pantalla
    screen.fill(Colors.d)
    dibujar_texto("Puntaje",Colors.white,550,20)
    f=pygame.font.SysFont("Impact",30)
    score_value=f.render(str(game.score),True,Colors.white)
    dibujar_texto("Jose",Colors.white,770,20)
    dibujar_texto("jicandurin",Colors.white,740,60)
    dibujar_texto("Bolivar",Colors.white,760,100)
    dibujar_texto(frase,Colors.white,480,400)   

    if game.game_over==True:
        dibujar_texto("GAME OVER",Colors.red,600,480)    
    
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
 