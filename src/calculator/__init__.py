"""Main entry point for this uv project."""

from .main import Calculator

def main() -> None:
    """Entry point for the script."""
    Calculator.run_calculator()

__all__ = ["Calculator", "main"]
