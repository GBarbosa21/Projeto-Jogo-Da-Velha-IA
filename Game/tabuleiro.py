# Representação do tabuleiro
tabuleiro = [0] * 9  # Inicia com 0 (vazio) para cada posição

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
      posicao = int(input(f"Jogador {jogador}, escolha uma posição (1-9): ")) - 1
      if 0 <= posicao <= 8 and tabuleiro[posicao] == 0:
        return posicao
      else:
        print("Posição inválida. Tente novamente.")
    except ValueError:
      print("Entrada inválida. Digite um número entre 1 e 9.")

# Loop principal do jogo
jogador_atual = 1  # Começa com o jogador 1
vencedor = None
while vencedor is None:
  imprimir_tabuleiro()
  posicao = obter_jogada(jogador_atual)
  tabuleiro[posicao] = jogador_atual
  vencedor = verificar_vencedor()
  jogador_atual = -jogador_atual  # Alterna entre 1 e -1

imprimir_tabuleiro()
if vencedor == 1:
  print("Jogador 1 venceu!")
elif vencedor == -1:
  print("Jogador 2 venceu!")
else:
  print("Empate!")