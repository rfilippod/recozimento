import re
import random

"""
        ----------------------------------------------------------------------------------------------------------------
        Calculo das restrições da solução enviada, neste dataset, o valor de todas as restrições são 1.
        Aqui são calculadas as restrições de professor (não pode dar aula no dia x da semana) e 
        Hhorários concorrentes: professores não podem dar aula pra turma 1 e a 2 ao mesmo tempo
        ---------------------------------------------------------------------------------------------------------------- 

"""



class Avaliacao():
    def __init__(self, dict_matriz):
        self.dict_matriz = dict_matriz

    def calcula(self):
        T3 = ('\\bT3\\b')
        T4 = ('\\bT4\\b')
        T5 = ('\\bT5\\b')
        T6 = ('\\bT6\\b')
        T7 = ('\\bT7\\b')
        T8 = ('\\bT8\\b')
        T9 = ('\\bT9\\b')
        T10 = ('\\bT10\\b')
        T11 = ('\\bT11\\b')
        T12 = ('\\bT12\\b')
        T13 = ('\\bT13\\b')
        T14 = ('\\bT14\\b')
        contador = 0  # Calculo das restrições dos professores, alguns não podem dar aula em certos dias
        for x in range(3):
            for i in range(5):
                if re.search(T3, self.dict_matriz[x][i][3], re.IGNORECASE):  # não pode dar aula quinta-feira
                    contador += 1
                if re.search(T4, self.dict_matriz[x][i][1], re.IGNORECASE):  # não pode dar aula terça-feira
                    contador += 1

                if re.search(T5, self.dict_matriz[x][i][0], re.IGNORECASE):  # não pode dar aula segunda-feira
                    contador += 1
                if re.search(T6, self.dict_matriz[x][i][2], re.IGNORECASE):  # não pode dar aula segunda-feira
                    contador += 1
                if re.search(T7, self.dict_matriz[x][i][1], re.IGNORECASE):  # não pode dar aula terça-feira
                    contador += 1
                if re.search(T8, self.dict_matriz[x][i][3], re.IGNORECASE):  # não pode dar aula quinta-feira
                    contador += 1
                if re.search(T9, self.dict_matriz[x][i][3], re.IGNORECASE):  # não pode dar aula quinta-feira
                    contador += 1
                if re.search(T10, self.dict_matriz[x][i][3], re.IGNORECASE):  # não pode dar aula quinta-feira
                    contador += 1
                if re.search(T11, self.dict_matriz[x][i][3], re.IGNORECASE):  # não pode dar aula quinta-feira
                    contador += 1
                if re.search(T12, self.dict_matriz[x][i][3], re.IGNORECASE):  # não pode dar aula quinta-feira
                    contador += 1
                if re.search(T13, self.dict_matriz[x][i][3], re.IGNORECASE):  # não pode dar aula quinta-feira
                    contador += 1
                if re.search(T14, self.dict_matriz[x][i][0], re.IGNORECASE):  # não pode dar aula quinta-feira
                    contador += 1

        """
        ----------------------------------------------------------------------------------------------------------------        
        Aqui embaixo é onde realiza-se a contagem dos horarios concorrentes para todos os professores
        ----------------------------------------------------------------------------------------------------------------
        """


        for j in range(5):
            for i in range(5):
                if re.search(T3, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T3, self.dict_matriz[1][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1
                if re.search(T3, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T3, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1
                if re.search(T3, self.dict_matriz[1][i][j], re.IGNORECASE) and re.search(T3, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1
                if re.search(T4, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T4, self.dict_matriz[1][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1
                if re.search(T4, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T4, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T4, self.dict_matriz[1][i][j], re.IGNORECASE) and re.search(T4, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T5, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T5, self.dict_matriz[1][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T5, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T5, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T5, self.dict_matriz[1][i][j], re.IGNORECASE) and re.search(T5, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T6, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T6, self.dict_matriz[1][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T6, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T6, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T6, self.dict_matriz[1][i][j], re.IGNORECASE) and re.search(T6, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T7, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T7, self.dict_matriz[1][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T7, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T7, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T7, self.dict_matriz[1][i][j], re.IGNORECASE) and re.search(T7, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T8, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T8, self.dict_matriz[1][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T8, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T8, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T8, self.dict_matriz[1][i][j], re.IGNORECASE) and re.search(T8, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T9, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T9, self.dict_matriz[1][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T9, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T9, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T9, self.dict_matriz[1][i][j], re.IGNORECASE) and re.search(T9, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T10, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T10, self.dict_matriz[1][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T10, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T10, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T10, self.dict_matriz[1][i][j], re.IGNORECASE) and re.search(T10, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T11, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T11, self.dict_matriz[1][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T11, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T11, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T11, self.dict_matriz[1][i][j], re.IGNORECASE) and re.search(T11, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T12, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T12, self.dict_matriz[1][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T12, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T12, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T12, self.dict_matriz[1][i][j], re.IGNORECASE) and re.search(T12, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T13, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T13, self.dict_matriz[1][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T13, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T13, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T13, self.dict_matriz[1][i][j], re.IGNORECASE) and re.search(T13, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T14, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T14, self.dict_matriz[1][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T14, self.dict_matriz[0][i][j], re.IGNORECASE) and re.search(T14, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

                if re.search(T14, self.dict_matriz[1][i][j], re.IGNORECASE) and re.search(T14, self.dict_matriz[2][i][j],
                                                                                    re.IGNORECASE):
                    contador += 1

        self.nota_avaliacao = contador
        return self.nota_avaliacao

        # soma as notas das avaliações, todas com custo 1

    def getAvaliacao(self):
        return self.nota_avaliacao




