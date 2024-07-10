import pygame
import sys
import random
import time
from game import Game
from colors import Colors
from datetime import datetime
from blocks import *

#Solicitar dimensiones de la matriz
flag=True
while flag:
    n=int(input("Ingrese la dimension del tablero (12/15)): " ))
    modo=input("Ingrese una modo de juego (tiempo/movimiento): ")
    if modo=="tiempo":
        tiempo=int(input("Ingrese los segundos de juego: "))
        aux_tiempo=tiempo
    if modo=="movimiento":
        movimientos=int(input("Ingrese la cantidad de movimientos: "))
        aux_movimientos=movimientos
    usuario=input("Ingrese su usuario: ")
    name=input("Ingrese su nombre: ")
    edo=input("Ingrese su estado: ")
    if n==12 or n==15 or n==9:
        flag=False
    else:
        print("Ingrese una dimension valida")

codigo_juego=000 #Codigo del juego
time=datetime.now() #Fecha actual


#Inicio del juego
pygame.init()

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

#Fuente del titulo y dibujar el texto en pantalla
def dibujar_texto(texto,color,x,y):
        fuente=pygame.font.SysFont("Impact",30)
        text=fuente.render(texto,True,color)
        screen.blit(text,(x,y))

#Piezas Seleccionadas
block=[block_1(),block_2(),block_3(),block_4(),block_5(),block_6(),block_7(),block_8(),block_9()]
piezas=[2,3,4,5,7]
piezas_act=[x-1 for x in piezas]
pieza=[]
for i in range (len(piezas_act)):
    pieza.append(block[piezas_act[i]])

#Recuadros para mostrar el puntaje y la pieza siguiente
score_rect=pygame.Rect(520,80,170,60)
next_rect=pygame.Rect(740,230,150,130)
mode_rect=pygame.Rect(535,230,150,130)

#Crear pantalla del juego
screen=pygame.display.set_mode((950,550))

#Titulo de la pantalla
pygame.display.set_caption("Epic Tetris")

#Velocidad del juego
clock=pygame.time.Clock()

#Iniciar el juego
game=Game(n,pieza,piezas_act)

#Evento para actualizar las posiciones de las piezas
GAME_UPDATE=pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,200) #Crea un temporizador que dispara GAME_UPDATE cada 200miliseg.

frase=random_frase()
ultima_frase=pygame.time.get_ticks()
ult_tiempo=pygame.time.get_ticks()

while True:
    for event in pygame.event.get(): #Verificar que el evento del ciclo actual no sea salir
        if event.type==pygame.QUIT: #Salir del juego
            pygame.quit()
            sys.exit() #Cerrar el programa
        if event.type==pygame.KEYDOWN:

            #Modo de tiempo
            if modo=="tiempo":
                if game.game_over:
                    codigo_juego+=1
                    registro(codigo_juego,50,game.score)
                    game.game_over=False
                    game.reset(piezas_act)
                if event.key==pygame.K_LEFT and game.game_over==False:
                    game.move_left()
                if event.key==pygame.K_RIGHT and game.game_over==False:
                    game.move_right()
                if event.key==pygame.K_DOWN and game.game_over==False:
                    game.move_down(piezas_act)
                if event.key==pygame.K_UP and game.game_over==False:
                    game.rotate()

            #Modo de movimientos
            if modo=="movimiento":
                if game.game_over:
                    codigo_juego+=1
                    registro(codigo_juego,50,game.score)
                    game.game_over=False
                    game.reset(piezas_act)
                if event.key==pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                if event.key==pygame.K_RIGHT and game.game_over == False:
                    game.move_right()
                if event.key==pygame.K_DOWN and game.game_over == False:
                    game.move_dowm(piezas_act,movimientos)
                if event.key==pygame.K_UP and game.game_over == False:
                    game.rotate()

        #Actualizacion del juego
        if event.type==GAME_UPDATE and game.game_over==False and modo=="tiempo": #La posicion se actualiza solo cuando se dispara
            tiempo_act=pygame.time.get_ticks()
            if tiempo_act-ult_tiempo>=1000:  # 30 segundos
                tiempo-=1
                ult_tiempo=tiempo_act
            if tiempo==0:
                game.game_over=True
                tiempo=aux_tiempo
            game.move_down(piezas_act)

        elif event.type==GAME_UPDATE and game.game_over==False and modo=="movimiento":
            game.move_dowm(piezas_act,movimientos)
            tiempo_act=pygame.time.get_ticks()
            if tiempo_act-ult_tiempo>=2500:  # 30 segundos
                movimientos-=1
                ult_tiempo=tiempo_act
            if game.game_over:
                game.game_over=False
                movimientos=aux_movimientos
                game.move_dowm(piezas_act,movimientos)

    if game.game_over and modo=="tiempo":
        tiempo=aux_tiempo

    if game.game_over and modo=="movimiento":
        movimientos=aux_movimientos

    tiempo_act=pygame.time.get_ticks()
    if tiempo_act-ultima_frase>=3000:  # 30 segundos
        frase=random_frase()
        ultima_frase=tiempo_act
    
    #Dibujar la pantalla
    screen.fill(Colors.d)

    #Dibujar cada uno de los items de la pantalla
    font=pygame.font.SysFont("Impact",30)
    dibujar_texto(name,Colors.white,750,20)
    score_value=font.render(str(game.score),True,Colors.white)
    dibujar_texto("Puntaje",Colors.white,560,20)
    dibujar_texto(usuario,Colors.white,740,60)
    dibujar_texto(edo,Colors.white,760,100)
    dibujar_texto(frase,Colors.white,480,400)  
    dibujar_texto("Siguiente",Colors.white,750,180)

    if modo=="tiempo":
        dibujar_texto("Tiempo",Colors.white,555,180)
        pygame.draw.rect(screen,Colors.light_blue,mode_rect,0,10)
        tiempo_value=font.render(str(tiempo),True,Colors.white)
        screen.blit(tiempo_value,tiempo_value.get_rect(centerx=mode_rect.centerx,centery=mode_rect.centery))
        if game.game_over:
            dibujar_texto("GAME OVER",Colors.red,600,480) 

    elif modo=="movimiento":
        dibujar_texto("Movimiento",Colors.white,550,180)
        pygame.draw.rect(screen,Colors.light_blue,mode_rect,0,10)
        movi_value=font.render(str(movimientos),True,Colors.white)
        screen.blit(movi_value,movi_value.get_rect(centerx=mode_rect.centerx,centery=mode_rect.centery))
        if game.game_over:
            dibujar_texto("GAME OVER",Colors.red,600,480) 
       
    
    pygame.draw.rect(screen,Colors.light_blue,score_rect,0,10) #Dibujar recuadro
    screen.blit(score_value,score_value.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))   
    pygame.draw.rect(screen,Colors.light_blue,next_rect,0,10)
    game.draw(screen)

    pygame.display.update() #Actualiza los cambios en los objetos del juego e imprime una imagen de ellos
    clock.tick(45) #Numero de frames por segundo








    