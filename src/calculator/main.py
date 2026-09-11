"""A simple command-line calculator module.
This module provides the `Calculator` class, which handles user input validation,
performs arithmetic calculations (addition, subtraction, multiplication, division,
power, and square root), and outputs the result. It supports decimal inputs using
either '.' or ',' as the decimal separator.
"""

import math
import operator
import os
from subprocess import call
import sys
import time

class Calculator:
    """Class which holds all the methods.

    A class-based calculator that processes two numbers and an operator.
    This class uses class attributes to store the first number, second number,
    and the selected operator. It provides methods to validate user input,
    perform arithmetic operations using the `operator` module, and run the
    calculation flow.

    Attributes:
        first_number (float): The first operand for the calculation.
        second_number (float): The second operand for the calculation.
        selected_operator (str): The arithmetic operator ('+', '-', '*', '/', '**', 'sqrt').
        run (bool): The state which determines if the app should run or not.
    """


    first_number: float = 0
    second_number: float = 0
    selected_operator: str = ""
    run: bool = True


    @classmethod
    def instructions(cls) -> None:
        """Formats and prints user instructions.

        Display usage instructions to the user with formatted text.
        Prints a multi-line string explaining how to input numbers, select operators
        (+, -, *, /, ** or sqrt), and exit the application by typing 'q'. Uses ANSI escape codes
        for bold formatting.
        """

        BOLD_START = "\033[1m"
        END = "\033[0m"

        print(
            "How to use:\n\n"
            "\t1. select a number, it can be integer or decimal\n"
            f"\t2. select an operator, it can be {BOLD_START}+, {BOLD_START}-{END}, "
            f"\t{BOLD_START}*{END}, {BOLD_START}/{END}, {BOLD_START}**{END} or "
            f"{BOLD_START}sqrt{END}\n"
            "\t3. If you did not chose sqrt or power,\n"
            "\tselect the next number, which also can be an integer or a decimal.\n"
            f"\tYou can type {BOLD_START}q{END} to exit the app.\n"
        )

    @classmethod
    def set_user_input(cls) -> None:
        """Prompt the user for two numbers and an arithmetic operator.
        Validates that inputs are provided, converts comma decimals to periods,
        ensures numbers are valid floats, and restricts the operator to '+', '-',
        '*', '/', '**', or 'sqrt'.
        Allows the user to exit the application by typing 'q' at any
        input prompt, which sets `cls.run` to False. Exits with an error message if
        validation fails for non-exit inputs.
        Updates:
            cls.first_number (float): The validated first number.
            cls.second_number (float): The validated second number.
            cls.selected_operator (str): The validated operator.
            cls.run (bool): Set to False if the user chooses to exit.

        Raises:
            SystemExit: If invalid inputs are given, it exits the app.
        """

        # Validating first number
        first_number = input("Type your first number: ")

        if first_number.lower() == "q":
            cls.run = False
            print("Closing the app...")
            return

        if not first_number:
            print("Error: first number is missing")
            sys.exit(1)

        if "," in first_number:
            first_number = first_number.replace(",", ".")

        try:
            cls.first_number = float(first_number)
        except ValueError as e:
            print(f"The first number has to be an integer or a decimal ({e})")
            sys.exit(1)


        # Validating operator
        user_selected_operator = input("Type an operator: ")

        if user_selected_operator.lower() == "q":
            cls.run = False
            print("Closing the app...")
            return

        if not user_selected_operator:
            print("Error: operator is missing")
            sys.exit(1)

        if user_selected_operator not in ("+", "-", "*", "/", "**", "sqrt"):
            print('Error: Select between "+", "-", "*", "/"', "**", "sqrt")
            sys.exit(1)

        try:
            cls.selected_operator = user_selected_operator
        except ValueError as e:
            print(f"Validation failed ({e})")
            sys.exit(1)

        # If sqrt we do not need a second number
        if cls.selected_operator == "sqrt":
            return

        # Validating second number
        second_number = input("Type your second number: ")

        if second_number.lower() == "q":
            cls.run = False
            print("Closing the app...")
            return

        if "," in second_number:
            second_number = second_number.replace(",", ".")

        if not second_number:
            print("Error: second number is missing")
            sys.exit(1)

        try:
            cls.second_number = float(second_number)
        except ValueError as e:
            print(f"The second number has to be an integer or a decimal ({e})")
            sys.exit(1)

    @classmethod
    def calculator(cls) -> float:
        """Performs the calculation.
        Perform the arithmetic operation based on the stored operator and numbers.
        Uses the `operator` module to execute addition, subtraction, multiplication,
        or true division. Checks for division by zero before executing.
        
        Returns:
            float: The result of the calculation.
            
        Raises:
            SystemExit: If division by zero is attempted.
        """

        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "**": operator.pow
        }

        if cls.selected_operator == "sqrt":
            result = math.sqrt(cls.first_number)
            return float(result)


        if cls.selected_operator == "/" and cls.first_number == 0.0 or cls.second_number == 0:
            print("Error: Can't devide by 0")
            sys.exit(1)

        op_func = operations[cls.selected_operator]
        result = op_func(cls.first_number, cls.second_number)
        return float(result)


    @classmethod
    def run_calculator(cls) -> None:
        """Orchestrates the calculator workflow.

        Calls `set_user_input` to gather and validate data, then calls `calculator`.
        If the user enters 'q' during input, the loop terminates gracefully.
        Otherwise, it computes the result, prints it, and waits before repeating.
        """

        while cls.run is True:
            call('cls' if os.name == 'nt' else 'clear')

            cls.instructions()
            cls.set_user_input()

            if not cls.run:
                break

            result = cls.calculator()
            print(result)
            time.sleep(3)


if __name__ == "__main__":
    Calculator.run_calculator()
