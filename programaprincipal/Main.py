from regrasquiz import Questao


def menuInicial():
    print("\n+---------------------------------------------------+\n" +
          "|                QUIZ SOBRE VACINAÇÃO               |" +
          "\n+---------------------------------------------------+\n" +
          "| Seja bem vindo ao quiz. Aqui o nosso objetivo é   |\n" +
          "| espalhar conhecimento sobre um assunto importe    |\n" +
          "| mas que está em torno de muitas fake news.        |\n" +
          "| Vacinação                                         |\n" +
          "| Ao longo do questionário, para a alternativa      |\n" +
          "| correta responda: A, B, C, D ou E                 |\n" +
          "+---------------------------------------------------+", end="")
    input("\n\nAperte 'ENTER' para prosseguir.")


menuInicial()

Questao.explicaQuestoes()

Questao.mostraPontuacaoFinal()
