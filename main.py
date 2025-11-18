from file_manager import FileManager
from operations import Sorter, Renamer, Organizer
from ui import UserInterface

def main():
    """Main function to run the file management tool."""
    ui = UserInterface()
    
    try:
        directory = ui.get_target_directory()
        file_manager = FileManager(directory)
        
        choice = ui.get_operation_choice()
        
        if choice == '1':
            # For now, let's use a default sort key.
            # This can be expanded to ask the user for the sort key.
            operation = Sorter(sort_key='name')
        elif choice == '2':
            # Example pattern. This should be requested from the user.
            pattern = input("Enter the renaming pattern (e.g., 'new_file_{index}.txt'): ")
            operation = Renamer(pattern)
        elif choice == '3':
            # Default organization strategy.
            operation = Organizer(strategy='extension')
        
        file_manager.execute_operation(operation)
        print("\nOperation completed successfully.")

    except NotADirectoryError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

