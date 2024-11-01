from IA.burro import jogada_burro
from IA.campeao import jogada_campeao
from plotagem import plot_result
from Game.tabuleiro import verificar_validade, verificar_vencedor, salvar_resultados_csv, imprimir_tabuleiro
from IA.inteligente import JogadorInteligente, consulta_melhor_jogada, atualizar_ranking, salvar_base_de_conhecimento, carregar_base_de_conhecimento

def mostrar_menu():
    print("=== Menu ===")
    print("1. Burro x Burro")
    print("2. Burro x Campeao")
    print("3. Inteligente x Burro")
    print("4. Sair")
    print("==============")

def obter_numero_de_jogos():
    while True:
        try:
            jogos = int(input("Jogos: "))  # Tenta converter a entrada para um inteiro
            if jogos <= 0:
                print("Por favor, insira um número positivo.")
            else:
                return jogos  # Retorna o número de jogos se for válido
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")


def burro_burro(jogos):
    tabuleiro = [0] * 15
    resultados_partidas = []
    for _ in range(jogos):  # Para jogar 10 rodadas
        burro1 = 1  # Jogador 1
        burro2 = -1 # Jogador 2
        vencedor = None
        jogador_atual = burro1
        
        # Reiniciar apenas as primeiras 11 posições
        tabuleiro[:11] = [0] * 11  # Reinicia o tabuleiro e o contador de jogadas (tabuleiro[0])

        while vencedor is None and tabuleiro[0] < 9:
            
            # Jogada do jogador atual
            posicao = jogada_burro()
            while not verificar_validade(posicao, tabuleiro):
                posicao = jogada_burro()

            # Registrar a jogada
            tabuleiro[posicao] = jogador_atual
            tabuleiro[0] += 1  # Contador de jogadas
            
            # Verificar vencedor
            vencedor = verificar_vencedor(tabuleiro)

            # Alternar jogador
            jogador_atual = burro2 if jogador_atual == burro1 else burro1

        if vencedor == 1:
            tabuleiro[12] += 1  # Atualiza contador de vitórias do jogador 1
        elif vencedor == -1:
            tabuleiro[14] += 1  # Atualiza contador de vitórias do jogador 2
        else:
            tabuleiro[13] += 1  # Atualiza contador de empates

        tabuleiro[10] += 1  # Atualiza contador de partidas jogadas

        try:
            resultado_partida = {
                'tabuleiro': tabuleiro[1:10],  # Somente as posições do tabuleiro (1 a 9)
                'vencedor': vencedor if vencedor is not None else "0",
                'vitorias_jog1': tabuleiro[12],
                'vitorias_jog2': tabuleiro[14],
                'empates': tabuleiro[13]
            }
            resultados_partidas.append(resultado_partida)
        except Exception as e:
            print(f"Erro ao salvar o resultado da partida {tabuleiro[10] + 1}: {e}")
    salvar_resultados_csv('resultados_tic_tac_toe.csv', resultados_partidas)

def burro_campeao(jogos):
    tabuleiro = [0] * 15
    resultados_partidas = []

    for _ in range(jogos):
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
            while not verificar_validade(posicao, tabuleiro):
                posicao = jogada_burro()

            # Registrar a jogada do burro
            tabuleiro[posicao] = burro
            tabuleiro[0] += 1  # Contador de jogadas
            
            # Verificar vencedor após a jogada do burro
            vencedor = verificar_vencedor(tabuleiro)
            

            # Jogada do campeão
            posicao, caminho = jogada_campeao(tabuleiro, campeao, caminho)
            if posicao is not None and 1 <= posicao <= 9:
                tabuleiro[posicao] = campeao
                tabuleiro[0] += 1
            else:
                print("Erro: Posição inválida retornada pela função jogada_campeao.")
            vencedor = verificar_vencedor(tabuleiro)
            if vencedor is not None or tabuleiro[0] >= 9:
                break         

        if vencedor == 1:
            tabuleiro[12] += 1  # contador de vitórias do jogador 1
        elif vencedor == -1:
            tabuleiro[14] += 1  #contador de vitórias do jogador 2
        else:
            tabuleiro[13] += 1  #contador de empates

        tabuleiro[10] += 1  #contador de partidas jogadas

        resultado_partida = {
            'tabuleiro': tabuleiro[1:10],  # Somente as posições do tabuleiro (1 a 9)
            'vencedor': vencedor if vencedor is not None else "0",
            'vitorias_jog1': tabuleiro[12],
            'vitorias_jog2': tabuleiro[14],
            'empates': tabuleiro[13]
        }
        resultados_partidas.append(resultado_partida)

    # Salvar os resultados em um arquivo CSV
    salvar_resultados_csv('resultados_tic_tac_toe.csv', resultados_partidas)

    print("Resultados salvos em 'resultados_tic_tac_toe.csv'.")

def campeao_burro(jogos):
    tabuleiro = [0] * 15
    resultados_partidas = []

    for _ in range(jogos):
        burro = -1  # Jogador 2
        campeao = 1  # Jogador 1
        vencedor = None
        caminho = None

        # Reiniciar o tabuleiro e o contador de jogadas
        tabuleiro[:11] = [0] * 11  # Reinicia todas as posições do tabuleiro

        # Loop principal do jogo
        while vencedor is None and tabuleiro[0] < 9:
            # Jogada do campeão
            # Jogada do campeão
            posicao, caminho = jogada_campeao(tabuleiro, campeao, caminho)
            if posicao is not None and 1 <= posicao <= 9:
                tabuleiro[posicao] = campeao
                tabuleiro[0] += 1
            else:
                print("Erro: Posição inválida retornada pela função jogada_campeao.")
            vencedor = verificar_vencedor(tabuleiro)
            if vencedor is not None or tabuleiro[0] >= 9:
                break

            # Jogada do jogador burro
            posicao = jogada_burro()
            while not verificar_validade(posicao, tabuleiro):
                posicao = jogada_burro()

            # Registrar a jogada do burro
            tabuleiro[posicao] = burro
            tabuleiro[0] += 1  # Contador de jogadas
            
            # Verificar vencedor após a jogada do burro
            vencedor = verificar_vencedor(tabuleiro)
            if vencedor is not None or tabuleiro[0] >= 9:
                break      

        if vencedor == 1:
            tabuleiro[12] += 1  # Atualiza contador de vitórias do jogador 1
        elif vencedor == -1:
            tabuleiro[14] += 1  # Atualiza contador de vitórias do jogador 2
        else:
            tabuleiro[13] += 1  # Atualiza contador de empates

        tabuleiro[10] += 1  # Atualiza contador de partidas jogadas

        resultado_partida = {
            'tabuleiro': tabuleiro[1:10],  # Somente as posições do tabuleiro (1 a 9)
            'vencedor': vencedor if vencedor is not None else "0",
            'vitorias_jog1': tabuleiro[12],
            'vitorias_jog2': tabuleiro[14],
            'empates': tabuleiro[13]
        }
        resultados_partidas.append(resultado_partida)

    # Salvar os resultados em um arquivo CSV
    salvar_resultados_csv('resultados_tic_tac_toe.csv', resultados_partidas)

    print("Resultados salvos em 'resultados_tic_tac_toe.csv'.")

def inteligente_burro(jogos):

    caminho_base_conhecimento = 'base_de_conhecimento.txt'
    base_de_conhecimento = carregar_base_de_conhecimento(caminho_base_conhecimento) or {}
    # Exemplo de uso
    jogadas_usadas = []
    resultados_partidas = []
    vitorias_jog1 = 0
    vitorias_jog2 = 0
    empates = 0

    for _ in range(jogos):
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
                jogadas_usadas = {
                    'tabuleiro' : tabuleiro[1:10],
                    'posicao' : posicao,
                }
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

def main():
    base_de_conhecimento = {}  # Inicializa a base de conhecimento
    while True:
        mostrar_menu()
        try:
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                print("\nDefina o número de jogos.")
                jogos = obter_numero_de_jogos()  # Chama a função para obter o número de jogos
                burro_burro(jogos)
                plot_result(jogos)

            elif opcao == '2':
                print("\nDefina o número de jogos.")
                jogos = obter_numero_de_jogos()  # Chama a função para obter o número de jogos

                print("Ordem dos jogadores:")
                print("1 - Campeão x Burro")
                print("2 - Burro x Campeão")
                ordem = input("Entre com a ordem: ")

                if ordem == '1':
                    campeao_burro(jogos)
                    plot_result(jogos)
                elif ordem == '2':
                    burro_campeao(jogos)
                    plot_result(jogos)
                else:
                    print("Escolha inválida!")
            elif opcao == '3':
                print("\nDefina o número de jogos.")
                jogos = obter_numero_de_jogos()  # Chama a função para obter o número de jogos
                inteligente_burro(jogos)
                plot_result(jogos)
            elif opcao == '4':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}. Tente novamente.")
if __name__ == "__main__":
    main()
