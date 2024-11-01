import time
import sys
import os

# Adicionando o diretório pai ao sistema para que possamos importar main.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import (
    carregar_base_de_conhecimento,
    JogadorInteligente,
    verificar_vencedor,
    jogada_burro,
    atualizar_ranking,
    salvar_base_de_conhecimento,
)

def testar_velocidade(num_partidas=100000):
    print(f"\nIniciando teste de velocidade para {num_partidas} partidas...")

    # O caminho para a base de conhecimento é relativo ao local do script
    caminho_base_conhecimento = 'base_de_conhecimento.json'
    base_de_conhecimento = carregar_base_de_conhecimento(caminho_base_conhecimento)
    
    inicio = time.time()
    
    partidas_por_salvamento = 10000  # Aumentado para reduzir I/O
    
    for _ in range(num_partidas):
        tabuleiro = [0] * 11
        vencedor = None
        while vencedor is None and tabuleiro[0] < 9:
            # Jogada do jogador inteligente
            posicao = JogadorInteligente(tabuleiro, base_de_conhecimento, caminho_base_conhecimento)
            if 1 <= posicao <= 9 and tabuleiro[posicao] == 0:
                tabuleiro[posicao] = 1
                tabuleiro[0] += 1
            
            vencedor = verificar_vencedor()
            if vencedor is not None or tabuleiro[0] >= 9:
                break

            # Jogada do jogador burro
            posicao = jogada_burro()
            tabuleiro[posicao] = -1
            tabuleiro[0] += 1
            
            vencedor = verificar_vencedor()

        # Atualizar a base de conhecimento
        for i in range(1, 10):
            if tabuleiro[i] != 0:
                ajuste = 1 if (tabuleiro[i] == 1 and vencedor == 1) or (tabuleiro[i] == -1 and vencedor == -1) else -1 if vencedor is not None else 0
                atualizar_ranking(base_de_conhecimento, tabuleiro[1:10], i, ajuste)

        if (_ + 1) % partidas_por_salvamento == 0:
            print(f"Salvando base de conhecimento após a partida {_ + 1}...")
            salvar_base_de_conhecimento(base_de_conhecimento, caminho_base_conhecimento)
    
    fim = time.time()
    tempo_total = fim - inicio
    
    print(f"Tempo total para {num_partidas} partidas: {tempo_total:.4f} segundos!")
    print(f"Velocidade média: {num_partidas / tempo_total:.2f} partidas por segundo!")

if __name__ == "__main__":
    testar_velocidade(num_partidas=100)
