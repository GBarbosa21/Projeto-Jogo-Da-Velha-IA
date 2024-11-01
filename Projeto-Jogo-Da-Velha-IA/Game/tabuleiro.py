import csv

def imprimir_tabuleiro(tabuleiro):
    for i in range(1, 10, 3):
        linha = [tabuleiro[i], tabuleiro[i + 1], tabuleiro[i + 2]]
        print(f"{linha[0]} | {linha[1]} | {linha[2]}")
        if i < 7:
            print("---------")

def verificar_vencedor(tabuleiro):
    for i in range(1, 10, 3):
        if tabuleiro[i] == tabuleiro[i + 1] == tabuleiro[i + 2] and tabuleiro[i] != 0:
            return tabuleiro[i]
    for i in range(1, 4):
        if tabuleiro[i] == tabuleiro[i + 3] == tabuleiro[i + 6] and tabuleiro[i] != 0:
            return tabuleiro[i]
    if (tabuleiro[1] == tabuleiro[5] == tabuleiro[9] and tabuleiro[1] != 0) or \
       (tabuleiro[3] == tabuleiro[5] == tabuleiro[7] and tabuleiro[3] != 0):
        return tabuleiro[5]
    return None

def verificar_validade(jogada, tabuleiro):
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