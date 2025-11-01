"""
Tests for the new logging schema that differentiates Information and Error logs.
"""
import unittest
import logging
from io import StringIO
import calculator
from logging_schema import DifferentiatedLogFormatter, configure_logging


class TestDifferentiatedLogFormatter(unittest.TestCase):
    """Test the custom log formatter."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.formatter = DifferentiatedLogFormatter()
        self.logger = logging.getLogger('test_logger')
        self.logger.setLevel(logging.INFO)
        
        # Capture log output
        self.log_capture = StringIO()
        self.handler = logging.StreamHandler(self.log_capture)
        self.handler.setLevel(logging.INFO)
        self.handler.setFormatter(self.formatter)
        
        # Clear existing handlers and add our test handler
        self.logger.handlers.clear()
        self.logger.addHandler(self.handler)
    
    def tearDown(self):
        """Clean up test fixtures."""
        self.logger.removeHandler(self.handler)
        self.log_capture.close()
    
    def get_log_output(self):
        """Get the captured log output."""
        return self.log_capture.getvalue()
    
    def test_info_log_format(self):
        """Test that INFO logs have the correct format with [INFO] prefix."""
        self.logger.info("Test information message")
        log_output = self.get_log_output()
        
        # Verify [INFO] prefix is present
        self.assertIn("[INFO]", log_output)
        # Verify the message is present
        self.assertIn("Test information message", log_output)
        # Verify logger name is present
        self.assertIn("test_logger", log_output)
        # Verify ERROR markers are NOT present
        self.assertNotIn("[ERROR]", log_output)
        self.assertNotIn("⚠️", log_output)
    
    def test_error_log_format(self):
        """Test that ERROR logs have the correct format with [ERROR] prefix and warning emoji."""
        self.logger.error("Test error message")
        log_output = self.get_log_output()
        
        # Verify [ERROR] prefix is present
        self.assertIn("[ERROR]", log_output)
        # Verify warning emoji is present
        self.assertIn("⚠️", log_output)
        # Verify the message is present
        self.assertIn("Test error message", log_output)
        # Verify logger name is present
        self.assertIn("test_logger", log_output)
    
    def test_info_and_error_differentiation(self):
        """Test that INFO and ERROR logs are clearly differentiated."""
        self.logger.info("Information log")
        self.logger.error("Error log")
        log_output = self.get_log_output()
        
        # Both types should be present
        self.assertIn("[INFO]", log_output)
        self.assertIn("[ERROR]", log_output)
        
        # Split by lines to verify format per line
        lines = log_output.strip().split('\n')
        self.assertEqual(len(lines), 2)
        
        # First line should be INFO
        self.assertIn("[INFO]", lines[0])
        self.assertIn("Information log", lines[0])
        self.assertNotIn("⚠️", lines[0])
        
        # Second line should be ERROR
        self.assertIn("[ERROR]", lines[1])
        self.assertIn("⚠️", lines[1])
        self.assertIn("Error log", lines[1])


class TestConfigureLogging(unittest.TestCase):
    """Test the configure_logging function."""
    
    def test_configure_logging_creates_formatter(self):
        """Test that configure_logging creates and returns a DifferentiatedLogFormatter."""
        formatter = configure_logging()
        self.assertIsInstance(formatter, DifferentiatedLogFormatter)
    
    def test_configure_logging_sets_level(self):
        """Test that configure_logging properly sets the logging level."""
        configure_logging(level=logging.DEBUG)
        root_logger = logging.getLogger()
        self.assertEqual(root_logger.level, logging.DEBUG)
        
        # Reset to INFO for other tests
        configure_logging(level=logging.INFO)
    
    def test_configure_logging_adds_handler(self):
        """Test that configure_logging adds a handler to the root logger."""
        configure_logging()
        root_logger = logging.getLogger()
        
        # Should have at least one handler
        self.assertGreater(len(root_logger.handlers), 0)
        
        # At least one handler should use our custom formatter
        has_custom_formatter = any(
            isinstance(handler.formatter, DifferentiatedLogFormatter)
            for handler in root_logger.handlers
        )
        self.assertTrue(has_custom_formatter)


class TestLoggingSchemaIntegration(unittest.TestCase):
    """Integration tests with the calculator module."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Configure logging with our new schema
        configure_logging(level=logging.INFO)
        
        # Capture log output
        self.log_capture = StringIO()
        self.handler = logging.StreamHandler(self.log_capture)
        self.handler.setLevel(logging.INFO)
        
        # Use the custom formatter
        formatter = DifferentiatedLogFormatter()
        self.handler.setFormatter(formatter)
        
        # Add handler to calculator logger
        self.calc_logger = logging.getLogger(calculator.__name__)
        self.calc_logger.addHandler(self.handler)
    
    def tearDown(self):
        """Clean up test fixtures."""
        self.calc_logger.removeHandler(self.handler)
        self.log_capture.close()
    
    def get_log_output(self):
        """Get the captured log output."""
        return self.log_capture.getvalue()
    
    def test_calculator_info_logs_use_new_schema(self):
        """Test that calculator INFO logs use the new schema."""
        from calculator import Calculator
        calc = Calculator()
        calc.add(5, 3)
        
        log_output = self.get_log_output()
        self.assertIn("[INFO]", log_output)
        self.assertIn("Addition: 5 + 3 = 8", log_output)
    
    def test_calculator_error_logs_use_new_schema(self):
        """Test that calculator ERROR logs use the new schema."""
        from calculator import Calculator
        calc = Calculator()
        
        try:
            calc.divide(10, 0)
        except ValueError:
            pass  # Expected
        
        log_output = self.get_log_output()
        self.assertIn("[ERROR]", log_output)
        self.assertIn("⚠️", log_output)
        self.assertIn("Division by zero attempted", log_output)


if __name__ == '__main__':
    unittest.main()
