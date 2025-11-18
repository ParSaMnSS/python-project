from pathlib import Path
from operations import FileOperation

class FileManager:
    """Manages file operations in a specific directory."""

    def __init__(self, directory: str):
        self.directory = Path(directory)
        if not self.directory.is_dir():
            raise NotADirectoryError(f"'{directory}' is not a valid directory.")

    def get_files(self) -> list[Path]:
        """Returns a list of files in the directory."""
        return [f for f in self.directory.iterdir() if f.is_file()]

    def execute_operation(self, operation: FileOperation):
        """Executes a given file operation."""
        files = self.get_files()
        operation.execute(files)
