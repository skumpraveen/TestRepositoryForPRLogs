#!/usr/bin/env python3
"""
Main script to demonstrate calculator functionality with logging.
"""
import logging
from calculator import Calculator
from logging_schema import configure_logging

# Configure logging at application entry point
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture all levels including WARNING
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


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
    
    # Demonstrate warning scenarios
    print("\n--- Warning Scenarios ---")
    print(f"\n5 - 10 = {calc.subtract(5, 10)} (Warning: results in negative)")
    print(f"1000000 * 100000 = {calc.multiply(1000000, 100000)} (Warning: very large result)")
    print(f"100 / 0.0001 = {calc.divide(100, 0.0001)} (Warning: dividing by very small number)")
    
    print("\n" + "=" * 40)
    print("Check the logs above for calculation details!")
    
    # Display calculation history
    print("\n" + "=" * 40)
    print("Calculation History:")
    print("=" * 40)
    history = calc.get_history()
    if history:
        for i, entry in enumerate(history, 1):
            print(f"{i}. {entry}")
    else:
        print("No calculations in history")
    print("=" * 40)



if __name__ == "__main__":
    main()
