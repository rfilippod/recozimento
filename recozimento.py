import math
import random
import numpy as np
import Avaliacao
import time
import Perturbacao
import copy
from xlwt import Workbook
import entradas
import matplotlib.pyplot as plt

"""
        Variáveis:
        ----------------------------------------------------------------------------------------------------------------
        estado:             é o valor da função objetivo
        ----------------------------------------------------------------------------------------------------------------
        estado_atual:       é o valor da função objetivo da solução atual
        ----------------------------------------------------------------------------------------------------------------
        solucao_subsequente[]:  dicionário que mantém as informações da solucao obtida após a perturbação da 
                                solucao_atual

                                solucao_subsequente[0]: recebe a matriz de horários da solução
                                solucao_subsequente[1]: recebe o valor da função objetivo calculada da solução
        ----------------------------------------------------------------------------------------------------------------
        solucao_atual[]:    dicionário que mantém as informações da solução tratada como adotada atualmente no ciclo de
                            operações

                            solucao_atual[0]: recebe a matriz de horários da solução
                            solucao_atual[1]: recebe o valor da função objetivo calculada da solução
        ----------------------------------------------------------------------------------------------------------------
        temperatura:        valor alto inicial o qual será descontada uma taxa de resfriamento fixo
        ----------------------------------------------------------------------------------------------------------------
        razao_resfriamento: valor fixo da razão pela qual a temperatura será gradativamente diminuída após cada série de
                            tentativas de obtenção de uma melhor solução
        ----------------------------------------------------------------------------------------------------------------
        temperatura_atual:  valor atual da temperatura inicial decrescido da razao_resfriamento na série atual de
                            tentativa de obtenção de uma melhor solução
        ---------------------------------------------------------------------------------------------------------------- 

"""

# t_total = []
vetor_fitness =[]
vetor_tempo =[]
vetor_seed =[]

for value in range(10):
    random.seed(value)
    t_inicio = time.time()


    temperatura = 100
    razao_resfriamento = 0.5
    solucao_subsequente = {}
    estado_atual = 0
    solucao_atual = {}

    """
            ----------------------------------------------------------------------------------------------------------------
                Realização do Simulated Annealing: a solucao_atual recebe a solucao inicial e, então, 
                enquanto a temperatura for maior que zero, continua realizando as trocas, caso as 
                soluções tenham custos menores que a anterior
            ----------------------------------------------------------------------------------------------------------------
    """


    def simulated_annealing(solucao_inicial, temperatura, razao_resfriamento):
        solucao_atual = copy.deepcopy(solucao_inicial)

        solucao_atual[1] = calcula_funcao_objetivo(solucao_atual[0])
        cont = 0
        while temperatura > 0:
            cont = cont + 1

            solucao_subsequente[0] = copy.deepcopy(perturbacao(solucao_atual[0]))
            solucao_subsequente[1] = calcula_funcao_objetivo(solucao_subsequente[0])
            #print(f'\nsolucao_subsequente[0] = \n{solucao_subsequente[0]}')
            #print(f'solucao_subsequente[1] = {solucao_subsequente[1]}')

            # Teste de variação do valor da função objetivo:
            variacao_atual = solucao_atual[1] - solucao_subsequente[1]

            troca = annealing(variacao_atual, temperatura)
            if troca == 1:
                solucao_atual = copy.deepcopy(solucao_subsequente)

            temperatura = temperatura * razao_resfriamento
            # print(f'A temperatura é {temperatura}')
        t_total = time.time() - t_inicio
        # print(f'O tempo final foi {t_total}')
        # print(cont)
        return solucao_atual


    """
            ----------------------------------------------------------------------------------------------------------------
            Se variacao < 0:    redução de energia, sendo a nova solução melhor que a anterior, solucao_atual passa a ser a 
                                solucao perturbada que apresentou melhor valor no cálculo da função objetivo
            ----------------------------------------------------------------------------------------------------------------
            Se variacao > 0:    aumento de energia, solução perturbada é aceita dada a função:
                                p = e^((-variacao)/temperatura): exponencial de (-) variação dividido pela temperatura
            ----------------------------------------------------------------------------------------------------------------
            Se troca:           retorna 1
            ----------------------------------------------------------------------------------------------------------------
            Se não troca:       retorna 0
            ----------------------------------------------------------------------------------------------------------------
    """


    def annealing(variacao, temperatura):
        if variacao < 0:
            return 1
        elif calcula_probabilidade(variacao, temperatura) < (random.uniform(0, 1)):
            return 1
        else:
            return 0


    """
            ----------------------------------------------------------------------------------------------------------------
            Cálculo probabilístico de aceitação da solução, conhecida como "critério de Metrópolis" (sem a constante de 
            Boltzman devido à constante não ter analogia num problema de otimização, sendo eliminada)
            ----------------------------------------------------------------------------------------------------------------
    """


    def calcula_probabilidade(variacao, temperatura_atual):
        return math.exp(-variacao / temperatura_atual)


    """
            ----------------------------------------------------------------------------------------------------------------
            Cáclulo da função objetivo da solução
            ----------------------------------------------------------------------------------------------------------------
    """


    def calcula_funcao_objetivo(solucao):

        novo = Avaliacao.Avaliacao(solucao)
        return novo.calcula()


    """
            ----------------------------------------------------------------------------------------------------------------
            Realização de uma perturbação na solução para que possa encontrar um vizinho
            ----------------------------------------------------------------------------------------------------------------
    
    """


    def perturbacao(solucao):
        pertuba = Perturbacao.Perturbacao(solucao)
        return pertuba.perturba()


    if __name__ == '__main__':  # função main

        matriz_solucao = {}

        matriz_solucao[0] = entradas.entrada()

        matriz_solucao[1] = calcula_funcao_objetivo(matriz_solucao[0])

        solucao = simulated_annealing(matriz_solucao, temperatura, razao_resfriamento)
        t_total = time.time() - t_inicio

        print(str("\n\n\n\n\ntempo %.4f" % t_total))
        print(f'solucao {value} \n{solucao}')
        wb = Workbook()
        sheet1 = wb.add_sheet('Resultados')
        sheet1.write(0, 0, 'Instância')
        sheet1.write(0, 1, 'Semente')
        sheet1.write(0, 2, 'Melhor resultado obtido')
        sheet1.write(0, 3, 'Tempo')

        j = 1
        y = 1

        # for x in range(4):
        sheet1.write(y, 0, 'BrazilInstance1')
        sheet1.write(y, 1, value)
        sheet1.write(y, 2, solucao[1])
        sheet1.write(y, 3, t_total)
        y += 1
        wb.save(f'Resultados{value}.xls')

        vetor_fitness.append(solucao[1])
        vetor_tempo.append(t_total)
        vetor_seed.append(value)

        # print(f'\nA solução encontrada foi: {solucao}')

        """testao = ['a', 'b', 'c']

        teste = np.array([['T8-S1', 'T1-S1', 'T3-S1', 'T1-S1', 'T7-S1'],
                 ['T4-S1', 'T1-S1', 'T4-S1', 'T2-S1', 'T3-S1'],
                 ['T4-S1', 'T2-S1', 'T2-S1', 'T2-S1', 'T3-S1'],
                 ['T6-S1', 'T2-S1', 'T7-S1', 'T7-S1', 'T6-S1'],
                 ['T6-S1', 'T8-S1', 'T7-S1', 'T7-S1', 'T6-S1']])
    
        teste1 = np.array([['T4-S2', 'T2-S2', 'T2-S2', 'T2-S2', 'T6-S2'],
                           ['T6-S2', 'T2-S2', 'T2-S2', 'T1-S2', 'T6-S2'],
                           ['T6-S2', 'T5-S2', 'T3-S2', 'T1-S2',	'T5-S2'],
                           ['T8-S2', 'T5-S2', 'T4-S2', 'T5-S2',	'T3-S2'],
                           ['T8-S2', 'T1-S2', 'T4-S2', 'T5-S2', 'T3-S2']])
    
        teste2 = np.array([['T6-S3', 'T5-S3', 'T7-S3', 'T7-S3',	'T3-S3'],
                           ['T8-S3', 'T5-S3', 'T7-S3', 'T7-S3',	'T7-S3'],
                           ['T8-S3', 'T1-S3', 'T4-S3', 'T5-S3',	'T6-S3'],
                           ['T4-S3', 'T6-S3', 'T3-S3', 'T1-S3',	'T5-S3'],
                           ['T4-S3', 'T6-S3', 'T3-S3', 'T1-S3',	'T5-S3']])
    
        testao[0] = teste
        testao[1] = teste1
        testao[2] = teste2
    
        oi = Avaliacao.Avaliacao(testao)"""
# print(f' from keys {entradas.evento}')
plt.title("BrazilInstance1_XHSTT-v2014")
# plt.xlabel("Tempo de execução (em segundos)")
plt.xlabel("Seed (semente)")
plt.ylabel("Valor de f(x)")
plt.scatter(vetor_seed, vetor_fitness)
plt.show()

