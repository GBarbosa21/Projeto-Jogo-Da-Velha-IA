import random

#JOGADOR BURRO VAI ESCOLHER "ALEATORIAMENTE" UMA JOGADA POSSÍVEL
def jogada_burro(self):
    jogada = random.choice([0, 9])
    self.jogadas.append(jogada)
    return jogada
