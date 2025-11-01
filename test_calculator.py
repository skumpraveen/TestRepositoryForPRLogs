"""
Tests for calculator module with logging verification.
"""
import unittest
import logging
from io import StringIO
from calculator import Calculator


class TestCalculatorLogging(unittest.TestCase):
    """Test calculator operations and their logging."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
        # Capture log output
        self.log_capture = StringIO()
        self.handler = logging.StreamHandler(self.log_capture)
        self.handler.setLevel(logging.DEBUG)  # Set to DEBUG to capture all levels including WARNING
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)
        
        # Get the calculator logger (using __name__ from calculator module)
        import calculator
        self.logger = logging.getLogger(calculator.__name__)
        self.logger.setLevel(logging.DEBUG)  # Set to DEBUG to ensure all levels are captured
        self.logger.addHandler(self.handler)
    
    def tearDown(self):
        """Clean up test fixtures."""
        self.logger.removeHandler(self.handler)
        self.log_capture.close()
    
    def get_log_output(self):
        """Get the captured log output."""
        return self.log_capture.getvalue()
    
    def test_add_operation(self):
        """Test addition operation."""
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)
        log_output = self.get_log_output()
        self.assertIn("Addition: 5 + 3 = 8", log_output)
        self.assertIn("INFO", log_output)
    
    def test_subtract_operation(self):
        """Test subtraction operation."""
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)
        log_output = self.get_log_output()
        self.assertIn("Subtraction: 10 - 4 = 6", log_output)
        self.assertIn("INFO", log_output)
    
    def test_multiply_operation(self):
        """Test multiplication operation."""
        result = self.calc.multiply(6, 7)
        self.assertEqual(result, 42)
        log_output = self.get_log_output()
        self.assertIn("Multiplication: 6 * 7 = 42", log_output)
        self.assertIn("INFO", log_output)
    
    def test_divide_operation(self):
        """Test division operation."""
        result = self.calc.divide(20, 4)
        self.assertEqual(result, 5.0)
        log_output = self.get_log_output()
        self.assertIn("Division: 20 / 4 = 5.0", log_output)
        self.assertIn("INFO", log_output)
    
    def test_divide_by_zero_logging(self):
        """Test that division by zero is logged as error."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
        log_output = self.get_log_output()
        self.assertIn("Division by zero attempted", log_output)
        self.assertIn("ERROR", log_output)
    
    def test_subtract_negative_result_warning(self):
        """Test that subtraction resulting in negative logs a warning."""
        result = self.calc.subtract(5, 10)
        self.assertEqual(result, -5)
        log_output = self.get_log_output()
        self.assertIn("Subtraction results in negative", log_output)
        self.assertIn("WARNING", log_output)
    
    def test_multiply_large_result_warning(self):
        """Test that multiplication with very large result logs a warning."""
        result = self.calc.multiply(1000000, 100000)
        self.assertEqual(result, 100000000000)
        log_output = self.get_log_output()
        self.assertIn("Multiplication result is very large", log_output)
        self.assertIn("WARNING", log_output)
    
    def test_divide_small_number_warning(self):
        """Test that division by very small number logs a warning."""
        result = self.calc.divide(100, 0.0001)
        self.assertEqual(result, 1000000.0)
        log_output = self.get_log_output()
        self.assertIn("Division by very small number", log_output)
        self.assertIn("WARNING", log_output)
    
    def test_divide_large_result_warning(self):
        """Test that division resulting in very large number logs a warning."""
        result = self.calc.divide(1e15, 10)
        self.assertEqual(result, 1e14)
        log_output = self.get_log_output()
        self.assertIn("Division result is very large", log_output)
        self.assertIn("WARNING", log_output)


class TestCalculatorOperations(unittest.TestCase):
    """Test basic calculator operations."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
    
    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-3, -3), 0)
    
    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(9, 3), 3.0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))


if __name__ == '__main__':
    unittest.main()
