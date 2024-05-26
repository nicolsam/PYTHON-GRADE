import unittest
from script import Database

class DatabaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        cls.database = Database('frutas.db')

    def test_InserirFruta(self):

        result = self.database.insert_fruit(100, 'Cereja', 'Vermelha')
        self.assertTrue(result)

    def test_SelecionarPorId(self):

        result = self.database.select_by_id('frutas', 100)
        self.assertEqual(result, (100, 'Cereja', 'Vermelha'))

    def test_AtualizarFruta(self):

        result = self.database.update_fruit(100, 'Framboesa', 'Vermelha')
        self.assertEqual(result, (100, 'Framboesa', 'Vermelha'))

    def test_DeletarFruta(self):

        result = self.database.delete_fruit(100)
        self.assertTrue(result)


test_suit = unittest.TestSuite()
test_suit.addTest(unittest.makeSuite(DatabaseTestCase))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suit)