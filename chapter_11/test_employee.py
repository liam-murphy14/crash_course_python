import unittest
import employee 

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee_0 = employee.Employee("jason", "derulo", 25_000)
    
    def test_default_raise(self):
        initial_salary = self.employee_0.salary
        self.employee_0.give_raise()
        self.assertEqual(self.employee_0.salary, initial_salary + 5_000)
    
    def test_custom_raise(self):
        initial_salary = self.employee_0.salary
        raise_amt = 3_500
        self.employee_0.give_raise(raise_amt)
        self.assertEqual(self.employee_0.salary, initial_salary + raise_amt)


if __name__ == "__main__":
    unittest.main()