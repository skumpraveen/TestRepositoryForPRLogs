"""
Simple calculator module with logging support.
"""
import logging

logger = logging.getLogger(__name__)

# Constants for warning thresholds
LARGE_RESULT_THRESHOLD = 1e10
SMALL_NUMBER_THRESHOLD = 0.001


class Calculator:
    """A simple calculator with logging for all operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        result = a + b
        logger.info(f"Addition: {a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract b from a."""
        result = a - b
        
        # Warning when subtracting a larger number from a smaller positive number
        if a > 0 and b > a:
            logger.warning(f"Subtraction results in negative: {a} - {b} = {result}")
        
        logger.info(f"Subtraction: {a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        result = a * b
        
        # Warning for very large results
        if abs(result) > LARGE_RESULT_THRESHOLD:
            logger.warning(f"Multiplication result is very large: {result}, precision may be affected")
        
        logger.info(f"Multiplication: {a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            logger.error(f"Division by zero attempted: {a} / {b}")
            raise ValueError("Cannot divide by zero")
        
        # Warning for division by very small numbers
        if abs(b) < SMALL_NUMBER_THRESHOLD and b != 0:
            logger.warning(f"Division by very small number: {a} / {b} may cause precision issues")
        
        result = a / b
        
        # Warning for very large results
        if abs(result) > LARGE_RESULT_THRESHOLD:
            logger.warning(f"Division result is very large: {result}, precision may be affected")
        
        logger.info(f"Division: {a} / {b} = {result}")
        return result
