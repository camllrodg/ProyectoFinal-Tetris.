import pygame
import sys
from game import Game
from colors import Colors

pygame.init()

#Fuente del titulo
title_font=pygame.font.Font(None,40)
score_surface=title_font.render("Puntaje",True,Colors.white)
next_surface=title_font.render("Siguiente",True,Colors.white)
game_over_surface=title_font.render("GAME OVER",True,Colors.white)

#Recuadros para mostrar el puntaje y la pieza siguiente
score_rect=pygame.Rect(320,55,170,60)
next_rect=pygame.Rect(320,215,170,180)

#Crear pantalla del juego
screen=pygame.display.set_mode((500,620))

#Titulo de la pantalla
pygame.display.set_caption("Epic Tetris")

#Velocidad del juego
clock=pygame.time.Clock()

game=Game()

#Evento para actualizar las posiciones de las piezas
GAME_UPDATE=pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,200) #Crea un temporizador que dispara GAME_UPDATE cada 200miliseg.

while True:
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
                game.update_score(0,1)
            if event.key==pygame.K_UP and game.game_over==False:
                game.rotate()
        if event.type==GAME_UPDATE and game.game_over==False : #La posicion se actualiza solo cuando se dispara
            game.move_down() 

    #Dibujar la pantalla
    score_value=title_font.render(str(game.score),True,Colors.white)
    screen.fill(Colors.blue)
    screen.blit(score_surface,(360,20,50,50)) #Mostrar el texto
    screen.blit(next_surface, (340,180,50,50))

    if game.game_over==True:
        screen.blit(game_over_surface,(320,450,50,50))

    pygame.draw.rect(screen,Colors.light_blue,score_rect,0,10) #Dibujar recuadro
    screen.blit(score_value,score_value.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen,Colors.light_blue,next_rect,0,10)
    game.draw(screen)

    pygame.display.update() #Actualiza los cambios en los objetos del juego e imprime una imagen de ellos
    clock.tick(60) #Numero de frames por segundo