"""
A simple command-line calculator module.
This module provides the `Calculator` class, which handles user input validation
for two numbers and an arithmetic operator (+, -, *, /), performs the calculation,
and outputs the result. It supports decimal inputs using either '.' or ',' as the
decimal separator.
"""

import sys
import operator

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
        operator (str): The arithmetic operator ('+', '-', '*', '/').
    """

    first_number: float = 0
    second_number: float = 0
    operator: str = ""

    @classmethod
    def set_user_input(cls) -> None:
        """Prompting the user, validating and setting the user inputs.

        Prompt the user for two numbers and an arithmetic operator.
        Validates that inputs are provided, converts comma decimals to periods,
        ensures numbers are valid floats, and restricts the operator to '+', '-',
        '*', or '/'. Exits with an error message if validation fails.
        Updates:
            cls.first_number (float): The validated first number.
            cls.second_number (float): The validated second number.
            cls.operator (str): The validated operator.
        """

        # Validating first number
        first_number = input("Type your first number: ")

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

        if not user_selected_operator:
            print("Error: operator is missing")
            sys.exit(1)

        if user_selected_operator not in ("+", "-", "*", "/"):
            print('Error: Select between "+", "-", "*", "/"')
            sys.exit(1)

        try:
            cls.operator = user_selected_operator
        except ValueError as e:
            print(f"Validation failed ({e})")
            sys.exit(1)

        # Validating second number
        second_number = input("Type your second number: ")

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
            "/": operator.truediv
        }

        if cls.operator == "/" and cls.first_number == 0.0 or cls.second_number == 0:
            print("Error: Can't devide by 0")
            sys.exit(1)

        op_func = operations[cls.operator]

        result = op_func(cls.first_number, cls.second_number)

        return float(result)


    @classmethod
    def run_calculator(cls) -> None:
        """
        Orchestrate the calculator workflow.
        Calls `set_user_input` to gather and validate data, then calls `calculator`
        to compute the result and prints it to the console.
        """
        cls.set_user_input()
        result = cls.calculator()

        print(result)


if __name__ == "__main__":
    Calculator.run_calculator()
