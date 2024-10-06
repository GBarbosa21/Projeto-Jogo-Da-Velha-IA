''' # Loop principal do jogo BURRO x BURRO
for _ in range(100000):  # Para jogar 10 rodadas
    burro1 = 1  # Jogador 1
    burro2 = -1 # Jogador 2
    vencedor = None
    jogador_atual = burro1
    
    # Reiniciar apenas as primeiras 11 posições
    tabuleiro[:11] = [0] * 11  # Reinicia o tabuleiro e o contador de jogadas (tabuleiro[0])

    while vencedor is None and tabuleiro[0] < 9:
        print("\n")
        imprimir_tabuleiro()
        print("\n")
        
        # Jogada do jogador atual
        posicao = jogada_burro()
        while not verificar_validade(posicao):
            posicao = jogada_burro()

        # Registrar a jogada
        tabuleiro[posicao] = jogador_atual
        tabuleiro[0] += 1  # Contador de jogadas
        
        # Verificar vencedor
        vencedor = verificar_vencedor()

        # Alternar jogador
        jogador_atual = burro2 if jogador_atual == burro1 else burro1

    imprimir_tabuleiro()
    print("\n")

    if vencedor == 1:
        print("Jogador 1 venceu!")
        tabuleiro[12] += 1  # Atualiza contador de vitórias do jogador 1
    elif vencedor == -1:
        print("Jogador 2 venceu!")
        tabuleiro[14] += 1  # Atualiza contador de vitórias do jogador 2
    else:
        print("Empate!")
        tabuleiro[13] += 1  # Atualiza contador de empates

    tabuleiro[10] += 1  # Atualiza contador de partidas jogadas

    try:
        resultado_partida = {
            'tabuleiro': tabuleiro[1:10],  # Somente as posições do tabuleiro (1 a 9)
            'vencedor': vencedor if vencedor is not None else "Empate",
            'vitorias_jog1': tabuleiro[12],
            'vitorias_jog2': tabuleiro[14],
            'empates': tabuleiro[13]
        }
        resultados_partidas.append(resultado_partida)
    except Exception as e:
        print(f"Erro ao salvar o resultado da partida {tabuleiro[10] + 1}: {e}") '''