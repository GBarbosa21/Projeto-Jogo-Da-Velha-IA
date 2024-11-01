import random
import csv

# Representação do tabuleiro
tabuleiro = [0] * 15  # Tamanho fixo de 15, mesmo que nem todas as posições sejam usadas

# Função para imprimir o tabuleiro (usa as posições de 1 a 9 da lista)
def imprimir_tabuleiro():
    for i in range(1, 10, 3):
        linha = [tabuleiro[i], tabuleiro[i + 1], tabuleiro[i + 2]]
        print(f"{linha[0]} | {linha[1]} | {linha[2]}")
        if i < 7:
            print("---------")

# Função para verificar se há um vencedor (usa as posições de 1 a 9)
def verificar_vencedor():
    # Verificar linhas
    for i in range(1, 10, 3):
        if tabuleiro[i] == tabuleiro[i + 1] == tabuleiro[i + 2] and tabuleiro[i] != 0:
            return tabuleiro[i]
    # Verificar colunas
    for i in range(1, 4):
        if tabuleiro[i] == tabuleiro[i + 3] == tabuleiro[i + 6] and tabuleiro[i] != 0:
            return tabuleiro[i]
    # Verificar diagonais
    if (tabuleiro[1] == tabuleiro[5] == tabuleiro[9] and tabuleiro[1] != 0) or \
       (tabuleiro[3] == tabuleiro[5] == tabuleiro[7] and tabuleiro[3] != 0):
        return tabuleiro[5]
    return None  # Nenhum vencedor ainda

# Função para verificar se a jogada é válida (posição entre 1 e 9)
def verificar_validade(jogada):
    if tabuleiro[jogada] == 0:
        return True
    return False

# Função para salvar os resultados em um arquivo CSV
def salvar_resultados_csv(arquivo, resultados):
    with open(arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escrevendo os títulos das colunas
        writer.writerow(['Partida', 'Tabuleiro', 'Vencedor', 'Vitorias Jogador 1', 'Vitorias Jogador 2', 'Empates'])
        
        # Escrevendo os resultados de cada partida
        for i, resultado in enumerate(resultados, start=1):
            writer.writerow([i, resultado['tabuleiro'], resultado['vencedor'], resultado['vitorias_jog1'], resultado['vitorias_jog2'], resultado['empates']])


resultados_partidas = []

for _ in range(100000):  # Para jogar X rodadas
    burro = 1  # Jogador 1
    campeao = -1  # Jogador 2
    vencedor = None
    caminho = None

    # Reiniciar o tabuleiro e o contador de jogadas
    tabuleiro[:11] = [0] * 11  # Reinicia todas as posições do tabuleiro

    # Loop principal do jogo
    while vencedor is None and tabuleiro[0] < 9:
        # Jogada do jogador burro
        posicao = jogada_burro()
        while not verificar_validade(posicao):
            posicao = jogada_burro()

        # Registrar a jogada do burro
        tabuleiro[posicao] = burro
        tabuleiro[0] += 1  # Contador de jogadas
        
        # Verificar vencedor após a jogada do burro
        vencedor = verificar_vencedor()
        
        print("\nTabuleiro após jogada do burro:")
        imprimir_tabuleiro()  # Exibir o tabuleiro após a jogada do burro
        print("\n")

        # Jogada do campeão
        posicao, caminho = jogada_campeao(tabuleiro, campeao, caminho)
        if posicao is not None and 1 <= posicao <= 9:
            tabuleiro[posicao] = campeao
            tabuleiro[0] += 1  # Contador de jogadas
            print(f"Posição de jogada: {posicao}")
            print(f"Caminho após verificar possibilidade: {caminho}")
        else:
            print("Erro: Posição inválida retornada pela função jogada_campeao.")
        # Trate o erro de acordo com as necessidades do seu jogo
        # Verificar se há vencedor após a jogada do campeão
        vencedor = verificar_vencedor()
        if vencedor is not None or tabuleiro[0] >= 9:
            break

        print("\nTabuleiro após jogada do campeão:")
        imprimir_tabuleiro()  # Exibir o tabuleiro após a jogada do campeão
        print("\n")
        
    # Exibir o tabuleiro final após o término do jogo
    print("Tabuleiro final:")
    imprimir_tabuleiro()

    # Exibir o resultado final
    if vencedor is not None:
        print(f"Vencedor: {vencedor}")
    else:
        print("Empate!")    

    if vencedor == 1:
        break
        print("Jogador 1 venceu!")
        tabuleiro[12] += 1  # Atualiza contador de vitórias do jogador 1
    elif vencedor == -1:
        print("Jogador 2 venceu!")
        tabuleiro[14] += 1  # Atualiza contador de vitórias do jogador 2
    else:
        print("Empate!")
        tabuleiro[13] += 1  # Atualiza contador de empates

    tabuleiro[10] += 1  # Atualiza contador de partidas jogadas

    resultado_partida = {
        'tabuleiro': tabuleiro[1:10],  # Somente as posições do tabuleiro (1 a 9)
        'vencedor': vencedor if vencedor is not None else "Empate",
        'vitorias_jog1': tabuleiro[12],
        'vitorias_jog2': tabuleiro[14],
        'empates': tabuleiro[13]
    }
    resultados_partidas.append(resultado_partida)

# Salvar os resultados em um arquivo CSV
salvar_resultados_csv('resultados_tic_tac_toe.csv', resultados_partidas)

print("Resultados salvos em 'resultados_tic_tac_toe.csv'.")