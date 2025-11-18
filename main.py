from file_manager import FileManager
from operations import Sorter, Renamer, Organizer
from ui import UserInterface

def main():
    """Main function to run the file management tool."""
    ui = UserInterface()
    
    try:
        directory = ui.get_target_directory()
        file_manager = FileManager(directory)
        
        extension_filter = ui.get_file_filter()
        
        choice = ui.get_operation_choice()
        
        operation = None
        if choice == '1':
            sort_key = ui.get_sort_key()
            operation = Sorter(sort_key=sort_key)
        elif choice == '2':
            pattern = ui.get_renaming_pattern()
            operation = Renamer(pattern)
        elif choice == '3':
            strategy = ui.get_organizer_strategy()
            operation = Organizer(strategy=strategy)
        
        if operation:
            file_manager.execute_operation(operation, extension_filter)
            print("\nOperation completed successfully.")

    except NotADirectoryError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

