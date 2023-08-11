class Mao():
  def __init__(self):
    self.cartas = [] 
    self.soma = 0
    self.imagens = []

  def adicionar(self, carta):
    print(carta)
    self.cartas.append(carta)
    self.imagens.append("".join((carta[0], carta[1])))
  
  def calcularMao(self):
    total = 0

    ordem_carta = [carta[0] for carta in self.cartas]
    nao_ases = [carta for carta in ordem_carta if carta != 'A']
    ases = [carta for carta in ordem_carta if carta == 'A']

    print(nao_ases, ases)

    for carta in nao_ases:
      if carta in 'JQK':
        total += 10
      else:
        total += int(carta)
    
    for carta in ases:
      if total <= 10:
        total += 11
      else:
        total += 1

    self.soma = total 