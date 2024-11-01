import time
import sys
import os

caminho_base_conhecimento = os.path.join(os.path.dirname(__file__), "data", "base_de_conhecimento.json")

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


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
    
    caminho_base_conhecimento = os.path.join(os.path.dirname(__file__), "..", "data", "base_de_conhecimento.json")
    base_de_conhecimento = carregar_base_de_conhecimento(caminho_base_conhecimento)
    
    inicio = time.time()
    
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

    salvar_base_de_conhecimento(base_de_conhecimento, caminho_base_conhecimento)
    
    fim = time.time()
    tempo_total = fim - inicio
    
    print(f"Tempo total para {num_partidas} partidas: {tempo_total:.4f} segundos!")
    print(f"Velocidade média: {num_partidas / tempo_total:.2f} partidas por segundo!")

if __name__ == "__main__":
    testar_velocidade(num_partidas=100)