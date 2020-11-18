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
q1pergunta = ("Quantos tipos de vacinas existem?"
              "\n\nA) 1 "
              "\n\nB) 2 "
              "\n\nC) 5 "
              "\n\nD) 10 "
              "\n\nE) Inúmeras")
q1explicacao = ("\nExplicação:"
                "\nExistem 2 tipos: vacinas produzidas a partir de"
                "\nvírus atenuados e vacinas produzidas a partir de"
                "\nvírus inativados, bactérias mortas ou até mesmo"
                "\npedaços de ambos. As de vírus atenuados são feitas"
                "\na partir de vírus que passaram porprocedimentos"
                "\nque os enfraqueceram. As de patógenos (ou seja,"
                "\ncausadores dadoença, como vírus e bactérias)"
                "\ninativados, mortos ou partidos são produzidas com"
                "\no agente “morto”, incapaz de provocar a doença, ou"
                "\napenas com mutaçõesdesses agentes.")

# Variaveis questão 2
q2valor = 5
q2correta = "C"
q2pergunta = ("Para quais grupos a vacinação é importante?"
              "\n\nA) Apenas idosos, já que são mais suscetíveis a"
              "\ndoenças como por exemplo sarampo."
              "\n\nB) Apenas adolescentes e crianças, já que estão em"
              "\ndesenvolvimento e precisam de anticorpos."
              "\n\nC) Todos, para que a imunidade de cada indivíduo da"
              "\nsociedade erradique a doença."
              "\n\nD) Apenas crianças, como ainda não possuem a"
              "\nquantidade de anticorpos necessária para se proteger."
              "\n\nE) Apenas adultos e idosos, já que pararam de fabricar"
              "\ncélulas de defesa, assim precisando de uma ajuda"
              "\nexterna.")
q2explicacao = ("\nExplicação:"
                "\nComo uma doença imunoprevenível (ou seja, que pode ser"
                "\nevitada de forma eficaz através de vacinas) precisa"
                "\ninfectar outros humanos para “sobreviver”, em um"
                "\ncenário no qual todos estejam imunes à doença, ela"
                "\neventualmente deixará de existir. Desta forma todos"
                "\nestarão protegidos.")
# Variaveis questão 3
q3valor = 5
q3correta = "C"
q3pergunta = ("Vacinas e remédios possuem a mesma finalidade."
              "\nEssa afirmação está correta? Por quê?"
              "\n\nA) Sim. Vacinas e remédios são eficazes apenas após o"
              "\npaciente contrair a doença."
              "\n\nB) Sim. Vacinas e remédios são eficazes apenas para"
              "\nprevenir doenças."
              "\n\nC) Não. Vacinas servem para prevenir e remédios"
              "\nservem para tratar."
              "\n\nD) Não. Vacinas servem para curar e remédios servem"
              "\npara prevenir."
              "\n\nE) Não. Apesar de serem feitas da mesma forma, vacinas"
              "\nservem para prevenir e remédios para curar.")
q3explicacao = ("\nExplicação:"
                "\nRemédios e vacinas possuem finalidades diferentes."
                "\nVacinas servem para prevenir que se contraia a"
                "\ndoença em questão, ou caso a contraia, apresente"
                "\nsintomas mais leves, visto que já possui memória"
                "\nimunológica para produzir anticorpos. Já os"
                "\nremédios são utilizados para tratar doenças, ou seja"
                "\ndevem ser usados como método de cura após o"
                "\nsurgimento dos sintomas.")

# Variaveis questão 4
q4valor = 10
q4correta = "D"
q4pergunta = ("Quem criou a primeira vacina? Em qual século e para"
              "\nprevenir qual doença?"
              "\n\nA) Edward Johnson, no século 17, para prevenir a"
              "\ngripe comum."
              "\n\nB) Edward Jenner, no século 15, para prevenir a"
              "\nAIDS."
              "\n\nC) Edward Johnson, no século 21, para prevenir a"
              "\nmalária."
              "\n\nD) Edward Jenner, no século 18, para prevenir a"
              "\nvaríola."
              "\n\nE) Edward Johnson, no século 20, para prevenir a"
              "\nhepatite C.")
q4explicacao = ("\nExplicação:"
                "\nTodas as doenças citadas, fora varíola, ainda não"
                "\npossuem nenhuma vacina. Isso ocorre por conta da"
                "\ncomplexidade de algumas dessas doenças, ou por se"
                "\ntratarem de vírus e bactérias que mutações ocorrem"
                "\ncom muita facilidade e velocidade. Ademais, foi em"
                "\n1796, com Edward Jenner, que de fato nasceu a"
                "\nimunologia.")

# Variaveis questão 5
q5valor = 10
q5correta = "A"
q5pergunta = ("O que constitui uma vacina?"
              "\n\nA) Vírus ou bactérias mortos ou atenuados, ou"
              "\nfragmentos desses agentes."
              "\n\nB) Anticorpos concentrados retirados de organismos"
              "\nque se tornaram imunes ao vírus ou bactéria."
              "\n\nC) Um remédio fabricado que faz com que as bactérias"
              "\nou vírus presentes no corpo do indivíduo sejam erradicadas."
              "\n\nD) Agentes como vírus ou bactérias diferentes dos"
              "\nda doença fabricados com intuito de desativar os"
              "\nagentes da doença."
              "\n\nE) Nutrientes selecionados para que o corpo se"
              "\ntorne capaz de combater a doença, criando assim"
              "\nanticorpos.")
q5explicacao = ("\nExplicação:"
                "\nVacinas são constituídas por patógenos (Vírus ou"
                "\nbactérias da doença em questão) desativados ou"
                "\natenuados, para que o corpo do indivíduo possa"
                "\ncombatê-los por meio da criação de anticorpos para"
                "\nconseguir combater a doença verdadeira.")

# Variaveis questão 6
q6valor = 20
q6correta = "D"
q6pergunta = ("Segundo a Organização Mundial da Saúde, quantos óbitos"
              "\nas vacinas evitam anualmente?"
              "\n\nA) 100 mil"
              "\n\nB) 50 mil"
              "\n\nC) 5 milhões"
              "\n\nD) 3 milhões"
              "\n\nE) 1 milhão")
q6explicacao = ("\nExplicação:"
                "\nHoje, as vacinas protegem a população contra mais"
                "\nde 30 doenças e previnem cerca de 3 milhões de"
                "\nmortes por ano. Vacinas ainda controlam epidemias"
                "\nreduzem a mortalidade infantil e são a base do"
                "\ncrescimento econômico dos serviços de saúde e"
                "\npoderiam salvar mais 1,5 milhão de vidas se sua"
                "\naplicação for ampliada, afirma a OMS.")

# Variaveis questão 7
q7valor = 5
q7correta = "C"
q7pergunta = ("Todas as alternativas abaixo representam MITOS, exceto:"
              "\n\nA) As vacinas contêm mercúrio, e por isso são"
              "\nperigosas."
              "\n\nB) Vacinas, geralmente, causam autismo."
              "\n\nC) Existem vacinas que não podem ser tomadas por"
              "\ngestantes."
              "\n\nD) Pessoas saudáveis não precisam tomar vacinas."
              "\n\nE) Se uma doença está erradicada em determinado país"
              "\nnão há necessidade de sua população se vacinar.")
q7explicacaoA = ("\nExplicação:"
                 "\nO tiomersal é um composto orgânico, que contém"
                 "\nmercúrio, adicionado a algumas vacinas como"
                 "\nconservantes. É o conservante mais utilizado para"
                 "\nvacinas que são fornecidas em frascos multidose."
                 "\nNão existe evidência que indique que a quantidade"
                 "\nde tiomersal utilizada nas vacinas representa um"
                 "\nrisco para a saúde."
                 "\nAs mulheres grávidas podem se vacinar contra"
                 "\nalgumas doenças, entretanto, outras vacinas não"
                 "\nsão recomendadas para gestantes. Dentre as vacinas"
                 "\nque a gestante pode tomar, está a vacina contra a"
                 "\ngripe, a vacina contra a hepatite B e a dTpa"
                 "\n(difteria, tétano e coqueluche). Já dentre as"
                 "\nvacinas contraindicadas podemos citar a vacina"
                 "\ncontra a varicela e a contra HPV.")

q7explicacaoB = ("\nExplicação:"
                 "\nUm estudo apresentado em 1998 levantou preocupações"
                 "\nsobre uma possível relação entre a vacina contra o"
                 "\nsarampo, a caxumba, a rubéola e o autismo. Tal"
                 "\npesquisa foi posteriormente considerada seriamente"
                 "\nfalha, consequentemente o artigo foi retirado pela"
                 "\nrevista que o publicou. Infelizmente, sua"
                 "\npublicação desencadeou um pânico que levou à queda"
                 "\ndas coberturas de vacinação e subsequentes surtos"
                 "\ndessas doenças. Não há evidência de uma ligação"
                 "\nentre essa vacina e o autismo/transtornos"
                 "\nautistas."
                 "\nAs mulheres grávidas podem se vacinar contra"
                 "\nalgumas doenças, entretanto, outras vacinas não"
                 "\nsão recomendadas para gestantes. Dentre as vacinas"
                 "\nque a gestante pode tomar, está a vacina contra a"
                 "\ngripe, a vacina contra a hepatite B e a dTpa"
                 "\n(difteria, tétano e coqueluche). Já dentre as"
                 "\nvacinas contraindicadas podemos citar a vacina"
                 "\ncontra a varicela e a contra HPV.")

q7explicacaoC = ("\nExplicação:"
                 "\nAs mulheres grávidas podem se vacinar contra"
                 "\nalgumas doenças, entretanto, outras vacinas não"
                 "\nsão recomendadas para gestantes. Dentre as vacinas"
                 "\nque a gestante pode tomar, está a vacina contra a"
                 "\ngripe, a vacina contra a hepatite B e a dTpa"
                 "\n(difteria, tétano e coqueluche). Já dentre as"
                 "\nvacinas contraindicadas podemos citar a vacina"
                 "\ncontra a varicela e a contra HPV.")

q7explicacaoD = ("\nExplicação:"
                 "\nUma vida saudável é fundamental para a prevenção de"
                 "\numa grande quantidade de doenças, porém, não"
                 "\ngarante proteção efetiva contra todas elas. Isso"
                 "\nsignifica que mesmo que a pessoa se alimente bem"
                 "\ntenha bons hábitos de higiene e pratique"
                 "\nexercícios, ela deve ter o seu cartão de vacinação"
                 "\nem dia."
                 "\nAs mulheres grávidas podem se vacinar contra"
                 "\nalgumas doenças, entretanto, outras vacinas não"
                 "\nsão recomendadas para gestantes. Dentre as vacinas"
                 "\nque a gestante pode tomar, está a vacina contra a"
                 "\ngripe, a vacina contra a hepatite B e a dTpa"
                 "\n(difteria, tétano e coqueluche). Já dentre as"
                 "\nvacinas contraindicadas podemos citar a vacina"
                 "\ncontra a varicela e a contra HPV.")

q7explicacaoE = ("\nExplicação:"
                 "\nMesmo que uma doença seja considerada erradicada em"
                 "\nnosso país, a vacinação é fundamental, uma vez que"
                 "\na doença pode ainda existir em outros lugares e"
                 "\noutras pessoas podem trazer o agente causador para"
                 "\nnossa região. As pessoas que não foram vacinadas"
                 "\npodem então contrair a doença e novos casos podem"
                 "\nsurgir no país."
                 "\nAs mulheres grávidas podem se vacinar contra"
                 "\nalgumas doenças, entretanto, outras vacinas não"
                 "\nsão recomendadas para gestantes. Dentre as vacinas"
                 "\nque a gestante pode tomar, está a vacina contra a"
                 "\ngripe, a vacina contra a hepatite B e a dTpa"
                 "\n(difteria, tétano e coqueluche). Já dentre as"
                 "\nvacinas contraindicadas podemos citar a vacina"
                 "\ncontra a varicela e a contra HPV.")


# Variaveis questão 8
q8valor = 5
q8correta = "B"
q8pergunta = ("Qual doença foi considerada erradicada através da"
              "\nvacinação? "
              "\n\nA) AIDS."
              "\n\nB) Sarampo."
              "\n\nC) Pneumonia."
              "\n\nD) Febre amarela."
              "\n\nE) Amebíase.")
q8explicacao = ("\nExplicação:"
                "\nNenhuma das alternativas diferentes de “B” foram"
                "\nconsideradas erradicadas. Sarampo foi considerado"
                "\numa doença erradicada no Brasil em 2016, porém"
                "\nhouve um aumento no número de casos nos anos"
                "\nsubsequentes, principalmente devido à não"
                "\nvacinação, que resultou na perda dessa certificação"
                "\nno ano de 2019.")

# Variaveis questão 9
q9valor = 20
q9correta = "B"
q9pergunta = ("No Brasil, quais são as mais importantes entidades"
              "\nprodutoras de vacinas?"
              "\n\nA) As entidades mais importantes são o Hospital"
              "\nAlbert Sabin e a Fundação de Amparo à Pesquisa do"
              "\nEstado de São Paulo. O órgão regulador é o Conselho"
              "\nMonetário Nacional."
              "\n\nB) As entidades mais importantes são o Instituto"
              "\nButantan e a Fundação Oswaldo Cruz. O órgão regulador"
              "\né a Agência Nacional de Vigilância Sanitária."
              "\n\nC) As entidades produtoras mais importantes são os"
              "\nhospitais públicos da rede SUS. O órgão regulador é"
              "\na Agência Nacional de Saúde Suplementar."
              "\n\nD) A única entidade produtora de vacinas é o"
              "\nInstituto Butantan. O órgão regulador é o Banco"
              "\nCentral do Brasil."
              "\n\nE) Não há entidades produtoras de vacinas"
              "\nimportantes no Brasil. O órgão regulador responsável"
              "\né a Agência Nacional de Telecomunicações.")
q9explicacao = ("\nExplicação:"
                "\nO Instituto Butantan, de São Paulo, e a Fundação"
                "\nOswaldo Cruz, do Rio de Janeiro, são os principais"
                "\nprodutores de imunobiológicos do Brasil. Além de"
                "\nprodutores, são importantíssimos polos de pesquisa"
                "\ne desenvolvimento científico. A ANVISA - Agência"
                "\nNacional de Vigilância Sanitária, é o órgão"
                "\nregulador responsável pela aprovação de vacinas.")

# Variaveis questão 10
q10valor = 10
q10correta = "B"
q10pergunta = ("As vacinas são produtos biológicos que protegem os"
               "\nindivíduos contra diversas doenças, conhecidas como"
               "\nimunopreveníveis. As doenças que são prevenidas por"
               "\nmeio de vacinas são:"
               "\nA) Hepatite A, tétano e hantavirose."
               "\nB) Tétano, hepatite B e raiva."
               "\nC) Tétano, malária e raiva."
               "\nD) AIDS, tétano e raiva."
               "\nE) Gripe aviária, herpes zóster e diabetes.")
q10explicacao = ("\nExplicação:"
                 "\nNão existe vacina para hantavirose, diabetes"
                 "\nmalária, AIDS ou Gripe aviária.")

# Função menu inicial
def menuInicial():
    print("\n+--------------------------------------------------+\n"+
          "|               QUIZ SOBRE VACINAÇÃO               |"+
          "\n+--------------------------------------------------+\n"+
          "| Seja bem vindo ao quiz. Aqui o nosso objetivo é  |\n"+
          "| espalhar conhecimento sobre um assunto importe   |\n"+
          "| mas que está em torno de muitas fake news.       |\n"+
          "| Vacinação                                        |", end="")

# Função questão
def questao(valor, correta, pergunta, explicacaoA, explicacaoB = "0", explicacaoC = "0", explicacaoD = "0", explicacaoE = "0"):
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
                time.sleep(10)
                input("\nAperte 'ENTER' para prosseguir.")
            break
    respostasComputadas.append(resposta)
    numQuestao += 1

# Função Pontuação final
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
    time.sleep(2)
    print("\nPontuação total:")
    print(totalPontos,"pontos!")
    if totalPontos >= 0 and totalPontos <= 10:
        print("\nVacinação é um assunto muito importante."
              "\nPesquise mais sobre o assunto e tente"
              "\nfazer o quiz novamente com as informações"
              "\nensinadas")
    elif totalPontos > 10 and totalPontos <= 30:
        print("\nVacinação é um assunto muito importante."
              "\nMesmo que tenha acertado algumas questões"
              "\nainda é importante que pesquise mais sobre"
              "\no assunto!")
    elif totalPontos > 30 and totalPontos <= 45:
        print("\nVacinação é um assunto muito importante."
              "\nMesmo que tenha atingido quase metade da"
              "\npontuação máxima, ainda há muito para"
              "\naprender. É importante que pesquise mais"
              "\nsobre o assunto!")
    elif totalPontos > 45 and totalPontos <= 65:
        print("\nVacinação é um assunto muito importante."
              "\nVocê atingiu uma pontuação relevante, e"
              "\ncomo premiação, receberá 1 vacinação"
              "\ngratuita. Entretanto, ainda há muito para"
              "\naprender. É importante que pesquise mais"
              "\nsobre o assunto!")
    elif totalPontos > 65 and totalPontos <= 85:
        print("\nVacinação é um assunto muito importante."
              "\nVocê atingiu uma pontuação boa, e"
              "\ncomo premiação, receberá 1 vacinação"
              "\ngratuita. Entretanto, ainda há conceitos"
              "\nimportantes sobre vacinação para"
              "\nrevisar. É importante que pesquise mais"
              "\nsobre o assunto!")
    elif totalPontos > 85 and totalPontos <= 95:
        print("\nVacinação é um assunto muito importante."
              "\nVocê atingiu uma pontuação muito boa, e"
              "\ncomo premiação, receberá 1 vacinação"
              "\ngratuita. Entretanto, ainda há conceitos"
              "\nimportantes sobre vacinação para"
              "\nrevisar. É importante que pesquise mais"
              "\nsobre o assunto!")
    else:
        print("\nVacinação é um assunto muito importante."
              "\nMas você já sabe disso, já que atingiu"
              "\na pontuação máxima."
              "\nComo premiação, receberá 1 ano de"
              "\nvacinação gratuita."
              "\nEste premio poderá ser doado a qualquer"
              "\nindividuo que escolher.")
    
# Chama a função menuInicial
menuInicial()

# Chama a função "questão" para cada questão.
questao(q1valor, q1correta, q1pergunta, q1explicacao)
questao(q2valor, q2correta, q2pergunta, q2explicacao)
questao(q3valor, q3correta, q3pergunta, q3explicacao)
questao(q4valor, q4correta, q4pergunta, q4explicacao)
questao(q5valor, q5correta, q5pergunta, q5explicacao)
questao(q6valor, q6correta, q6pergunta, q6explicacao)
questao(q7valor, q7correta, q7pergunta, q7explicacaoA, q7explicacaoB, q7explicacaoC, q7explicacaoD, q7explicacaoE)
questao(q8valor, q8correta, q8pergunta, q8explicacao)
questao(q9valor, q9correta, q9pergunta, q9explicacao)
questao(q10valor, q10correta, q10pergunta, q10explicacao)

# Chama a função "pontuacaoFinal" após as questões
pontuacaoFinal()
