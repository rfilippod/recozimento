import random
import Avaliacao
import copy
import re

"""
        ----------------------------------------------------------------------------------------------------------------
        Classe para a realização de perturbação do sistema.

        A perturbação aqui é realizada da seguinte maneira: escolhe-se uma turma aleatória e então um evento aleatório,
        feito isso, troca-se com o primeiro evento da turma e então retorna a nova solução
        ----------------------------------------------------------------------------------------------------------------
        Variáveis
        ----------------------------------------------------------------------------------------------------------------
        self.dict_matriz: recebe o dicionario das matrizes 
        ----------------------------------------------------------------------------------------------------------------
        self.dict_matriz_novo: onde será feita toda a perturbação, é o dicionario que sera retornado
        ----------------------------------------------------------------------------------------------------------------
        rand_x: seleciona aleatóriamente uma turma para realizar a troca
        ----------------------------------------------------------------------------------------------------------------
        rand_i e rand_j: selecionam uma linha e uma coluna aleatória, fazendo com que um evento seja selecionado para a 
        troca
        ----------------------------------------------------------------------------------------------------------------

"""


class Perturbacao():
    def __init__(self, dict_matriz):
        self.dict_matriz = dict_matriz

    def perturba(self):
        self.dict_matriz_novo = copy.deepcopy(self.dict_matriz)

        rand_x = random.randint(0, 2)

        rand_i = random.sample(range(len(self.dict_matriz[0])), len(self.dict_matriz[0]))  # refinando a matriz 0 (S1)

        rand_j = random.sample(range(len(self.dict_matriz[0])), len(self.dict_matriz[0]))

        rand_w = random.sample(range(len(self.dict_matriz[0])), len(self.dict_matriz[0]))

        rand_y = random.sample(range(len(self.dict_matriz[0])), len(self.dict_matriz[0]))


        i = 1

        self.dict_matriz_novo[rand_x][rand_i[i]][rand_j[i]], self.dict_matriz_novo[rand_x][rand_w[i]][rand_y[i]] = \
            self.dict_matriz_novo[rand_x][rand_w[i]][rand_y[i]], self.dict_matriz_novo[rand_x][rand_i[i]][rand_j[i]]
        return self.dict_matriz_novo



