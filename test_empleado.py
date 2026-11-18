import unittest
from empleado import Empleado

class TestEmpleado(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Empleado("Jonathan", "Aceves", 50000)
        self.emp_2 = Empleado("Maria", "Lopez", 60000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, "jonathan.aceves@empresa.com")
        self.assertEqual(self.emp_2.email, "maria.lopez@empresa.com")

    def test_nombre_completo(self):
        self.assertEqual(self.emp_1.nombre_completo, "Jonathan Aceves")
        self.assertEqual(self.emp_2.nombre_completo, "Maria Lopez")

    def test_aplicar_aumento(self):
        self.emp_1.aplicar_aumento(0.10)
        self.emp_2.aplicar_aumento(0.05)
        self.assertEqual(self.emp_1.salario, 55000)
        self.assertEqual(self.emp_2.salario, 63000)

    def test_aumento_negativo(self):
        with self.assertRaises(ValueError):
            self.emp_1.aplicar_aumento(-0.05)

if __name__ == "__main__":
    unittest.main()
