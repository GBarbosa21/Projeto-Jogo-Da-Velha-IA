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

# JOGADOR BURRO ESCOLHE UMA JOGADA ALEATÓRIA (apenas entre 1 e 9)
def jogada_burro():
    return random.choice([i for i in range(1, 10) if tabuleiro[i] == 0])

def verificar_possibilidade_de_vencer(tabuleiro, jogador):
        # Verificar linhas
        for i in range(1, 10, 3):
            if tabuleiro[i] == 0 and tabuleiro[i + 1] == jogador and tabuleiro[i + 2] == jogador:
                return 1
            if tabuleiro[i] == jogador and tabuleiro[i + 1] == 0 and tabuleiro[i + 2] == jogador:
                return 2
            if tabuleiro[i] == jogador and tabuleiro[i + 1] == jogador and tabuleiro[i + 2] == 0:
                return 3

        # Verificar colunas
        for i in range(1, 4):
            if tabuleiro[i] == 0 and tabuleiro[i + 3] == jogador and tabuleiro[i + 6] == jogador:
                return 4
            if tabuleiro[i] == jogador and tabuleiro[i + 3] == 0 and tabuleiro[i + 6] == jogador:
                return 5
            if tabuleiro[i] == jogador and tabuleiro[i + 3] == jogador and tabuleiro[i + 6] == 0:
                return 6

        # Verificar diagonais
        if tabuleiro[1] == 0 and tabuleiro[5] == jogador and tabuleiro[9] == jogador:
            return 7  # diagonal 1 - 9
        if tabuleiro[1] == jogador and tabuleiro[5] == 0 and tabuleiro[9] == jogador:
            return 8  # diagonal 5 - 9
        if tabuleiro[1] == jogador and tabuleiro[5] == jogador and tabuleiro[9] == 0:
            return 9
        if tabuleiro[3] == 0 and tabuleiro[5] == jogador and tabuleiro[7] == jogador:
            return 10
        if tabuleiro[3] == jogador and tabuleiro[5] == 0 and tabuleiro[7] == jogador:
            return 11
        if tabuleiro[3] == jogador and tabuleiro[5] == jogador and tabuleiro[7] == 0:
            return 12

        return 0

def jogada_campeao(tabuleiro, vez, caminho):
    global caminho_global
    caminho_global = caminho
    if vez==1:
        print(f"Caminho : {caminho}")
        if tabuleiro[1] == 0:  # Começa pela ponta
            return 1, caminho
        if tabuleiro[9] == 0:  # Se a ponta oposta estiver livre
            return 9, caminho
        elif tabuleiro[5] == 0:  # Caso o meio esteja livre e a ponta ocupada
            caminho=6
            print(f"Caminho : {caminho}")
            return 5, caminho
            
        if caminho == 6:
            if(verificar_possibilidade_de_vencer(tabuleiro, -1)==1):
                if(tabuleiro[8]==-1):
                    caminho = 30
                    return 7, caminho
            
            elif(tabuleiro[7] and tabuleiro[9] == burro):
                caminho = 31
                return 8, caminho

            elif(verificar_possibilidade_de_vencer(tabuleiro, -1)==4):
                caminho = 32
                return 3, caminho
            
            elif(verificar_possibilidade_de_vencer(tabuleiro, -1)):
                caminho = 33
                return 6, caminho

        if verificar_possibilidade_de_vencer(tabuleiro,-1) == 0:
            if tabuleiro[4] == burro:
                caminho = 34
                return 3, caminho
            else:
                caminho = 35
                return 7, caminho

        if caminho==34:
            if(tabuleiro[2]==0):
                return 2, caminho
            else:
                return 7, caminho

        if caminho==35:
            if(tabuleiro[4]==0):
                return 4, caminho
            else:
                return 3, caminho

        if caminho == 30:
            if(tabuleiro[3]==0):
                return 3, caminho
            else:
                return 4, caminho

        if caminho == 31:
            if(tabuleiro[8]==0):
                return 8, caminho
            else:
                caminho == 34
                return 2, caminho
        
        if caminho == 34:
            if(tabuleiro[6]==0):
                return 6, caminho
            else:
                return 4, caminho

        if caminho == 32:
            if(tabuleiro[2]==0):
                return 2, caminho
            else:
                return 7, caminho

        if caminho == 33:
            if (tabuleiro[4]==0):
                return 4, caminho
            else:
                caminho == 35
                return 2, caminho

        if caminho == 35:
            if(tabuleiro[8]==0):
                return 8, caminho
            else:
                return 7, caminho

        if caminho== 1:
            if (tabuleiro[7]==0):
                return 7, caminho #fim de jogo
            elif (tabuleiro[3]==0):
                return 3, caminho
            elif(tabuleiro[2]==0):
                return 2, caminho #fim de jogo
            else:
                return 8, caminho #fim de jogo VELHA

        if (caminho==3):
            if(tabuleiro[3]==0):
                return 3, caminho
            elif(tabuleiro[7]==0):
                caminho = 5
                return 7, caminho
            
        if (caminho == 5):
            if(tabuleiro[8]==0):
                return 8, caminho
            else:
                return 2, caminho
            
        if caminho == 2:
            if (tabuleiro[3]==0):
                return 3, caminho #fim do jogo
            elif (tabuleiro[7]==0):
                return 7, caminho
            elif(tabuleiro[8]==0):
                return 8, caminho #fim do jogo
            else:
                return 2, caminho #fim do jogo velha
            
        if caminho == 4:
            if(tabuleiro[3]==0):
                return 3, caminho
            elif (tabuleiro[7]==0):
                return 7, caminho
            elif (tabuleiro[4]==0):
                return 4, caminho
            else:
                return 6, caminho
            
        if caminho == 7:
            if(tabuleiro[7]==0):
                return 7, caminho
            else:
                caminho = 8
                return 3, caminho
            
        if caminho == 8:
            if(tabuleiro[6]==0):
                return 6, caminho
            else:
                return 4, caminho

        if caminho==3:
            if(tabuleiro[2]==0):
                return 2, caminho
            else:
                return 6, caminho
            
        if caminho==12:
            if(tabuleiro[4]==0):
                return 4, caminho
            else:
                return 8, caminho
            
        if caminho==25:
            p = 0
            if(tabuleiro[7]==0):
                return 7, caminho
            elif(tabuleiro[2]==0):
                return 2, caminho
            while(tabuleiro[p]!=0):
                p = p + 1
                return p, caminho

        if caminho==26:
            if(tabuleiro[4]==0):
                return 4, caminho
            else:
                return 3, caminho

        if tabuleiro[5] == 0: #tenta ganhar no meio
           return 5
        elif verificar_possibilidade_de_vencer(tabuleiro, -1) == 1: # 0 / x / x
            if(tabuleiro[5]==-1 and tabuleiro[6]==-1):
                caminho = 1
                if tabuleiro[4]==0:
                    return 4, caminho
            if (tabuleiro[8] and tabuleiro[9]== burro):
                caminho = 26
                return 7, caminho
        
        elif verificar_possibilidade_de_vencer(tabuleiro, -1) == 3: # x / x / 0
           if(tabuleiro[5]==-1 and tabuleiro[4]==-1):
                caminho = 2
                if (tabuleiro[4]==0):
                   return 4, caminho
                else:
                    caminho = 3
                    return 6, caminho
                
        elif verificar_possibilidade_de_vencer(tabuleiro, -1) == 4:
                caminho = 4
                if(tabuleiro[5] and tabuleiro[8]== -1):
                    return 2, caminho
            
        elif verificar_possibilidade_de_vencer(tabuleiro, -1) == 6:
            caminho = 7
            return 8, caminho
        

        elif verificar_possibilidade_de_vencer(tabuleiro, -1) == 10:
            caminho = 10
            return 3, caminho

        elif verificar_possibilidade_de_vencer(tabuleiro, -1) == 12:
            caminho = 12
            return 7, caminho

        elif verificar_possibilidade_de_vencer(tabuleiro, -1) ==0:
            caminho == 25
            return 3, caminho

    else: #é o segundo jogador

        #caminhos
        if caminho == 1:
            if tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[2]==0:
                return 2, caminho
            else:
                return 8, caminho

        if caminho == 2:
            if verificar_possibilidade_de_vencer(tabuleiro, 1)==6:
                caminho = 10 #caminho de segundo nivel 10-20
                return 8, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1)== 4:
                caminho = 11
                return 2, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1)== 12:
                caminho = 12
                return 7, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1) == 10:
                caminho = 13
                return 3, caminho
            else:
                caminho = 14
                return 3, caminho

        if caminho == 3:
            if tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[4]==0:
                return 4, caminho
            else:
                return 6, caminho
        
        if caminho == 4:
            if verificar_possibilidade_de_vencer(tabuleiro, 1)==1:
                caminho = 15
                return 4, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1)==3:
                caminho = 16
                return 6, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1)==12:
                caminho = 17
                return 7, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1)==10:
                caminho = 18
                return 3, caminho
            else:
                caminho = 19
                return 7, caminho

        if caminho == 5:
            if tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[6]==0:
                return 6, caminho
            else:
                return 4, caminho
        
        if caminho == 6:
            if tabuleiro[4]==0:
                return 4, caminho
            elif tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            else:
                return 2, caminho

        if caminho == 7:
            if tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[4]==0:
                return 4, caminho
            elif tabuleiro[4]==1:
                return 6, caminho
            else:
                return 7, caminho

        if caminho == 50:
            if tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[4]==0:
                return 4, caminho
            elif tabuleiro[6]==0:
                return 6, caminho
            else:
                return 8, caminho

        if caminho == 51:
            if tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[4]==0:
                return 4, caminho
            else:
                return 9, caminho

        if caminho == 52:
            if tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[4]==0:
                return 4, caminho
            else:
                return 7, caminho
        
        if caminho == 53:
            if tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[2]==1 and tabuleiro[3]==0:
                caminho = 20
                return 3, caminho
            elif tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            else:
                return 9, caminho
            
        if caminho == 54:
            if tabuleiro[4]==0:
                return 4, caminho
            elif tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            else:
                return 1, caminho

        if caminho == 55:
            if tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            else:
                return 6, caminho

        if caminho == 56:
            if tabuleiro[1]==0:
                return 1, caminho
            elif tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            else:
                return 4, caminho

        if caminho==57:
            if tabuleiro[1]==0:
                return 1, caminho
            elif tabuleiro[4]==0:
                return 4, caminho
            elif tabuleiro[6]==0:
                return 6, caminho
            else:
                return 2, caminho
        
        if caminho==58:
            if tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[4]==0:
                return 4, caminho
            elif tabuleiro[6]==0:
                return 6, caminho
            else:
                return 3, caminho

        if caminho==59:
            if tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[4]==0:
                return 4, caminho
            else:
                return 2, caminho
            
        if caminho==60:
            if tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            else:
                return 9, caminho

        if caminho == 61:
            if tabuleiro[4]==0:
                return 4, caminho
            elif tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            else:
                return 7, caminho

        if caminho==62:
            if tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[2]==0:
                return 2, caminho
            else:
                return 3, caminho

        if caminho == 63:
            if tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[2]==0:
                return 2, caminho
            else:
                return 1, caminho
        
        if caminho == 64:
            if tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[4]==0:
                return 4, caminho
            else:
                return 7, caminho

        if caminho == 65:
            if tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[4]==0:
                return 4, caminho
            elif tabuleiro[6]==0:
                return 6, caminho
            else:
                return 8, caminho

        if caminho == 66:
            if tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[4]==0:
                return 4, caminho
            else:
                return 2, caminho

        if caminho == 67:
            if tabuleiro[1]==0:
                return 1, caminho
            elif tabuleiro[4]==0:
                return 4, caminho
            elif tabuleiro[6]==0:
                return 6, caminho
            else: 
                return 3, caminho

        if caminho == 68:
            if tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[2]==0:
                return 2, caminho
            else:
                return 3, caminho

        if caminho == 69:
            if tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            else:
                return 9, caminho

        if caminho == 70:
            if tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[2]==0:
                return 2, caminho
            else:
                return 1, caminho

        if caminho == 71:
            if tabuleiro[1]==0:
                return 1, caminho
            elif tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            else:
                return 7, caminho
            
        if caminho == 80:
            if tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            elif tabuleiro[1] ==-1 and tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            else:
                return 3, caminho
            
        if caminho == 81:
            if tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[3]==0:
                return 3, caminho
            else:
                return 9, caminho

        if caminho == 82:
            if tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            else:
                return 3, caminho
            
        if caminho ==83:
            if tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[3]==0:
                return 3, caminho
            else:
                return 6, caminho
            
        if caminho == 84:
            if tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[3]==0:
                return 3, caminho
            else:
                return 6, caminho
            
        if caminho == 85:
            if tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            else:
                return 8, caminho

        if caminho == 86:
            if tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            else:
                return 3, caminho

        if caminho == 87:
            if tabuleiro[4]==0:
                return 4, caminho
            elif tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[7]==0:
                return 7, caminho
            else:
                return 1, caminho

        if caminho == 88:
            if tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            else:
                return 9, caminho

#CAMINHOS DE SEGUNDO NIVEL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if caminho == 10:
            if verificar_possibilidade_de_vencer(tabuleiro, 1)==10:
                return 3, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1)==12:
                return 7, caminho

        if caminho == 11:
            if tabuleiro[3]==0:
                return 3, caminho
            else:
                return 6, caminho
        
        if caminho == 12:
            if tabuleiro[9]==1:
                return 8, caminho
            elif tabuleiro[2]==1:
                return 8, caminho
            else:
                return 2, caminho

        if caminho == 13:
            if tabuleiro[2]==0:
                return 2, caminho
            else:
                return 9, caminho   

        if caminho == 14:
            if tabuleiro[2]==0:
                return 2, caminho
            else:
                return 8, caminho

        if caminho == 15:
            if tabuleiro[7]==0:
                return 7, caminho
            else:
                return 3, caminho

        if caminho == 16:
            if tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[3]==0:
                return 3, caminho
            else:
                return 9, caminho
        
        if caminho == 17:
            if tabuleiro[4]==0:
                return 4, caminho
            else:
                return 6, caminho
        
        if caminho == 18:
            if tabuleiro[2]==0:
                return 2, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            else:
                return 4, caminho

        if caminho == 19:
            if tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[4]==0:
                return 4, caminho
            elif tabuleiro[7]==0:
                return 7, caminho
            else:
                return 6, caminho

        if caminho == 20:
            if tabuleiro[8]==0:
                return 8, caminho
            else:
                return 9, caminho


        #verifica onde o primeiro jogador jogou
        if tabuleiro[5]==1: #se jogou no meio
            if tabuleiro[1] == 0:
                return 1, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1)==1:
                caminho = 1
                return 4, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1)==3:
                caminho = 2
                return 6, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1)==4:
                caminho = 3
                return 2, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1)==6:
                caminho = 4
                return 8, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1)==10:
                caminho = 5
                return 3, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1)==12:
                caminho=6
                return 7, caminho
            else:
                caminho = 7
                return 3, caminho
                    

        elif tabuleiro[1] or tabuleiro[3] or tabuleiro[7] or tabuleiro[9] == 1: #se jogou nas pontas
            if tabuleiro[5]==0:
                return 5, caminho
            if tabuleiro[1] or tabuleiro[3] == 1:
                if verificar_possibilidade_de_vencer(tabuleiro, 1)==3:
                    caminho = 50
                    return 3, caminho
                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==2:
                    caminho = 51
                    return 2, caminho
                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==1:
                    caminho = 52
                    return 1, caminho
                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==5:
                    if tabuleiro[1]==1:
                        caminho = 53
                        return 4, caminho
                    else:
                        caminho == 54
                        return 6, caminho

                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==6:
                    if tabuleiro[1]==1:
                        caminho = 55
                        return 7, caminho
                    else:
                        caminho == 56
                        return 9, caminho
                else:
                    caminho = 83
                    return 2, caminho

            else:
                if verificar_possibilidade_de_vencer(tabuleiro, 1)==3:
                    caminho = 57
                    return 9, caminho
                
                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==2:
                    caminho = 58
                    return 8, caminho
                
                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==1:
                    caminho = 59
                    return 7, caminho

                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==5:
                    if tabuleiro[7]==1:
                        caminho = 60
                        return 4, caminho
                    else:
                        caminho = 61
                        return 6, caminho

                elif tabuleiro[7]==1:
                    if tabuleiro[2]==1:
                        caminho = 86
                        return 4, caminho
                    else:
                        caminho = 88
                        return 8, caminho

                elif tabuleiro[9]==1:
                    caminho = 87
                    return 6, caminho

                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==4:
                    if tabuleiro[7]==1:
                        caminho = 62
                        return 1, caminho
                    else:
                        caminho = 63
                        return 3, caminho
                
                else: 
                    caminho = 80
                    return 4, caminho

        elif tabuleiro[2] or tabuleiro[4] or tabuleiro[6] or tabuleiro [8] == 1: #se jogou no cruscifixo
            if tabuleiro[5]==0:
                return 5, caminho
            if tabuleiro[2]==1:
                if verificar_possibilidade_de_vencer(tabuleiro, 1)==1:
                    caminho = 64
                    return 1, caminho
                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==3:
                    caminho = 65
                    return 3, caminho
                
                else:
                    caminho = 85
                    return 3, caminho

            elif tabuleiro[8]==1:
                if verificar_possibilidade_de_vencer(tabuleiro, 1)==1:
                    caminho = 66
                    return 7, caminho

                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==3:
                    caminho = 67
                    return 9, caminho
                
                else:
                    caminho = 84
                    return 8, caminho
            
            elif tabuleiro[4]==1:
                if verificar_possibilidade_de_vencer(tabuleiro, 1)==4:
                    caminho = 68
                    return 1, caminho
                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==6:
                    caminho = 69
                    return 7, caminho
                else:
                    caminho = 82
                    return 2, caminho
                
            elif tabuleiro[6]==1:
                if verificar_possibilidade_de_vencer(tabuleiro, 1)==4:
                    caminho = 70
                    return 3, caminho
                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==6:
                    caminho = 71
                    return 9, caminho
                else:
                    caminho = 81
                    return 2, caminho

        print(f"Posição de jogada: {posicao}")
        print(f"Caminho após verificar possibilidade: {caminho}")

resultados_partidas = []

for _ in range(100):  # Para jogar X rodadas
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
        print("Jogador 1 venceu!")
        break
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