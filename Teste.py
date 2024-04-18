from Operacoes import Operacoes
import unittest

class TesteOperacoes(unittest.TestCase):
    
    def test_soma(self):
        self.assertEqual(8, Operacoes.soma(5, 3), "Deveria ser 8 na Soma")
        self.assertEqual(-3, Operacoes.soma(-2,-1), "Deveria ser -3 na Soma")
        self.assertEqual(0, Operacoes.soma(5, -5), "Deveria ser 0 na Soma")
        
    def test_subtracao(self):
        self.assertEqual(6, Operacoes.subtracao(8,2), "Deveria ser 6 na Subtração")
        self.assertEqual(-5, Operacoes.subtracao(-3,2), "Deveria ser -5 na Subtração")
        self.assertEqual(0, Operacoes.subtracao(-5,-5), "Deveria ser 0 na Subtração")
        
    def test_multiplicacao(self):
        self.assertEqual(4, Operacoes.multiplicacao(2,2), "Deveria ser 4 na Multiplicação")
        self.assertEqual(-35, Operacoes.multiplicacao(5,-7), "Deveria ser -35 na Multiplicação")
        self.assertEqual(9, Operacoes.multiplicacao(-3,-3), "Deveria ser 9 na Multiplicação")
        self.assertEqual(0, Operacoes.multiplicacao(2,0), "Deveria ser 0 na Multiplicação")
        self.assertEqual(0, Operacoes.multiplicacao(0,0), "Deveria ser 0 na Multiplicação")

    def test_divisao(self):
        self.assertEqual(2, Operacoes.divisao(4,2), "Deveria ser 2 na Divisão")
        self.assertEqual(-2, Operacoes.divisao(4,-2), "Deveria ser -2 na Divisão")
        self.assertEqual(5, Operacoes.divisao(-10,-2), "Deveria ser 5 na Divisão")
        self.assertEqual("Não é possivel dividir um valor por 0", Operacoes.divisao(3,0))


#inicia o teste
unittest.main()
