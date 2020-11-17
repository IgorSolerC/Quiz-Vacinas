import time

# Lista com entradas válidas
respostasPossiveis = ["A","B","C","D","E"]

# Declaração de listas
respostasComputadas = []
respostasCorretas = []
respostasPontuacao = []

# Declaração de variaveis
questao = 0
totalPontos = 0

# Primeira questão
def menuInicial():
    print("\n+--------------------------------------------------+\n"+
          "|               QUIZ SOBRE VACINAÇÃO               |"+
          "\n+--------------------------------------------------+\n"+
          "| Seja bem vindo ao quiz. Aqui o nosso objetivo é  |\n"+
          "| espalhar conhecimento sobre um assunto importe   |\n"+
          "| mas que está em torno de muitas fake news.       |\n"+
          "| Vacinação                                        |", end="")

    questao1()

def questao1():
    global questao
    valor = 10
    correta = "B"
    respostasPontuacao.append(valor)
    respostasCorretas.append(correta)
    print("\n+--------------------------------------------------+\n")
    print("Quantos tipos de vacinas existem?",
          "\nA) 1",
          "\nB) 2",
          "\nC) 5",
          "\nD) 10",
          "\nE) Inúmeras")
    while True:
        resposta = input("\nResposta: ").upper()
        if resposta not in respostasPossiveis:
            print("Resposta inválida")
            continue
        else:
            if resposta == respostasCorretas[questao]:
                print("\nCorreto!")
                time.sleep(1)
            else:
                print("\nIncorreto.")
                time.sleep(1)
                print("\nExplicação:",
                      "\nExistem 2 tipos: vacinas produzidas a partir de"+
                      "\nvírus atenuados e vacinas produzidas a partir de"+
                      "\nvírus inativados, bactérias mortas ou até mesmo"+
                      "\npedaços de ambos. As de vírus atenuados são feitas"+
                      "\na partir de vírus que passaram porprocedimentos"+
                      "\nque os enfraqueceram. As de patógenos (ou seja,"+
                      "\ncausadores dadoença, como vírus e bactérias)"+
                      "\ninativados, mortos ou partidos são produzidascom"+
                      "\no agente “morto”, incapaz de provocar a doença, ou"+
                      "\napenas com mutaçõesdesses agentes.")
                time.sleep(5)
                input("\nAperte 'ENTER' para prosseguir.")
            break
    respostasComputadas.append(resposta)
    questao += 1
    questao2()

# Segunda questão
def questao2():
    global questao
    valor = 5
    correta = "C"
    respostasPontuacao.append(valor)
    respostasCorretas.append(correta)
    print("\n+--------------------------------------------------+\n")
    print("Pergunta",
          "\nA) resposta",
          "\nB) resposta",
          "\nC) resposta",
          "\nD) resposta",
          "\nE) resposta")
    while True:
        resposta = input("\nResposta: ").upper()
        if resposta not in respostasPossiveis:
            print("Resposta inválida")
            continue
        else:
            if resposta == respostasCorretas[questao]:
                print("\nCorreto!")
                time.sleep(1)
            else:
                print("\nIncorreto.")
                time.sleep(1)
                print("\nExplicação:",
                      "'texto'")
                time.sleep(5)
                input("\nAperte 'ENTER' para prosseguir.")
            break
    respostasComputadas.append(resposta)
    questao += 1
    #questao3()

# Pontuação final
def pontuacaoFinal():
    global totalPontos
    print("\n+--------------------------------------------------+\n")
    print("Resultados:")
    for i in range(len(respostasComputadas)):
        if respostasComputadas[i] == respostasCorretas[i]:
            resultado = "(+"+str(respostasPontuacao[i])+")"
            totalPontos += respostasPontuacao[i]
        else:
            resultado = "(Erro)"
        print("Questão",str(i+1)+":",respostasComputadas[i], resultado)
    print("\nPontuação total:")
    print(totalPontos,"pontos!")
    

menuInicial()
pontuacaoFinal()
