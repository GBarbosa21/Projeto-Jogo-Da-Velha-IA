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
        burro = -1
        if tabuleiro[1] == 0:  # Começa pela ponta
            return 1, caminho
        if tabuleiro[9] == 0:  # Se a ponta oposta estiver livre
            return 9, caminho
        elif tabuleiro[5] == 0:  # Caso o meio esteja livre e a ponta ocupada
            caminho=6
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
        burro = 1

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
            elif tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[7]==0:
                return 7, caminho
            else:
                return 8, caminho
            
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
            if tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
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
            elif tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro [7]==0:
                return 7, caminho
            else:
                return 9, caminho

        if caminho == 87:
            if tabuleiro[4]==0:
                return 4, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            else:
                return 7, caminho
            
        if caminho == 88:
            if tabuleiro[1]==0:
                return 1, caminho
            elif tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[7]==1:
                if tabuleiro[4]==0:
                    return 4, caminho
                else:
                    return 2, caminho
            elif tabuleiro[3]==0:
                return 3, caminho
            else:
                return 2, caminho

        if caminho == 89:
            if tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            else:
                return 2, caminho

        if caminho == 90:
            if tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            else:
                return 4, caminho

        if caminho == 91:
            if tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[3]==0:
                return 3, caminho
            else:
                return 9, caminho

        if caminho == 92:
            if tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            else:
                return 4, caminho

        if caminho == 93:
            if tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[7]==0:
                return 7, caminho
            else:
                return 9, caminho
            
        if caminho == 94:
            if tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            else:
                return 4, caminho

        if caminho == 95:
            if tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            else:
                return 4, caminho

        if caminho == 96:
            if tabuleiro[8]==0:
                return 8, caminho
            elif tabuleiro[7]==0:
                return 7, caminho
            elif tabuleiro[3]==0:
                return 3, caminho
            else:
                return 6, caminho
            
        if caminho == 97:
            if tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            else:
                return 2, caminho

        if caminho == 98:
            if tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[7]==0:
                return 7, caminho
            else:
                return 9, caminho
            
        if caminho == 99:
            if tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            else:
                return 3, caminho

        if caminho == 110:
            if tabuleiro[6]==0:
                return 6, caminho
            elif tabuleiro[9]==0:
                return 9, caminho
            elif tabuleiro[1]==0:
                return 1, caminho
            else:
                return 3, caminho

        if caminho == 100:
            if tabuleiro[2]==1:
                if verificar_possibilidade_de_vencer(tabuleiro, 1)==1:
                    caminho = 64
                    return 1, caminho
                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==3:
                    caminho = 65
                    return 3, caminho
                elif tabuleiro[7]==1:
                    caminho = 99
                    return 4, caminho
                elif tabuleiro[8]==1:
                    caminho = 110
                    return 4, caminho
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
                    
                elif tabuleiro[1]==1:
                    caminho = 86
                    return 4, caminho
                
                elif tabuleiro[3]==1:
                    caminho = 87
                    return 6, caminho
                
                elif tabuleiro[6]==1:
                    caminho = 88
                    return 9, caminho

                elif tabuleiro[4]==1:
                    caminho = 89
                    return 7, caminho

                else:
                    caminho = 84
                    return 3, caminho
            
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
                elif tabuleiro[4]==1:
                    caminho = 81
                    return 2, caminho
                elif tabuleiro[1]==1:
                    caminho = 91
                    return 2, caminho
                elif tabuleiro[7]==1:
                    caminho = 92
                    return 2, caminho

        
        if caminho == 101:
            if verificar_possibilidade_de_vencer(tabuleiro, 1)==1:
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
            elif tabuleiro[1]==1:
                caminho = 93
                return 4, caminho
            else:
                caminho = 7
                return 3, caminho


        if caminho == 102:
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
                elif tabuleiro[1]==1 and tabuleiro[9]==1:
                    caminho = 83
                    return 2, caminho
                elif tabuleiro[3]==1 and tabuleiro[8]==1:
                    caminho = 97
                    return 4, caminho
                elif tabuleiro[1]==1 and tabuleiro[8]==1:
                    caminho = 98
                    return 4, caminho
                else:
                    caminho = 94
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
                    
                elif verificar_possibilidade_de_vencer(tabuleiro, 1)==4:
                    if tabuleiro[7]==1:
                        caminho = 62
                        return 1, caminho
                    else:
                        caminho = 63
                        return 3, caminho
                
                else:
                    if tabuleiro[6]==1 and tabuleiro[7]==1:
                        caminho = 90
                        return 2, caminho
                    elif tabuleiro[7]==1 and tabuleiro[3]==1:
                        caminho = 95
                        return 2, caminho
                    elif tabuleiro[9]==1 and tabuleiro[1]==1:
                        caminho = 96
                        return 2, caminho
                    else:
                        caminho = 80
                        return 4, caminho

#CAMINHOS DE SEGUNDO NIVEL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if caminho == 10:
            if verificar_possibilidade_de_vencer(tabuleiro, 1)==10:
                return 3, caminho
            elif verificar_possibilidade_de_vencer(tabuleiro, 1)==12:
                return 7, caminho
            else:
                return 9, caminho

        if caminho == 11:
            if tabuleiro[3]==0:
                return 3, caminho
            elif tabuleiro[7]==0:
                return 7, caminho
            else: 
                return 9, caminho
        
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
            caminho = 101
            if tabuleiro[1] == 0:
                return 1, caminho
                    
        elif tabuleiro[1] or tabuleiro[3] or tabuleiro[7] or tabuleiro[9] == 1 and tabuleiro[8]==0: #se jogou nas pontas
            caminho = 102
            if tabuleiro[5]==0:
                return 5, caminho

        elif tabuleiro[2] or tabuleiro[4] or tabuleiro[6] or tabuleiro [8] == 1: #se jogou no cruscifixo
            caminho = 100
            if tabuleiro[5]==0:
                return 5, caminho
