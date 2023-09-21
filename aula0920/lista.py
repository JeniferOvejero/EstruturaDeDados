from elemento import Elemento

class Lista:
    def __init__(self):
        self.inicio = None
        self.final = None

    def inserirFrente(self, id: int, resto: str):
        novoElemento = Elemento(id, resto)

        if self.inicio == None:
            self.inicio = novoElemento
            self.final = novoElemento
        else:
            self.inicio.proximo = self.inicio
            self.inicio = novoElemento

    def buscar(self, id: int):
        elemento = self.inicio
        while elemento != self.final:
            if elemento.id == id:
                print(elemento.resto)
            else:
                elemento = elemento.proximo

    def excluir(self, id: int):
        elemento = self.inicio
        if elemento.id == id:
            self.inicio = elemento.proximo
        else:
            while elemento != self.final:
                if elemento.proximo.id == id:
                    elemento.proximo = elemento.proximo.proximo
                else:
                    elemento = elemento.proximo