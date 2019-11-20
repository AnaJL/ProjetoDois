from Dados import Dado 

class No:
    def __init__(self, dado):
        self._dado = dado
        self._left = None
        self._right = None
    def get_dado(self):
        return self._dado
    def set_dado(self, novoDado):
        self._dado = novoDado
    def get_left(self):
        return self._left
    def set_left(self, outro):
        self._left = outro
    def get_right(self):
        return self._right
    def set_right(self, outro):
        self._right = outro
    def __str__(self):
        return str(self._dado)
