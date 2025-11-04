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


class TestCalculatorHistory(unittest.TestCase):
    """Test calculator history tracking."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_history_initialized_empty(self):
        """Test that history is empty on initialization."""
        history = self.calc.get_history()
        self.assertEqual(len(history), 0)
        self.assertIsInstance(history, list)
    
    def test_history_tracks_addition(self):
        """Test that addition is tracked in history."""
        self.calc.add(5, 3)
        history = self.calc.get_history()
        self.assertEqual(len(history), 1)
        self.assertIn("5 + 3 = 8", history[0])
    
    def test_history_tracks_subtraction(self):
        """Test that subtraction is tracked in history."""
        self.calc.subtract(10, 4)
        history = self.calc.get_history()
        self.assertEqual(len(history), 1)
        self.assertIn("10 - 4 = 6", history[0])
    
    def test_history_tracks_multiplication(self):
        """Test that multiplication is tracked in history."""
        self.calc.multiply(6, 7)
        history = self.calc.get_history()
        self.assertEqual(len(history), 1)
        self.assertIn("6 * 7 = 42", history[0])
    
    def test_history_tracks_division(self):
        """Test that division is tracked in history."""
        self.calc.divide(20, 4)
        history = self.calc.get_history()
        self.assertEqual(len(history), 1)
        self.assertIn("20 / 4 = 5.0", history[0])
    
    def test_history_tracks_multiple_operations(self):
        """Test that multiple operations are tracked in order."""
        self.calc.add(10, 5)
        self.calc.subtract(10, 3)
        self.calc.multiply(4, 5)
        self.calc.divide(20, 4)
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 4)
        self.assertIn("10 + 5 = 15", history[0])
        self.assertIn("10 - 3 = 7", history[1])
        self.assertIn("4 * 5 = 20", history[2])
        self.assertIn("20 / 4 = 5.0", history[3])
    
    def test_history_tracks_division_by_zero_error(self):
        """Test that division by zero error is tracked in history."""
        try:
            self.calc.divide(10, 0)
        except ValueError:
            pass
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 1)
        self.assertIn("10 / 0 = Error: Division by zero", history[0])
    
    def test_clear_history(self):
        """Test that clear_history removes all entries."""
        self.calc.add(5, 3)
        self.calc.subtract(10, 4)
        self.calc.multiply(6, 7)
        
        self.assertEqual(len(self.calc.get_history()), 3)
        
        self.calc.clear_history()
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 0)
    
    def test_get_history_returns_copy(self):
        """Test that get_history returns a copy, not the original list."""
        self.calc.add(5, 3)
        history1 = self.calc.get_history()
        history1.append("Modified externally")
        
        history2 = self.calc.get_history()
        self.assertEqual(len(history2), 1)
        self.assertNotIn("Modified externally", history2)


if __name__ == '__main__':
    unittest.main()
