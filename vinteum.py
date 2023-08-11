from pygame import *
from baralho import *
from mao import *
import time

mixer = pygame.mixer
mixer.init()

def convCarta(carta="back"):
  image = pygame.image.load('images/' + carta + '.png').convert()

  return pygame.transform.scale(image, (DIMENSAO_CARTA))

class VinteUm:
  def __init__(self, tela):
    self.baralho = Baralho()
    self.jogador = Mao()
    self.banca = Mao()
    self.tela = tela
    self.segurou = False
    self.jogando = True

    self.baralho.embaralhar()

  def distribuir(self):
    for i in range(2):
      self.banca.adicionar(self.baralho.comprar())
      self.jogador.adicionar(self.baralho.comprar())

    self.jogador.calcularMao()

    self.tela.blit(convCarta(self.banca.imagens[0]), (300, 100))
    self.tela.blit(convCarta(), (370, 100))
    
    self.tela.blit(convCarta(self.jogador.imagens[0]), (300, 450))
    self.tela.blit(convCarta(self.jogador.imagens[1]), (370, 450))
  
  def checarResultado(self):

    def Final(image, audio, saida_terminal):
      self.tela.blit(image, (0, 0))
      mixer.music.load(audio)
      print(saida_terminal)

    pygame.time.delay(1000)
    self.tela.fill(black)

    if self.jogador.soma > 21:
      Final(imagem_jogador_perdeu, "audios/perdeu.mp3", "jogador perdeu")

    elif self.banca.soma > 21 or self.jogador.soma > self.banca.soma:
      Final(imagem_jogador_ganhou, "audios/ganhou.mp3", "jogador ganhou")

    elif self.banca.soma == self.jogador.soma:
      Final(imagem_jogador_empatou, "audios/empatou.mp3, jogador empatou")

    else:
      Final(imagem_jogador_perdeu, "audios/perdeu.mp3", "jogador perdeu")

    mixer.music.play()

  def comprar(self):
    if not self.segurou:
      self.jogador.adicionar(self.baralho.comprar())

      i = len(self.jogador.cartas)-1

      self.tela.blit(convCarta(self.jogador.imagens[i]), (300 + i*70 ,450))
      
      self.jogador.calcularMao()
      pygame.display.flip()

    if self.jogador.soma > 21:
      self.checarResultado()

  def segurar(self):
    self.segurou = True
    i = 2

    self.tela.blit(convCarta(self.banca.imagens[1]), (370 ,100))
    pygame.display.flip()
    self.banca.calcularMao()
    pygame.time.wait(2000)

    while self.jogador.soma > self.banca.soma < 17:
      
      self.banca.adicionar(self.baralho.comprar())

      self.tela.blit(convCarta(self.banca.imagens[i]), (300 + i*70 ,100))
    
      self.banca.calcularMao()
      # texto(f"soma: {jogo.banca.soma}", 700, 50)
      print('soma banca:', self.banca.soma)

      pygame.display.flip()
      pygame.time.wait(1500)
      i += 1

    self.checarResultado()