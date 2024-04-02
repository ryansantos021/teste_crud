import unittest 
from unittest.mock import patch 
from CRUD import UsersCRUD 
import coverage 
import webbrowser 
import os 

 
class TestUsersCRUD(unittest.TestCase): 
    def setUp(self):  
        self.crud = UsersCRUD() 
        self.crud.create_user("Alice", 25) 
        self.crud.create_user("Bob", 30) 
        self.crud.create_user("Charlie", 20)

    def test_read_users(self): 
        self.crud.read_users()

    def test_update_user(self): 
        self.crud.update_user(0,'Ryan',26)

    def test_update_user_invalid_index(self):
        self.crud.update_user(4,'Ryan',26)
    
    def test_delete_user(self):
        self.crud.delete_user(0)

    def test_delete_user_invalid_index(self): 
        self.crud.delete_user(4)


if __name__ == '__main__': 
    # Criar uma instância do Coverage com o arquivo .coveragerc 
    cov = coverage.Coverage(config_file='.coveragerc.txt') 

    # Iniciar a medição da cobertura 
    cov.start() 

    # Executar os testes 
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUsersCRUD) 
    unittest.TextTestRunner(verbosity=2).run(suite) 

    # Encerrar a medição da cobertura após os testes 
    cov.stop() 

    # Salvar os dados de cobertura em um arquivo 
    cov.save() 
    cov.html_report(directory='htmlcov') 

    # Abra o relatório no navegador 
    index_file = os.path.join('htmlcov', 'index.html') 
    webbrowser.open('file://' + os.path.abspath(index_file)) 

 

 