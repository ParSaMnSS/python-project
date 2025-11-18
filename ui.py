from pathlib import Path

class UserInterface:
    """Handles command-line user interactions."""

    def get_target_directory(self) -> str:
        """Prompts the user for a directory path and validates it."""
        while True:
            path_str = input("Enter the target directory path: ")
            path = Path(path_str)
            if path.is_dir():
                return path_str
            else:
                print("Invalid directory path. Please try again.")

    def get_operation_choice(self) -> str:
        """Displays a menu of operations and returns the user's choice."""
        print("\nAvailable Operations:")
        print("1. Sort files")
        print("2. Rename files")
        print("3. Organize files")
        
        while True:
            choice = input("Enter the number of the operation you want to perform: ")
            if choice in ['1', '2', '3']:
                return choice
            else:
                print("Invalid choice. Please enter a number from 1 to 3.")
