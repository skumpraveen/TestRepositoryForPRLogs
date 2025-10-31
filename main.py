#!/usr/bin/env python3
"""
Main script to demonstrate calculator functionality with logging.
"""
from calculator import Calculator


def main():
    """Run calculator demonstrations."""
    calc = Calculator()
    
    print("Calculator Demo with Logging")
    print("=" * 40)
    
    # Perform various calculations
    print(f"\n10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    
    # Try division by zero
    print("\nAttempting division by zero...")
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print("\n" + "=" * 40)
    print("Check the logs above for calculation details!")


if __name__ == "__main__":
    main()
