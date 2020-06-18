#tocando MP3 com a lib pygame
import pygame
pygame.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer_music.play()
pygame.event.wait()

