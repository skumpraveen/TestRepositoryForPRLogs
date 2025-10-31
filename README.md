# TestRepositoryForPRLogs
A test repository with a simple calculator that includes logging for all calculations.

## Features

- Simple calculator with basic operations: addition, subtraction, multiplication, and division
- **Comprehensive logging** for all calculation operations
- Error logging for invalid operations (e.g., division by zero)
- Complete test suite to verify functionality

## Calculator Operations

The calculator supports the following operations:
- **Addition**: `add(a, b)` - Adds two numbers
- **Subtraction**: `subtract(a, b)` - Subtracts b from a
- **Multiplication**: `multiply(a, b)` - Multiplies two numbers
- **Division**: `divide(a, b)` - Divides a by b (with zero-division protection)

## Logging

The repository uses a **differentiated logging schema** that clearly distinguishes between Information logs and Error logs:

### Logging Schema Features

- **Information Logs (INFO)**: Prefixed with `[INFO]` for clear identification of successful operations
- **Error Logs (ERROR)**: Prefixed with `[ERROR]` and marked with ⚠️ emoji for high visibility of failures
- **Timestamps**: All logs include precise timestamps
- **Module Names**: Logger names identify the source of each log entry
- **Detailed Messages**: Operation details, operands, and results

### Log Format Examples

**Information Log:**
```
[INFO] 2025-10-31 19:38:53,726 - calculator - Addition: 10 + 5 = 15
```

**Error Log:**
```
[ERROR] 2025-10-31 19:38:53,726 - calculator - ⚠️  Division by zero attempted: 10 / 0
```

### Using the New Logging Schema

The logging schema is configured automatically when running the application:

```python
from logging_schema import configure_logging
import logging

# Configure logging with the differentiated schema
configure_logging(level=logging.INFO)
```

All calculations are automatically logged with the appropriate format:
- **Successful operations** use the INFO schema
- **Errors and failures** use the ERROR schema with enhanced visibility

## Usage

### Running the Demo

```bash
python3 main.py
```

This will demonstrate all calculator operations with their corresponding logs.

### Using the Calculator in Code

```python
from calculator import Calculator

calc = Calculator()

# All operations are automatically logged
result = calc.add(10, 5)      # Logs: Addition: 10 + 5 = 15
result = calc.subtract(10, 5) # Logs: Subtraction: 10 - 5 = 5
result = calc.multiply(10, 5) # Logs: Multiplication: 10 * 5 = 50
result = calc.divide(10, 5)   # Logs: Division: 10 / 5 = 2.0
```

## Testing

Run the test suite to verify calculator functionality and logging:

```bash
python3 -m unittest test_calculator.py -v
```

The test suite includes:
- Tests for all basic calculator operations
- Verification that calculations are properly logged
- Tests for error handling and error logging
