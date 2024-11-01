import random

#JOGADOR BURRO VAI ESCOLHER "ALEATORIAMENTE" UMA JOGADA POSSÍVEL
def jogada_burro():
    return random.choice([i for i in range(1, 10)])
