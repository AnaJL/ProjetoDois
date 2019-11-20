class Dado:
    def __init__(self, filme=None, ano=None, chave = None):
        self._filme = filme   
        self._ano = ano
        self._id = chave 
    def get_filme(self):
        return self._filme
    def get_ano(self):
        return self._ano
    def set_filme(self, new):
         self._filme = new
    def set_ano(self, new):
        self._ano = new
    def set_id(self, new):
         self._id = new
    def get_id(self, new):
        return self._id
    def set_filmeeano(self,newfil, newano):
        self._filme = newfil
        self._ano = newano
    def get_filmeeano(self):
        return f'''FILME: {self._filme}
                   ANO: {self._ano}
                   CHAVE: {self._id}'''
    
