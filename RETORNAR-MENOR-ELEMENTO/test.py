import unittest
from script import MenorElemento

class MenorElementoTestCase(unittest.TestCase):
    
    def test_ListaPossuiApenasUmElementoOuNenhum(self):
        result = MenorElemento([5])
        self.assertEqual(result, 5)

        result = MenorElemento([50])
        self.assertEqual(result, 50)

        result = MenorElemento([])
        self.assertEqual(result, [])

    def test_RetornarMenorElemento(self):

        result = MenorElemento([5,9,33,65,32,12,89])
        print(result)
        self.assertEqual(result, 5)

test_suit = unittest.TestSuite()
test_suit.addTest(unittest.makeSuite(MenorElementoTestCase))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suit)