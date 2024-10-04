from IA.burro import jogada_burro

# Representação do tabuleiro
tabuleiro = [0] * 9  # Inicia com 0 (vazio) para cada posição 

# 0 - jogadas / 1-9 - tabuleiro / 10 - vencedor (campeao) / 11 - velha / 12 - vitorias (burro)

# Função para imprimir o tabuleiro
def imprimir_tabuleiro():
  for i in range(0, 9, 3):
    print(f"{tabuleiro[i]} | {tabuleiro[i+1]} | {tabuleiro[i+2]}")
    if i < 6:
      print("---------")

# Função para verificar se há um vencedor
def verificar_vencedor():
  # Verificar linhas
  for i in range(0, 9, 3):
    if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] and tabuleiro[i] != 0:
      return tabuleiro[i]

  # Verificar colunas
  for i in range(3):
    if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] and tabuleiro[i] != 0:
      return tabuleiro[i]

  # Verificar diagonais
  if (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] and tabuleiro[0] != 0) or \
     (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] and tabuleiro[2] != 0):
    return tabuleiro[4]

  return None  # Nenhum vencedor ainda

# Função para obter a jogada do jogador
def obter_jogada(jogador):
  while True:
    try:
      posicao = int(input(f"Escolha uma posição (1-9): ")) - 1
      if 0 <= posicao <= 8 and tabuleiro[posicao] == 0:
        return posicao
      else:
        print("Posição inválida. Tente novamente.")
    except ValueError:
      print("Entrada inválida. Digite um número entre 1 e 9.")

def verificar_validade(jogada):
    if tabuleiro[jogada] == 0:
      return 0
    else:
          return 1

# Loop principal do jogo
jogador_atual = 1  # Começa com o jogador
jogador_burro = -1
vencedor = None
while vencedor is None:
  imprimir_tabuleiro()
  posicao = obter_jogada(jogador_atual)
  tabuleiro[posicao] = jogador_atual
  vencedor = verificar_vencedor()
  jogador_atual = jogador_burro
  while(valido!=0):
    posicao = jogada_burro()
    valido = verificar_validade(posicao)
  tabuleiro[posicao] = jogador_atual
  vencedor = verificar_vencedor()
  jogador_atual = 1

imprimir_tabuleiro()
if vencedor == 1:
  print("Jogador 1 venceu!")
elif vencedor == -1:
  print("Jogador 2 venceu!")
else:
  print("Empate!")
