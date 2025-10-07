from src.Operaciones import Operaciones
import pytest

class TestOperaciones:
    
    op = Operaciones()
    '''
    @pytest.fixture(scope="module")
    def datos():
        return {
            "aa": 2, 
            "bb": 3
        }
    '''
    def test_sumar(self):
        print("Ejecutando test_sumar")
        assert self.op.sumar(2, 3) == 5, "Validando"
        assert self.op.sumar(-1, 1) == 0
        assert self.op.sumar(-1, -1) == -2

    def test_restar(self):
        assert self.op.restar(5, 3) == 2
        assert self.op.restar(0, 0) == 0
        assert self.op.restar(-1, -1) == 0

    def test_multiplicar(self):
        assert self.op.multiplicar(2, 3) == 6
        assert self.op.multiplicar(-1, 1) == -1
        assert self.op.multiplicar(-1, -1) == 1  

    def test_dividir(self):
        assert self.op.dividir(6, 3) == 2
        assert self.op.dividir(-6, -3) == 2
        assert self.op.dividir(-6, 3) == -2
        try:
            self.op.dividir(5, 0)
            assert False, "Expected ValueError"
        except ValueError:
            pass

    def test_dividir_floats(self):
        assert self.op.dividir(5.0, 2.0) == 2.5
        assert self.op.dividir(-5.0, -2.0) == 2.5
        assert self.op.dividir(-5.0, 2.0) == -2.5
        try:
            self.op.dividir(5.0, 0.0)
            assert False, "Expected ValueError"
        except ValueError:
            pass

    def test_sumar_floats(self):
        assert self.op.sumar(2.5, 3.5) == 6.0
        assert self.op.sumar(-1.5, 1.5) == 0.0
        assert self.op.sumar(-1.5, -1.5) == -3.0

    def test_restar_floats(self):
        assert self.op.restar(5.5, 3.5) == 2.0
        assert self.op.restar(0.0, 0.0) == 0.0
        assert self.op.restar(-1.5, -1.5) == 0.0

    def test_multiplicar_floats(self):
        assert self.op.multiplicar(2.5, 3.5) == 8.75
        assert self.op.multiplicar(-1.5, 1.5) == -2.25
        assert self.op.multiplicar(-1.5, -1.5) == 2.25

    def test_multiplicar_por_cero(self):
        assert self.op.multiplicar(0, 5) == 0
        assert self.op.multiplicar(5, 0) == 0
        assert self.op.multiplicar(0, 0) == 0

    def test_sumar_ceros(self):
        assert self.op.sumar(0, 0) == 0
        assert self.op.sumar(0, 5) == 5
        assert self.op.sumar(5, 0) == 5