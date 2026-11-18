import unittest
import operaciones

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(operaciones.sumar(5, 3), 8)
        self.assertEqual(operaciones.sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(operaciones.restar(10, 4), 6)
        self.assertEqual(operaciones.restar(0, 5), -5)

    def test_multiplicar(self):
        self.assertEqual(operaciones.multiplicar(3, 4), 12)
        self.assertEqual(operaciones.multiplicar(-2, 3), -6)

    def test_dividir_exitoso(self):
        self.assertEqual(operaciones.dividir(10, 2), 5.0)
        self.assertAlmostEqual(operaciones.dividir(1, 3), 0.3333333, places=6)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            operaciones.dividir(10, 0)

    def test_es_par(self):
        self.assertTrue(operaciones.es_par(4))
        self.assertFalse(operaciones.es_par(7))

    def test_validar_edad_excepciones(self):
        with self.assertRaises(TypeError):
            operaciones.validar_edad("dieciocho")
        with self.assertRaises(ValueError):
            operaciones.validar_edad(-5)

if __name__ == "__main__":
    unittest.main()
