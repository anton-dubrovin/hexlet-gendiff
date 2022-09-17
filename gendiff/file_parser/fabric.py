"""Fabric for file parser module."""
from .json_parser import JsonParser
from .yaml_parser import YamlParser


def parse_file_data(file_path: str) -> dict:
    """Parse file data into dict.

    Args:
        file_path: Path to file

    Returns:
        File data
    """
    if file_path.lower().endswith(".json"):
        return JsonParser(file_path).parse()
    if file_path.lower().endswith((".yml", ".yaml")):
        return YamlParser(file_path).parse()
    return {}
