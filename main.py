import random, csv, json, os, timeit, re

def reparar_json(conteudo):
    # Remove as linhas que não começam com { ou terminam com }
    linhas_validas = [linha.strip() for linha in conteudo.split('\n') if linha.strip().startswith('{') and linha.strip().endswith('}')]
    
    # Junta as linhas válidas em uma única string
    json_reparado = '[' + ','.join(linhas_validas) + ']'
    
    # Remove quaisquer vírgulas extras entre objetos
    json_reparado = re.sub(r'},\s*]', '}]', json_reparado)
    
    return json_reparado

# Função para carregar o arquivo JSON da base de conhecimento
def carregar_base_de_conhecimento(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            data = json.load(arquivo)
            # Converte a estrutura antiga (lista) para a nova (dicionário)
            if isinstance(data, list):
                new_data = {}
                for entry in data:
                    estado = ''.join(map(str, entry[1:10]))
                    if estado not in new_data:
                        new_data[estado] = []
                    new_data[estado].append({'jogada': entry[0], 'ranking': entry[10]})
                return new_data
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        print("Erro ao carregar o arquivo. Criando nova base de conhecimento.")
        return {}
    

# Função para salvar a base de conhecimento no arquivo JSON
def salvar_base_de_conhecimento(base_de_conhecimento, caminho_arquivo):
    try:
        with open(caminho_arquivo, 'w') as arquivo:
            json.dump(base_de_conhecimento, arquivo, indent=2)
    except Exception as e:
        print(f"Erro ao salvar a base de conhecimento: {e}")

def consulta_melhor_jogada(base_de_conhecimento, estado):
    estado_str = ''.join(map(str, estado))
    if estado_str in base_de_conhecimento:
        melhor_jogada = max(base_de_conhecimento[estado_str], key=lambda x: x['ranking'])
        return melhor_jogada['jogada']
    return None

def atualizar_ranking(base_de_conhecimento, estado, jogada, ajuste):
    estado_str = ''.join(map(str, estado))
    if estado_str not in base_de_conhecimento:
        base_de_conhecimento[estado_str] = []
    
    for entrada in base_de_conhecimento[estado_str]:
        if entrada['jogada'] == jogada:
            entrada['ranking'] += ajuste
            return
    
    base_de_conhecimento[estado_str].append({'jogada': jogada, 'ranking': ajuste})

def JogadorInteligente(tabuleiro, base_de_conhecimento, caminho_arquivo):
    jogada = consulta_melhor_jogada(base_de_conhecimento, tabuleiro[1:10])

    if jogada is None or tabuleiro[jogada] != 0:
        jogadas_disponiveis = [i for i in range(1, 10) if tabuleiro[i] == 0]
        jogada = random.choice(jogadas_disponiveis)
    
    atualizar_ranking(base_de_conhecimento, tabuleiro[1:10], jogada, 0)
    return jogada

# Representação do tabuleiro
tabuleiro = [0] * 15
caminho_base_conhecimento = 'base_de_conhecimento.json'
base_de_conhecimento = carregar_base_de_conhecimento(caminho_base_conhecimento)

# Função para imprimir o tabuleiro (usa as posições de 1 a 9 da lista)
def imprimir_tabuleiro():
    for i in range(1, 10, 3):
        linha = [tabuleiro[i], tabuleiro[i + 1], tabuleiro[i + 2]]
        print(f"{linha[0]} | {linha[1]} | {linha[2]}")
        if i < 7:
            print("---------")

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

# JOGADOR BURRO ESCOLHE UMA JOGADA ALEATÓRIA (apenas entre 1 e 9)
def jogada_burro():
    return random.choice([i for i in range(1, 10) if tabuleiro[i] == 0])

# Exemplo de uso
resultados_partidas = []
vitorias_jog1 = 0
vitorias_jog2 = 0
empates = 0

for _ in range(100000): 
    Intel = 1  # Jogador 1
    burro = -1  # Jogador 2
    vencedor = None
    caminho = None

    # Reiniciar o tabuleiro e o contador de jogadas
    tabuleiro[:11] = [0] * 11  # Reinicia o tabulero

    # Loop principal do jogo
    while vencedor is None and tabuleiro[0] < 9:

        # Jogada do inteligente
        posicao = JogadorInteligente(tabuleiro, base_de_conhecimento, caminho_base_conhecimento)
        if posicao is not None and 1 <= posicao <= 9:
            tabuleiro[posicao] = Intel
            tabuleiro[0] += 1  # Contador de jogadas
            # Atualiza o ranking para a jogada do jogador inteligente
            atualizar_ranking(base_de_conhecimento, tabuleiro[1:10], posicao, 0)  # 0 para jogada neutra  # 0 para jogada neutra

        # print("\nTabuleiro após jogada do inteligente:")
        # imprimir_tabuleiro()  # Exibir o tabuleiro após a jogada do campeão
        # print("\n")

        # Verificar se há vencedor após a jogada do inteligente
        vencedor = verificar_vencedor()
        if vencedor is not None or tabuleiro[0] >= 9:
            break

        # Jogada do jogador burro
        posicao = jogada_burro()
        while not verificar_validade(posicao):
            posicao = jogada_burro()
        atualizar_ranking(base_de_conhecimento, tabuleiro[1:10], posicao, 0)  # 0 para jogada neutra

        # print("\nTabuleiro após jogada do burro:")
        # imprimir_tabuleiro()  # Exibir o tabuleiro após a jogada do campeão
        # print("\n")

        # Registrar a jogada do burro
        tabuleiro[posicao] = burro
        tabuleiro[0] += 1  # Contador de jogadas
        
        # Verificar vencedor após a jogada do burro
        vencedor = verificar_vencedor()

        if vencedor is not None or tabuleiro[0] >= 9:
            break

    # Atualizar a base de conhecimento com o resultado da partida
    if vencedor == 1:
        # print("Jogador 1 venceu!")
        vitorias_jog1 += 1
    elif vencedor == -1:
        # print("Jogador 1 venceu!")
        vitorias_jog2 += 1
    else:
        empates += 1

    resultado_partida = {
        'tabuleiro': tabuleiro[1:10],
        'vencedor': vencedor,
        'vitorias_jog1': vitorias_jog1,
        'vitorias_jog2': vitorias_jog2,
        'empates': empates
    }
    if _ % 50 == 0:  # Salvar a cada 1000 partidas
        salvar_base_de_conhecimento(base_de_conhecimento, caminho_base_conhecimento)
    resultados_partidas.append(resultado_partida)

# Salvar os resultados das partidas no arquivo CSV
salvar_resultados_csv('resultados_tic_tac_toe.csv', resultados_partidas)

# Salvar a base de conhecimento no arquivo JSON
salvar_base_de_conhecimento(base_de_conhecimento, 'base_de_conhecimento.json')

print("Resultados disponiveis em resultados_tic_tac_toe.csv")