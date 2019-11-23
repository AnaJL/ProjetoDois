from Dados import Dado
class No:
    def __init__(self,dado, filho = None, esquerda = None, direita = None):
        self._dado = dado
        self._filho = filho
        self._esquerda = esquerda
        self._direita = direita
    def get_esquerda(self):
        return self._esquerda
    def set_esquerda(self,novo):
        self._esquerda = novo
    def get_direita(self):
        return self._direita
    def set_direita(self,novo):
        self._direita = novo
    def profundidade(self):
        prof_esq = 0
        prof_dir = 0
        if self.get_esquerda():
            prof_esq = self.get_esquerda().profundidade()
        if self.get_direita():
            prof_dir = self.get_direita().profundidade()
        return max(prof_esq, prof_dir)
    def verBalanco(self):
        profundidade_esquerda = 0
        profundidade_direita = 0
        if self.get_esquerda:
           profundidade_esquerda = self.get_esquerda().profundidade()
        if self.get_direita:
            profundidade_direita = self.get_direita().profundidade()
        return profundidade_esquerda - profundidade_direita
    def Rotacionar_Esquerda(self):
        aux = self._dado.get_direita()
        self._dado.set_direita(aux._esquerda())
        aux.set_esquerda(self._dado)
        return aux
    def Rotacionar_Direita(self):
        aux = self._dado.get_esquerda()
        self._dado.set_esquerda(aux.set_direita())
        aux.set_direita(self._dado)
        return aux
    def inserir(self, elem):
        if elem < self._dado:
            if not self._esquerda:
                self.set_direita(elem)
            else:
                self._esquerda.inserir(elem)
        else:
            if not self._direita:
                self.set_direita(elem)
            else:
                self._direita.inserir(elem)
        self.Balanceamento()


    def Rotacionar_Esquerda_Direita(self):
        self.get_esquerda().Rotacionar_Esquerda()
        self.Rotacionar_Direita()

    def Rotacionar_Direita_Esquerda(self):
        self.get_direita().Rotacionar_Direita()
        self.Rotacionar_Direita()
    def Balanceamento(self):
        balancear = self.verBalanco()
        if balancear > 1:
            if self.get_esquerda().balanco() > 0:
                self.Rotacionar_Direita()
            else:
                self.Rotacionar_Esquerda_Direita()
        elif balancear < -1:
            if self.get_direita().balanco < 0:
                self.Rotacionar_Esquerda()
            else:
                self.Rotacionar_Direita_Esquerda()
    def imprimeArvoreAvl(self, espaco = 0):
        print(" " * espaco + str(self._dado))
        if self._esquerda:
            self._esquerda.imprimeArvore(espaco + 2)
        if self._direita:
            self._direita.imprimeArvore(espaco + 2)
