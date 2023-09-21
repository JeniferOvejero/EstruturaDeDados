from lista import Lista

class Hash:
    def __init__(self, tamTab: int):
        self.tamTab = tamTab
        tab = [None]*tamTab

    def inserirHash(self, id: int, resto: str):
        grupo = funcaoHash(id)
        tab[grupo].inserirFrente(id, resto)
    
    def funcaoHash(self, id: int):
        enderecoPrimario = id % self.tamTab