import random
from Game.tabuleiro import tabuleiro

#JOGADOR BURRO VAI BUSCAR TODAS AS POSIÇÕES E ESCOLHER UMA QUE SEJA IGUAL A 0 (SEM NENHUMA JOGADA)
def burro(self, tabuleiro):
    jogada = random.choice([i for i, x in enumerate(tabuleiro) if x == 0])
    self.jogadas.append(jogada)
    return jogada
