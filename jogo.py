import pygame as pygame
from utils import *
from vinteum import *

pygame.init()

mixer = pygame.mixer
mixer.init()

tela = pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption("21 do Caneta Azul")

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def texto(text, x, y):
    TextSurf, TextRect = text_objects(text, textfont)
    TextRect.center = (x, y)
    tela.blit(TextSurf, TextRect)

    pygame.display.update()

def menu_de_jogo():
    tela.fill(green)

    mixer.music.stop()
    mixer.music.load("audios/inicial.mp3")
    mixer.music.play()

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jogar()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        tela.blit(imagem_menu_principal, (0, 0))
        pygame.display.flip()

def jogar():
    mixer.music.stop()
    

    tela.fill(plano_de_fundo)
    pygame.draw.rect(tela, grey, pygame.Rect(0, 0, 250, 700))
    tela.blit(imagem_tela_jogo, (0, 0))
    texto("Instruções:", 100, 440)
    texto("Comprar: C", 100, 520)
    texto("Segurar: V", 100, 600)

    jogo = VinteUm(tela)
    
    texto("Banca:", 500, 50)
    texto("Sua mão:", 500, 400)
    
    jogo.distribuir()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and not jogo.segurou:
                    jogo.comprar()
                elif event.key == pygame.K_v and not jogo.segurou:
                    jogo.segurar()
                elif event.key == pygame.K_q:
                    menu_de_jogo()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # texto(f"soma: {jogo.banca.soma}", 700, 50)
            # texto(f"soma: {jogo.jogador.soma}", 700, 400)
        pygame.display.flip()
menu_de_jogo()