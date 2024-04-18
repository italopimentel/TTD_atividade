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

#inicia o teste
unittest.main()
