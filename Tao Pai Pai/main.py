import pygame
import random

pygame.init()
ancho_ventana = 500
alto_ventana = 800
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Tao Pai Pai Pai")
clock = pygame.time.Clock()
cielo = pygame.image.load("./images/cielo.webp")
montanas = pygame.image.load("./images/montanas.webp")
viento = pygame.image.load("./images/viento.webp")
tao = pygame.image.load("./images/tao.webp")

#Obtener la altura y ancho de la imagen
ancho_cielo = cielo.get_width()
#alto_cielo = cielo.get_height()
ancho_montanas = montanas.get_width()
alto_montanas = montanas.get_height()
ancho_viento = viento.get_width()
#alto_viento = viento.get_height()
#ancho_tao = tao.get_width()
#alto_tao = tao.get_height()

posicion_x_cielo = posicion_x_montanas = posicion_x_viento =0

velocidad_x_cielo = 1
velocidad_x_montanas =2
velocidad_x_viento = 5

tao_pos_y = 100
tao_pos_x = 200
velocida_tao = 5
rango_movimiento_tao = (100,500)

temblor = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and tao_pos_y > rango_movimiento_tao[0]:
        tao_pos_y -= velocida_tao
    if keys[pygame.K_DOWN] and tao_pos_y < rango_movimiento_tao[1]:
        tao_pos_y += velocida_tao
    tiembla = random.randint(-temblor,temblor)

    posicion_x_cielo -= velocidad_x_cielo
    posicion_x_montanas -= velocidad_x_montanas 
    posicion_y_montanas = alto_ventana - alto_montanas
    posicion_x_viento -= velocidad_x_viento

    if posicion_x_cielo <= -ancho_cielo:
        posicion_x_cielo = 0
    if posicion_x_montanas <= -ancho_montanas:
        posicion_x_montanas = 0
    if posicion_x_viento <= -ancho_viento:
        posicion_x_viento = 0

    screen.blit(cielo, (posicion_x_cielo, 0))
    screen.blit(cielo, (posicion_x_cielo+ ancho_cielo,0))
    screen.blit(montanas, (posicion_x_montanas, posicion_y_montanas))
    screen.blit(montanas, (posicion_x_montanas + ancho_montanas , posicion_y_montanas))
    screen.blit(viento, (posicion_x_viento,0))    
    screen.blit(viento, (posicion_x_viento+ ancho_viento,0))
    screen.blit(tao, (tao_pos_x, tao_pos_y + tiembla))

    pygame.display.flip()
    clock.tick(60)
