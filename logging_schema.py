"""
Custom logging schema that clearly differentiates Information and Error logs.
"""
import logging


class DifferentiatedLogFormatter(logging.Formatter):
    """
    Custom formatter that provides clear visual distinction between 
    Information logs and Error logs.
    
    Information logs are prefixed with [INFO] and use a standard format.
    Error logs are prefixed with [ERROR] and include additional markers for visibility.
    """
    
    # Format templates for different log levels
    INFO_FORMAT = '[INFO] %(asctime)s - %(name)s - %(message)s'
    ERROR_FORMAT = '[ERROR] %(asctime)s - %(name)s - ⚠️  %(message)s'
    DEFAULT_FORMAT = '[%(levelname)s] %(asctime)s - %(name)s - %(message)s'
    
    def format(self, record):
        """
        Format the log record based on its level.
        
        Args:
            record: LogRecord instance to format
            
        Returns:
            Formatted log string with appropriate schema
        """
        # Store original format
        original_format = self._style._fmt
        
        # Apply different format based on log level
        if record.levelno == logging.INFO:
            self._style._fmt = self.INFO_FORMAT
        elif record.levelno == logging.ERROR:
            self._style._fmt = self.ERROR_FORMAT
        else:
            self._style._fmt = self.DEFAULT_FORMAT
        
        # Format the record
        result = logging.Formatter.format(self, record)
        
        # Restore original format
        self._style._fmt = original_format
        
        return result


def configure_logging(level=logging.INFO):
    """
    Configure logging with the differentiated schema.
    
    Args:
        level: The logging level to use (default: logging.INFO)
        
    Returns:
        The configured formatter instance
    """
    # Create custom formatter
    formatter = DifferentiatedLogFormatter()
    
    # Get root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    
    # Remove existing handlers to avoid duplicates
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Create and configure console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    
    # Add handler to root logger
    root_logger.addHandler(console_handler)
    
    return formatter
