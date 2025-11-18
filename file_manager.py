from pathlib import Path
from operations import FileOperation

class FileManager:
    """Manages file operations in a specific directory."""

    def __init__(self, directory: str):
        self.directory = Path(directory)
        if not self.directory.is_dir():
            raise NotADirectoryError(f"'{directory}' is not a valid directory.")

    def get_files(self, extension_filter: str | None = None) -> list[Path]:
        """Returns a list of files in the directory, with an optional filter."""
        files = [f for f in self.directory.iterdir() if f.is_file()]
        if extension_filter:
            return [f for f in files if f.suffix == extension_filter]
        return files

    def execute_operation(self, operation: FileOperation, extension_filter: str | None = None):
        """Executes a given file operation on filtered files."""
        files = self.get_files(extension_filter)
        if not files:
            print("No files found matching the filter.")
            return
        operation.execute(files)
