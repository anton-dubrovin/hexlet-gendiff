"""YAML file parser."""
from yaml import safe_load as yaml_load

from .file_parser import FileParser


class YamlParser(FileParser):
    """Create YAML file parser."""

    def parse(self) -> dict:
        """Parse data from YAML file.

        Returns:
            File data
        """
        with open(self.file_path, "r") as file_data:
            self.file_data = yaml_load(file_data)
        return self.file_data
