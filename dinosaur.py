# importar el modulo de pygame
import pygame
from pygame.locals import *
import os
import sys
import math
import time

pygame.init() # inicio de pygame
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 500]) # pantalla
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
cactus = []
dinosaur = pygame.image.load('img/dinosaur.png')
dinosaur = pygame.transform.scale(dinosaur, (100, 100))
for i in range(0,10):
    temp = pygame.image.load('img/cactus.png')
    temp = pygame.transform.scale(temp, (50, 50))
    cactus.append(temp)
dinosaurY = 300
subiendo = False
bajada = False
contador = 0
cactusX = [300, 500, 800, 1200, 1600, 1800, 2000, 2200, 2500, 3000]
cactusCopia = [300, 500, 800, 1200, 1600, 1800, 2000, 2200, 2500, 3000]
startTimer = True
tiempoFinal = True
while True:
    if startTimer == True:
        t0 = time.time()
        startTimer = False
    cactusBox = []
    for i in range(0,10):
        cactusBox.append(pygame.Rect(cactusX[i]+10, 370, 30, 30))
    dinosaurBox = pygame.Rect(8, dinosaurY, 80, 80)
    for i in range(0,10):
        cactusX[i]-=0.3
    if subiendo == True:
        contador+=1
        if contador%3==0:
            dinosaurY -= 1
        if contador >= 300:
            subiendo = False
            contador = 0
            bajada = True
    if bajada == True:
        contador+=1
        if contador%3==0:
            dinosaurY +=1
        if contador >= 300:
            contador = 0
            bajada = False
    # si cierran la ventana
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                if subiendo == False and bajada == False:
                    subiendo = True
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    for i in range(0,10):
        if dinosaurBox.colliderect(cactusBox[i]):
            for i in range(0,10):
                cactusX[i] = cactusCopia[i]
    screen.fill(WHITE)

    for i in range(0,10):
        screen.blit(cactus[i], (cactusX[i],350))
    pygame.draw.line(screen, BLACK, (0, 400), (1000, 400), 5)
    screen.blit(dinosaur, (0, dinosaurY))
    if cactusX[0] <= -3000:
        if tiempoFinal == True:
            t1 = time.time()
            tiempoFinal = False
        print("Tiempo final: " + str(t1-t0))
        pygame.quit()
        sys.exit(0)
    #pygame.draw.rect(screen, (255, 0, 0), dinosaurBox)
    for i in range(0,10):
        pygame.draw.rect(screen, (0, 255, 0), cactusBox[i])
    pygame.display.flip()