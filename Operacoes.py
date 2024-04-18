class Operacoes():

    @staticmethod
    def soma(x, y):
        return x + y

    @staticmethod
    def subtracao(x, y):
        return x - y
    
    @staticmethod
    def multiplicacao(a,b):
        return a * b
    
    @staticmethod
    def divisao(a,b):
        if b == 0:
            return "Não é possivel dividir um valor por 0"
        return a/b