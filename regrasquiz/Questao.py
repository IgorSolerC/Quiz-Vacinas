import time

from constants import TextoQuestoes

respostasPossiveis = ["A", "B", "C", "D", "E"]
respostasComputadas = []
respostasCorretas = []
respostasPontuacao = []
numQuestao = 0
totalPontos = 0


def criaQuestao(valor, correta, pergunta, explicacaoA, explicacaoB="0", explicacaoC="0", explicacaoD="0",
                explicacaoE="0"):
    global numQuestao
    respostasPontuacao.append(valor)
    respostasCorretas.append(correta)
    print(pergunta)
    while True:
        resposta = input("\nResposta: ").upper()
        if resposta not in respostasPossiveis:
            print("Resposta inválida")
            continue
        else:
            if resposta == respostasCorretas[numQuestao]:
                print("\nCorreto!")
                time.sleep(1)
            else:
                print("\nIncorreto!")
                time.sleep(1)
                if explicacaoB == "0":
                    print(explicacaoA)
                elif resposta == "A":
                    print(explicacaoA)
                elif resposta == "B":
                    print(explicacaoB)
                elif resposta == "C":
                    print(explicacaoC)
                elif resposta == "D":
                    print(explicacaoD)
                elif resposta == "E":
                    print(explicacaoE)
                input("\n Aperte 'ENTER' para prosseguir.")
            break
    respostasComputadas.append(resposta)
    numQuestao += 1


def explicaQuestoes():
    criaQuestao(TextoQuestoes.Q1_VALOR, TextoQuestoes.Q1_CORRETA,
                TextoQuestoes.Q1_PERGUNTA, TextoQuestoes.Q1_EXPLICACAO)
    criaQuestao(TextoQuestoes.Q1_VALOR, TextoQuestoes.Q2_CORRETA,
                TextoQuestoes.Q2_PERGUNTA, TextoQuestoes.Q2_EXPLICACAO)
    criaQuestao(TextoQuestoes.Q3_VALOR, TextoQuestoes.Q3_CORRETA,
                TextoQuestoes.Q3_PERGUNTA, TextoQuestoes.Q3_EXPLICACAO)
    criaQuestao(TextoQuestoes.Q4_VALOR, TextoQuestoes.Q4_CORRETA,
                TextoQuestoes.Q4_PERGUNTA, TextoQuestoes.Q4_EXPLICACAO)
    criaQuestao(TextoQuestoes.Q5_VALOR, TextoQuestoes.Q5_CORRETA,
                TextoQuestoes.Q5_PERGUNTA, TextoQuestoes.Q5_EXPLICACAO)
    criaQuestao(TextoQuestoes.Q6_VALOR, TextoQuestoes.Q6_CORRETA,
                TextoQuestoes.Q6_PERGUNTA, TextoQuestoes.Q6_EXPLICACAO)
    criaQuestao(TextoQuestoes.Q7_VALOR, TextoQuestoes.Q7_CORRETA,
                TextoQuestoes.Q7_PERGUNTA, TextoQuestoes.Q7_EXPLICACAO_A,
                TextoQuestoes.Q7_EXPLICACAO_B, TextoQuestoes.Q7_EXPLICACAO_C,
                TextoQuestoes.Q7_EXPLICACAO_D,TextoQuestoes.Q7_EXPLICACAO_E)
    criaQuestao(TextoQuestoes.Q8_VALOR, TextoQuestoes.Q8_CORRETA,
                TextoQuestoes.Q8_PERGUNTA, TextoQuestoes.Q8_EXPLICACAO)
    criaQuestao(TextoQuestoes.Q9_VALOR, TextoQuestoes.Q9_CORRETA,
                TextoQuestoes.Q9_PERGUNTA, TextoQuestoes.Q9_EXPLICACAO)
    criaQuestao(TextoQuestoes.Q10_VALOR, TextoQuestoes.Q10_CORRETA,
                TextoQuestoes.Q10_PERGUNTA, TextoQuestoes.Q10_EXPLICACAO)


def mostraPontuacaoFinal():
    global totalPontos
    print("\n+--------------------------------------------------+\n")
    print("Resultados:")
    for i in range(len(respostasComputadas)):
        if respostasComputadas[i] == respostasCorretas[i]:
            resultado = "(+" + str(respostasPontuacao[i]) + ")"
            totalPontos += respostasPontuacao[i]
        else:
            resultado = "(Erro)"
        print("Questão", str(i + 1) + ":", respostasComputadas[i], resultado)
    time.sleep(2)
    print("\n Pontuação total:")
    print(totalPontos, "pontos!")

    if 0 <= totalPontos <= 10:
        print(TextoQuestoes.PESQUISE_MAIS_SOBRE_VACINACAO)

    elif 10 < totalPontos <= 30:
        print(TextoQuestoes.VACINACAO_IMPORTANTE_METADE_PONTUACAO)

    elif 30 < totalPontos <= 45:
        print(TextoQuestoes.VACINACAO_IMPORTANTE_METADE_PONTUACAO)

    elif 45 < totalPontos <= 65:
        print(TextoQuestoes.PONTUACAO_RELEVANTE)

    elif 65 < totalPontos <= 85:
        print(TextoQuestoes.PONTUACAO_BOA)

    elif 85 < totalPontos <= 95:
        print(TextoQuestoes.PONTUACAO_MUITO_BOA)

    else:
        print(TextoQuestoes.PONTUACAO_MAXIMA)
