import time

# Lista com entradas válidas
respostasPossiveis = ["A","B","C","D","E"]

# Declaração de listas
respostasComputadas = []
respostasCorretas = []
respostasPontuacao = []

# Declaração de variaveis
numQuestao = 0
totalPontos = 0

# Variaveis questão 1
q1valor = 10
q1correta = "B"
q1pergunta = ("Quantos tipos de vacinas existem? "
              "\nA) 1 "
              "\nB) 2 "
              "\nC) 5 "
              "\nD) 10 "
              "\nE) Inúmeras")
q1explicacao = ("\nExplicação:"
                "\nExistem 2 tipos: vacinas produzidas a partir de"
                "\nvírus atenuados e vacinas produzidas a partir de"
                "\nvírus inativados, bactérias mortas ou até mesmo"
                "\npedaços de ambos. As de vírus atenuados são feitas"
                "\na partir de vírus que passaram porprocedimentos"
                "\nque os enfraqueceram. As de patógenos (ou seja,"
                "\ncausadores dadoença, como vírus e bactérias)"
                "\ninativados, mortos ou partidos são produzidascom"
                "\no agente “morto”, incapaz de provocar a doença, ou"
                "\napenas com mutaçõesdesses agentes.")

# Variaveis questão 2
q2valor = 5
q2correta = "C"
q2pergunta = ("Pergunta"
              "\nA) a"
              "\nB) b"
              "\nC) c"
              "\nD) d"
              "\nE) e")
q2explicacao = ("\nExplicação:"
                "\ntextotextotextotextotextotextotextotextotextotexto"
                "\ntextotextotextotextotextotextotextotextotextotexto"
                "\ntextotextotextotextotextotextotextotextotextotexto"
                "\ntextotextotextotextotextotextotextotextotextotexto"
                "\ntextotextotextotextotextotextotextotextotextotexto"
                "\ntextotextotextotextotextotextotextotextotextotexto"
                "\ntextotextotextotextotextotextotextotextotextotexto"
                "\ntextotextotextotextotextotextotextotextotextotexto"
                "\ntextotextotextotextotextotextotextotextotextotexto"
                "\ntextotextotextotextotextotextotextotextotextotexto")

# Primeira questão
def menuInicial():
    print("\n+--------------------------------------------------+\n"+
          "|               QUIZ SOBRE VACINAÇÃO               |"+
          "\n+--------------------------------------------------+\n"+
          "| Seja bem vindo ao quiz. Aqui o nosso objetivo é  |\n"+
          "| espalhar conhecimento sobre um assunto importe   |\n"+
          "| mas que está em torno de muitas fake news.       |\n"+
          "| Vacinação                                        |", end="")

# Função questão
def questao(valor, correta, pergunta, explicacao):
    global numQuestao
    respostasPontuacao.append(valor)
    respostasCorretas.append(correta)
    print("\n+--------------------------------------------------+\n")
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
                print("\nIncorreto.")
                time.sleep(1)
                print(explicacao)
                time.sleep(5)
                input("\nAperte 'ENTER' para prosseguir.")
            break
    respostasComputadas.append(resposta)
    numQuestao += 1

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
questao(q1valor, q1correta, q1pergunta, q1explicacao)
questao(q2valor, q2correta, q2pergunta, q2explicacao)
pontuacaoFinal()
