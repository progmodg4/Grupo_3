from modulo_de_alteracao_t import *
import unittest

class TestStringMethods(unittest.TestCase):
    def test_01_inserir_produto_ok_com_sucesso(self):
        print("Caso de Teste 01 - Verifica inserção")
        r = insere_aux(11,"testes",10,1)
        assert r==0

    def test_02_inserir_produto_nok_num_ja_existe(self):
        print("Caso de Teste 02 - Impede a inserção caso " + "já existe codigo inserido")
        r = insere_aux(11,"teste 2",10,1)
        assert r==1

    def test_03_inserir_produto_nok_nome_ja_existe(self):
        print("Caso de Teste 03 - Impede a inserção caso " + "já existe nome inserido")
        r = insere_aux(12,"testes",10,1)
        assert r==1

    def test_04_altera_nome_produto_ok_com_sucesso(self):
        print("Caso de Teste 04 - Verifica alterar nome")
        r = atualiza_nome_aux(1,"testes1")
        assert r==0

    def test_05_altera_nome_produto_nok_nome_ja_existe(self):
        print("Caso de Teste 05 - Impede a alteracao caso " + "já existe nome inserido")
        r = atualiza_nome_aux(1,"testes")
        assert r==1

    def test_06_altera_nome_produto_nok_codigo_nao_existe(self):
        print("Caso de Teste 06 - Impede a alteracao caso " + "codigo não exista")
        r = atualiza_nome_aux(42,"testes2")
        assert r==1

    def test_07_altera_qtd_produto_ok_com_sucesso(self):
        print("Caso de Teste 07 - Verifica alterar quantidade")
        r = atualiza_qtd_aux(1,2)
        assert r==0

    def test_08_altera_qtd_produto_nok_codigo_nao_existe(self):
        print("Caso de Teste 08 - Impede a alteracao caso " + "codigo não exista")
        r = atualiza_qtd_aux(42,123)
        assert r==1

    def test_09_altera_preco_produto_ok_com_sucesso(self):
        print("Caso de Teste 09 - Verifica alterar preço")
        r = atualiza_preco_aux(1,25)
        assert r==0

    def test_10_altera_preco_produto_nok_codigo_nao_existe(self):
        print("Caso de Teste 08 - Impede a alteracao caso " + "codigo não exista")
        r = atualiza_preco_aux(42,"testes2")
        assert r==1

    def test_11_remove_produto_ok_com_sucesso(self):
        print("Caso de Teste 11 - Verifica remoção")
        r = remove_aux(11)
        assert r==0

    def test_12_remove_produto_nok_codigo_nao_existe(self):
        print("Caso de Teste 12 - Impede remoção caso codigo não exista")
        r = remove_aux(11)
        assert r==1
    

if __name__ == '__main__':
    unittest.main()
