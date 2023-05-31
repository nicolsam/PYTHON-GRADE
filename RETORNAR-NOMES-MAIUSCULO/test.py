import unittest
from script import TransformarEmMaiusculo

class TransformarEmMaiusculoTestCase(unittest.TestCase):
    def test_RetornaNomesEmMaiusculo(self):
        payload = ['aviao', 'carro', 'navio']
        result = TransformarEmMaiusculo(payload)
        self.assertEqual(result, ['AVIAO', 'CARRO', 'NAVIO'])


test_suit = unittest.TestSuite()
test_suit.addTest(unittest.makeSuite(TransformarEmMaiusculoTestCase))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suit)