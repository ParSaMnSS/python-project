from abc import ABC, abstractmethod
import os
import shutil
from pathlib import Path
from datetime import datetime
import tempfile

class FileOperation(ABC):
    """An abstract base class for file operations."""

    @abstractmethod
    def execute(self, files: list[Path]):
        """
        Executes the file operation.

        Args:
            files: A list of Path objects to operate on.
        """
        pass

class Sorter(FileOperation):
    """Sorts files based on a specified key."""

    def __init__(self, sort_key: str = 'name', reverse: bool = False):
        self.sort_key = sort_key
        self.reverse = reverse

    def execute(self, files: list[Path]):
        print(f"Sorting files by {self.sort_key}...")
        if self.sort_key == 'name':
            files.sort(key=lambda f: f.name, reverse=self.reverse)
        elif self.sort_key == 'date':
            files.sort(key=lambda f: f.stat().st_mtime, reverse=self.reverse)
        elif self.sort_key == 'size':
            files.sort(key=lambda f: f.stat().st_size, reverse=self.reverse)
        elif self.sort_key == 'extension':
            files.sort(key=lambda f: f.suffix, reverse=self.reverse)
        
        print("Sorted files:")
        for file in files:
            print(f"- {file.name}")

class Renamer(FileOperation):
    """Renames files based on a pattern."""

    def __init__(self, pattern: str):
        self.pattern = pattern

    def execute(self, files: list[Path]):
        print(f"Renaming files with pattern: {self.pattern}...")
        for i, file in enumerate(files):
            try:
                new_name = self.pattern.format(index=i + 1, name=file.stem, ext=file.suffix)
                new_path = file.with_name(new_name)
                if new_path.exists():
                    print(f"Warning: {new_path} already exists. Skipping rename for {file.name}")
                    continue
                file.rename(new_path)
                print(f"Renamed {file.name} to {new_path.name}")
            except Exception as e:
                print(f"Error renaming {file.name}: {e}")

class Organizer(FileOperation):
    """Organizes files into subdirectories."""

    def __init__(self, strategy: str = 'extension'):
        self.strategy = strategy

    def execute(self, files: list[Path]):
        print(f"Organizing files by {self.strategy}...")
        if self.strategy == 'extension':
            for file in files:
                if file.is_dir():
                    continue
                ext = file.suffix[1:] if file.suffix else 'no_extension'
                dest_dir = file.parent / ext
                dest_dir.mkdir(exist_ok=True)
                shutil.move(str(file), str(dest_dir))
                print(f"Moved {file.name} to {dest_dir}")
        elif self.strategy == 'date':
            for file in files:
                if file.is_dir():
                    continue
                mod_time = file.stat().st_mtime
                date_str = datetime.fromtimestamp(mod_time).strftime('%Y-%m')
                dest_dir = file.parent / date_str
                dest_dir.mkdir(exist_ok=True)
                shutil.move(str(file), str(dest_dir))
                print(f"Moved {file.name} to {dest_dir}")

class Archiver(FileOperation):
    """Compresses files into a ZIP archive."""

    def __init__(self, output_name: str = 'archive'):
        self.output_name = output_name

    def execute(self, files: list[Path]):
        if not files:
            print("No files to archive.")
            return

        # Get the parent directory from the first file
        parent_dir = files[0].parent
        archive_path_base = parent_dir / self.output_name

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # Copy files to the temporary directory
            for file in files:
                if file.is_file():
                    shutil.copy(file, temp_path / file.name)
            
            # Create the archive from the temporary directory
            try:
                archive_path = shutil.make_archive(
                    base_name=str(archive_path_base),
                    format='zip',
                    root_dir=temp_path
                )
                print(f"Successfully created archive: {Path(archive_path).resolve()}")
            except Exception as e:
                print(f"Error creating archive: {e}")
