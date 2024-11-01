import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()

def plot_result(jogadas):
    resultados = pd.read_csv("resultados_tic_tac_toe.csv")

    vitorias_jogador1 = resultados['Vitorias Jogador 1']
    vitorias_jogador2 = resultados['Vitorias Jogador 1']
    empates = resultados['Empates']

    plt.plot(vitorias_jogador1, label='Vitórias Jogador 1')
    plt.plot(vitorias_jogador2, label='Vitórias Jogador 2')
    plt.plot(empates, label='Empates')

    plt.plot(vitorias_jogador1, vitorias_jogador2, empates)
    plt.grid()
    plt.ylabel('Numero de Vitórias')
    plt.xlabel('Numéro de Partidas Jogadas')
    plt.legend()
    plt.title('Resultado estatístico das partidas')

    plt.xlim(left=0)
    plt.xlim(right=jogadas)
    plt.ylim(bottom=0)

    plt.show()