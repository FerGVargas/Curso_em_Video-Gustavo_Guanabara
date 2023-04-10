# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygames
pygame.init()
pygame.mixer.music.load('my_dreams.mp3')
pygame.mixer.music.paly()
pygame.event.wait()