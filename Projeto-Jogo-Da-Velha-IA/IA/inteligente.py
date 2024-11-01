import random

def carregar_base_de_conhecimento(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            base_de_conhecimento = {}
            for linha in arquivo:
                linha = linha.strip()  # Remove espaços em branco no início e no final
                if linha:  # Verifica se a linha não está vazia
                    # Divide a linha em partes
                    partes = linha.split(',')
                    jogada = None
                    tabuleiro = None
                    decisao = None
                    ranking = None
                        
                    for parte in partes:
                        parte = parte.strip()
                        if 'Jogada:' in parte:
                            jogada = int(parte.split(':')[1].strip())
                        elif 'Tabuleiro:' in parte:
                            tabuleiro = parte.split(':')[1].strip()
                        elif 'Decisão:' in parte:
                            decisao = int(parte.split(':')[1].strip())
                        elif 'Ranking:' in parte:
                            ranking = int(parte.split(':')[1].strip())
                        
                    # Verifica se todas as partes foram encontradas
                    if jogada is not None and tabuleiro is not None and decisao is not None and ranking is not None:
                        if tabuleiro not in base_de_conhecimento:
                            base_de_conhecimento[tabuleiro] = []
                        base_de_conhecimento[tabuleiro].append({
                           'jogada': jogada,
                            'decisao': decisao,
                            'ranking': ranking
                        })
            print("Base de conhecimento carregada com sucesso.")
            return base_de_conhecimento
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}. Criando nova base de conhecimento.")
        return {}
    except Exception as e:
        print(f"Ocorreu um erro ao carregar a base de conhecimento: {e}")
        return {}

def salvar_base_de_conhecimento(base_de_conhecimento, caminho_arquivo):
    try:
        with open(caminho_arquivo, 'w') as arquivo:
            for estado, jogadas in base_de_conhecimento.items():
                arquivo.write(f"{estado}:")
                for jogada_info in jogadas:
                    arquivo.write(f" {jogada_info['jogada']};{jogada_info['ranking']},")
                arquivo.write("\n")
    except Exception as e:
        print(f"Erro ao salvar a base de conhecimento: {e}")

def consulta_melhor_jogada(base_de_conhecimento, estado):
    estado_str = ' '.join(map(str, estado))  # Converte o estado em uma string
    if estado_str in base_de_conhecimento:
        melhor_jogada = max(base_de_conhecimento[estado_str], key=lambda x: x['ranking'])
        return melhor_jogada['jogada']
    else:
        return None
    
def atualizar_ranking(base_de_conhecimento, tabuleiro, jogada, novo_ranking):
    # Converte a lista de tabuleiro em uma string, se necessário
    if isinstance(tabuleiro, list):
        tabuleiro = ''.join(map(str, tabuleiro))  # Converte a lista em uma string

    # Verifica se o tabuleiro existe na base de conhecimento
    if tabuleiro in base_de_conhecimento:
        for entrada in base_de_conhecimento[tabuleiro]:
            # Verifica se a chave 'jogada' existe na entrada
            if 'jogada' in entrada:
                if entrada['jogada'] == jogada:
                    entrada['ranking'] = novo_ranking
                    return
    else:
        # Se o tabuleiro não existe, cria uma nova entrada
        if tabuleiro not in base_de_conhecimento:
            base_de_conhecimento[tabuleiro] = []
        base_de_conhecimento[tabuleiro].append({'jogada': jogada, 'ranking': novo_ranking})

def JogadorInteligente(tabuleiro, base_de_conhecimento, caminho_arquivo):
    jogada = consulta_melhor_jogada(base_de_conhecimento, tabuleiro[1:10])

    if jogada is None or tabuleiro[jogada] != 0:
        jogadas_disponiveis = [i for i in range(1, 10) if tabuleiro[i] == 0]
        jogada = random.choice(jogadas_disponiveis)
    
    atualizar_ranking(base_de_conhecimento, tabuleiro[1:10], jogada, 0)
    return jogada

# Representação do tabuleiro
tabuleiro = [0] * 15
caminho_base_conhecimento = 'base_de_conhecimento.txt'
base_de_conhecimento = carregar_base_de_conhecimento(caminho_base_conhecimento)