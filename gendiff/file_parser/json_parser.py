"""JSON file parser."""
from json import load as json_load

from .file_parser import FileParser


class JsonParser(FileParser):
    """Create JSON file parser."""

    def parse(self) -> dict:
        """Parse data from JSON file.

        Returns:
            File data
        """
        with open(self.file_path, "r") as file_data:
            self.file_data = json_load(file_data)
        return self.file_data
