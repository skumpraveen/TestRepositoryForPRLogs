"""
Simple calculator module with logging support.
"""
import logging

logger = logging.getLogger(__name__)


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
        logger.info(f"Subtraction: {a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        result = a * b
        logger.info(f"Multiplication: {a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            logger.error(f"Division by zero attempted: {a} / {b}")
            raise ValueError("Cannot divide by zero")
        result = a / b
        logger.info(f"Division: {a} / {b} = {result}")
        return result
