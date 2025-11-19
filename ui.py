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
        print("4. Archive files")
        
        while True:
            choice = input("Enter the number of the operation you want to perform: ")
            if choice in ['1', '2', '3', '4']:
                return choice
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")

    def get_sort_key(self) -> str:
        """Prompts the user for a valid sort key."""
        print("\nSort by:")
        print("1. Name")
        print("2. Date")
        print("3. Size")
        print("4. Extension")
        
        key_map = {'1': 'name', '2': 'date', '3': 'size', '4': 'extension'}
        
        while True:
            choice = input("Enter the number for the sort key: ")
            if choice in key_map:
                return key_map[choice]
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")

    def get_renaming_pattern(self) -> str:
        """Prompts the user for a renaming pattern."""
        print("\nEnter the renaming pattern.")
        print("You can use the following placeholders:")
        print("  {index} - The file number (e.g., 1, 2, 3)")
        print("  {name}  - The original file name (without extension)")
        print("  {ext}   - The original file extension (e.g., .txt)")
        return input("Pattern: ")

    def get_organizer_strategy(self) -> str:
        """Prompts the user for a valid organization strategy."""
        print("\nOrganize by:")
        print("1. Extension")
        print("2. Date")
        
        strategy_map = {'1': 'extension', '2': 'date'}
        
        while True:
            choice = input("Enter the number for the organization strategy: ")
            if choice in strategy_map:
                return strategy_map[choice]
            else:
                print("Invalid choice. Please enter a number from 1 to 2.")

    def get_file_filter(self) -> str | None:
        """Asks the user if they want to filter files and gets the filter."""
        while True:
            choice = input("Do you want to filter files by extension? (y/n): ").lower()
            if choice in ['y', 'n']:
                break
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")
        
        if choice == 'y':
            return input("Enter the file extension to filter by (e.g., '.pdf'): ")
        else:
            return None
