import random
import csv
import os
import timeit
import re
from Game import imprimir_tabuleiro, verificar_vencedor, verificar_validade, salvar_resultados_csv
from IA.burro import jogada_burro
from IA.campeao import jogada_campeao, verificar_possibilidade_de_vencer
from IA.inteligente import JogadorInteligente, consulta_melhor_jogada, atualizar_ranking, salvar_base_de_conhecimento, carregar_base_de_conhecimento

caminho_base_conhecimento = 'base_de_conhecimento.txt'
base_de_conhecimento = carregar_base_de_conhecimento(caminho_base_conhecimento) or {}

# Exemplo de uso
resultados_partidas = []
vitorias_jog1 = 0
vitorias_jog2 = 0
empates = 0

for _ in range(1000):
    Intel = 1  # Jogador 1
    burro = -1  # Jogador 2
    vencedor = None

    # Reiniciar o tabuleiro e o contador de jogadas
    tabuleiro = [0] * 15  # Reinicia o tabuleiro
    tabuleiro[0] = 0  # Reinicia o contador de jogadas

    # Loop principal do jogo
    while vencedor is None and tabuleiro[0] < 9:

        # Jogada do jogador inteligente
        posicao = JogadorInteligente(tabuleiro, base_de_conhecimento, caminho_base_conhecimento)

        if posicao is not None and 1 <= posicao <= 9:
            tabuleiro[posicao] = Intel
            tabuleiro[0] += 1
            atualizar_ranking(base_de_conhecimento, tabuleiro[1:10], posicao, 0)  # 0 para jogada neutra

        vencedor = verificar_vencedor(tabuleiro)
        if vencedor is not None or tabuleiro[0] >= 9:
            break

        # Jogada do jogador burro
        posicao = jogada_burro()
        while not verificar_validade(posicao, tabuleiro):
            posicao = jogada_burro()

        tabuleiro[posicao] = burro
        tabuleiro[0] += 1  # Contador de jogadas
        
        vencedor = verificar_vencedor(tabuleiro)

    # Atualiza a base de conhecimento
    if vencedor == 1:
        vitorias_jog1 += 1
        for posicao in range(1, 10):
            if tabuleiro[posicao] == Intel:
                atualizar_ranking(base_de_conhecimento, tabuleiro[1:10], posicao, 1)
            elif tabuleiro[posicao] == burro:
                atualizar_ranking(base_de_conhecimento, tabuleiro[1:10], posicao, -1)
    elif vencedor == -1:
        vitorias_jog2 += 1
        for posicao in range(1, 10):
            if tabuleiro[posicao] == burro:
                atualizar_ranking(base_de_conhecimento, tabuleiro[1:10], posicao, 1)
            elif tabuleiro[posicao] == Intel:
                atualizar_ranking(base_de_conhecimento, tabuleiro[1:10], posicao, -1)
    else:
        empates += 1

    resultado_partida = {
        'tabuleiro': tabuleiro[1:10],
        'vencedor': vencedor,
        'vitorias_jog1': vitorias_jog1,
        'vitorias_jog2': vitorias_jog2,
        'empates': empates
    }

    resultados_partidas.append(resultado_partida)

# Salvar os resultados das partidas no arquivo CSV
salvar_resultados_csv('resultados_tic_tac_toe.csv', resultados_partidas)

# Salvar a base de conhecimento no arquivo TXT
def salvar_base_de_conhecimento_txt(base_de_conhecimento, caminho):
    with open(caminho, 'w') as f:
        for estado, entradas in base_de_conhecimento.items():
            f.write(f"{estado}:\n")
            for entrada in entradas:
                f.write(f"  Jogada: {entrada['jogada']}, Ranking: {entrada['ranking']}\n ")
            f.write("\n")

salvar_base_de_conhecimento_txt(base_de_conhecimento, 'base_de_conhecimento.txt')
print("Resultados disponíveis!!")