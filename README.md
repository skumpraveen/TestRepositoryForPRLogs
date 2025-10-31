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

All calculations are automatically logged with the following information:
- **Timestamp**: When the calculation was performed
- **Operation**: The type of calculation (addition, subtraction, etc.)
- **Operands**: The input values
- **Result**: The calculated result
- **Level**: 
  - **INFO** for successful operations
  - **WARNING** for operations that may have issues (e.g., division by very small numbers, very large results, unexpected negative results)
  - **ERROR** for failures (e.g., division by zero)

Example log output:
```
2025-10-31 13:17:46,472 - calculator - INFO - Addition: 10 + 5 = 15
2025-10-31 13:17:46,472 - calculator - INFO - Subtraction: 10 - 5 = 5
2025-10-31 13:17:46,473 - calculator - WARNING - Subtraction results in negative: 5 - 10 = -5
2025-10-31 13:17:46,474 - calculator - WARNING - Multiplication result is very large: 100000000000, precision may be affected
2025-10-31 13:17:46,475 - calculator - ERROR - Division by zero attempted: 10 / 0
```

### Warning Scenarios

The calculator logs warnings for the following situations:
- **Division by very small numbers** (absolute value < 0.001): May cause precision issues
- **Very large results** (absolute value > 10^10): Precision may be affected
- **Negative results from positive operands**: When subtracting a larger number from a smaller positive number

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
