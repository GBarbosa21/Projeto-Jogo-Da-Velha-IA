from Game.tabuleiro import tabuleiro

def Jogada_campeao(tabuleiro, vez):
    if (vez==1):
        for i in range(9):
            if tabuleiro[i] == 0: #se o tabuleiro estiver vazio
                tabuleiro[1]=1 #coloca na posicao 1
            if(tabuleiro[9]==0): #se nao joga na posicao 9
                tabuleiro[9]=1 #joga na 9
            else: #se joga na ponta oposta
                tabuleiro[5]=1 #joga no meio
                if(verificar_possibilidade_de_vencer(tabuleiro, -1)==1):
                    tabuleiro[7]=1 
                    if(tabuleiro[4]==0):
                        tabuleiro[4]=1 #fim de jogo<<<<<<<<<<<<<<<<<<
                    elif(tabuleiro[3]==0):
                        tabuleiro[3]=1 #fim de jogo<<<<<<<<<<<<<<<<<<<<<<<<
                elif(verificar_possibilidade_de_vencer(tabuleiro, -1)==2):
                    tabuleiro[8]=1
                    if(tabuleiro[2]==0):
                       tabuleiro[2]=1 #fim de jogo<<<<<<<<<<<<<<<<<<<<<<<<<<
                    else:
                        tabuleiro[6]=1
                        if(tabuleiro[4]==0):
                            tabuleiro[4]=1 #fim de jogo<<<<<<<<<<<<<<<<<<<<<<<
                        else:
                           tabuleiro[3]=1
                           #VELHA

            if(tabuleiro[5]==0):
                tabuleiro[5]=1#FIM DE JOGO
            elif(verificar_possibilidade_de_vencer(tabuleiro, -1)==1): #se a tabela do meio for risco de derrota
                tabuleiro[4]=1
                if(tabuleiro[7]==0):
                    tabuleiro[7]=1
                else:
                    tabuleiro[3]==1
                    if(tabuleiro[2]==0):
                        tabuleiro[2]=1 #fim de jogo<<<<<<<<<<<<<<<<<<
                    else:
                        tabuleiro[8]=1 #VELHA                      
            elif(verificar_possibilidade_de_vencer(tabuleiro, -1)==3): 
                    tabuleiro[6]=1
                    if(tabuleiro[3]==0):
                        tabuleiro[3]=1 
                        #fim de jogo <<<<<<<<<<<<<<<  
                    else:
                        tabuleiro[7]=1
                        if(tabuleiro[8]==0):
                            tabuleiro[8]=1
                            #fim de jogo <<<<<<<<<<<<<<
                        else:
                            tabuleiro[2]=1
                            #VELHA <<<<<<<<<<<<<<<<<<
            elif(verificar_possibilidade_de_vencer(tabuleiro, -1)==4):
                tabuleiro[2]=1
                if(tabuleiro[3]==0):
                    tabuleiro[3]=1 #fim de jogo<<<<<<<<<<<<
                else:
                    tabuleiro[4]=1
                    if(tabuleiro[7]==0):
                       tabuleiro[7]=1 #fim de jogo<<<<<<<<<<<<<<
                    else:
                       tabuleiro[6]=1 #VELHA
            elif(verificar_possibilidade_de_vencer(tabuleiro, -1)==6):
                tabuleiro[8]=1
                if(tabuleiro[7]==0):
                    tabuleiro[7]=1 #fim de jogo<<<<<<<<<<<<<
                else:
                    tabuleiro[6]=1
                    if(tabuleiro[3]==0):
                        tabuleiro[3]=1 #fim de jogo<<<<<<<<<<
                    else:
                       tabuleiro[4]=1 #VELHA


    else: #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SE FOR A VEZ DO SEGUNDO JOGADOR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


        if(tabuleiro[5]==0):
            tabuleiro[5]=-1
            if(verificar_possibilidade_de_vencer(tabuleiro, 1)==1):
                if(tabuleiro[2]==1): #dois de cima
                    tabuleiro[1]=-1
                    if(tabuleiro[9]==0):
                       tabuleiro[9]=-1 #fim de jogo<<<<<<<<<<<<<
                    else:
                        tabuleiro[6]=-1
                        if(tabuleiro[4]==0):
                            tabuleiro[4]=-1 #fim de jogo<<<<<<<<<<<<<<<<<
                        else:
                           tabuleiro[7]=-1 #VELHA
            elif(tabuleiro[8]==1):
                tabuleiro[7]=-1
                if(tabuleiro[3]==0):
                    tabuleiro[3]=-1 #fim de jogo<<<<<<<<<<<<<<<<<
                else:
                    tabuleiro[1]=-1
                    if(tabuleiro[4]==0):
                        tabuleiro[4]=-1 #fim de jogo<<<<<<<<<<<<<<<<<
                    tabuleiro[6]=-1 #VELHA
                   
            elif(verificar_possibilidade_de_vencer(tabuleiro, 1)==2):
                if(tabuleiro[1]==1): #dois de cima
                    tabuleiro[2]=-1
                    if(tabuleiro[8]==0):
                       tabuleiro[8]=-1 #fim de jogo<<<<<<<<<<<<<<
                    else:
                        tabuleiro[6]=-1
                        if(tabuleiro[4]==0):
                            tabuleiro[4]=-1 #fim de jogo<<<<<<<<<<<<<<<<<
                        else:
                            tabuleiro[7]=-1 #VELHA
                elif(tabuleiro[7]==1):
                    tabuleiro[8]=-1
                    if(tabuleiro[2]==0):
                        tabuleiro[2]=-1
                    else:
                        tabuleiro[6]
                        if(tabuleiro[4]==0):
                            tabuleiro[4]=-1 #fim de jogo<<<<<<<<<<<<<<<<<
                        else:
                            tabuleiro[3]=-1#velha



                
            elif(verificar_possibilidade_de_vencer(tabuleiro, 1)==3):
                if(tabuleiro[2]==1):
                    tabuleiro[3]=-1
                    if(tabuleiro[7]==0):
                       tabuleiro[7]=-1 #fim de jogo<<<<<<<<<<<<<<<<
                    else:
                        tabuleiro[4]=-1
                        if(tabuleiro[6]==0):
                            tabuleiro[6]=-1 #fim de jogo<<<<<<<<<<<<<<<<<<
                        else:
                            tabuleiro[9]=-1 #VELHA
                elif(tabuleiro[9]==1):
                    tabuleiro[7]=-1
                    if(tabuleiro[3]==0):
                        tabuleiro[3]=-1 #fim de jogo<<<<<<<<<<<<<<<<<<
                    else:
                        tabuleiro[6]=-1
                        if(tabuleiro[4]==0):
                            tabuleiro[4]=-1
                        else:
                            tabuleiro[2]=-1                   
            #verificando linhas
            elif(verificar_possibilidade_de_vencer(tabuleiro, 1)==4):
                if(tabuleiro[4]==1):
                    tabuleiro[1]=-1
                    if(tabuleiro[3]==0):
                        tabuleiro[3]=-1 #fim de jogo<<<<<<<<<<<<<<<<<<<<
                    else:
                        tabuleiro[8]=-1
                        if(tabuleiro[2]==0):
                            tabuleiro[2]=-1 #fim de jogo<<<<<<<<<<<<<<<<<<<<<
                        else:
                            tabuleiro[6]=-1
                elif(tabuleiro[6]==1):
                    tabuleiro[3]=-1
                    if(tabuleiro[2]==0):
                        tabuleiro[2]=-1 #fim de jogo<<<<<<<<<<<<<<<<<<<<<<
                    else:
                        tabuleiro[1]=-1 #VELHA
            elif(verificar_possibilidade_de_vencer(tabuleiro, 1)==5):
                if(tabuleiro[1]==1):
                    tabuleiro[4]=-1
                    if(tabuleiro[6]==0):
                        tabuleiro[6]=-1 #fim de jogo<<<<<<<<<<<<<<<<<<<<<<<<<
                    else:
                        tabuleiro[2]=-1
                        if(tabuleiro[8]==0):
                            tabuleiro[8]=-1 #fim de jogo<<<<<<<<<<<<<<<<<<<<<<<<<
                        else:
                            tabuleiro[9]=-1
                elif(tabuleiro[3]==1):
                    tabuleiro[6]=-1
                    if(tabuleiro[4]==0):
                        tabuleiro[4]=-1
                    else:
                        tabuleiro[2]=-1
                        if(tabuleiro[2]==0):
                            tabuleiro[2]=-1
                        else:
                            tabuleiro[1]=-1
            elif(verificar_possibilidade_de_vencer(tabuleiro, 1)==6):
                if(tabuleiro[1]==1):
                    tabuleiro[7] = -1
                    if(tabuleiro[3]==0):
                        tabuleiro[3]=-1#fim de jogo<<<<<<<<<<<<<<<<<<<<
                    else:
                        tabuleiro[2]=-1
                        if(tabuleiro[8]):
                            tabuleiro[8]=-1#fim de jogo<<<<<<<<<<<<<<<<<<<<<
                        else:
                            tabuleiro[9]=-1
                if(tabuleiro[3]==1):
                    tabuleiro[9] = -1
                    if(tabuleiro[1]==0):
                        tabuleiro[1]=-1 #fim de jogo<<<<<<<<<<<<<<
                    else:
                        tabuleiro[2]=-1
                        if(tabuleiro[8]==0):
                            tabuleiro[8]=-1 #fim de jogo<<<<<<<<<<<<<<<<<<<<
                        else:
                            tabuleiro[7]=-1 #velha

def verificar_possibilidade_de_vencer(tabuleiro, jogador):
      # Verificar linhas
  for i in range(0, 9, 3):
    if tabuleiro[i] == 0 and tabuleiro[i+1] == jogador and tabuleiro[i+2] == jogador:
      return 1
    if tabuleiro[i] == jogador and tabuleiro[i+1] == 0 and tabuleiro[i+2] == jogador:
      return 2
    if tabuleiro[i] == jogador and tabuleiro[i+1] == jogador and tabuleiro[i+2] == 0:
      return 3

  # Verificar colunas
  for i in range(3):
    if tabuleiro[i] == 0 and tabuleiro[i+3] == jogador and tabuleiro[i+6] == jogador:
      return 4
    if tabuleiro[i] == jogador and tabuleiro[i+3] == 0 and tabuleiro[i+6] == jogador:
      return 5
    if tabuleiro[i] == jogador and tabuleiro[i+3] == jogador and tabuleiro[i+6] == 0:
      return 6

  # Verificar diagonais
  if tabuleiro[0] == 0 and tabuleiro[4] == jogador and tabuleiro[8] == jogador:
    return 7 #diagonal 5 - 6
  if tabuleiro[0] == jogador and tabuleiro[4] == 0 and tabuleiro[8] == jogador:
    return 8 #diagonal 1 - 8
  if tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == 0:
    return 9
  if tabuleiro[2] == 0 and tabuleiro[4] == jogador and tabuleiro[6] == jogador:
    return 10
  if tabuleiro[2] == jogador and tabuleiro[4] == 0 and tabuleiro[6] == jogador:
    return 11
  if tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == 0:
    return 12

  return False