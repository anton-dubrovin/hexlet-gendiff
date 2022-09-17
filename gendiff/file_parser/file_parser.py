"""Interface for FileParser."""
from abc import ABC, abstractmethod


class FileParser(ABC):
    """Create interface for FileParser."""

    def __init__(self, file_path: str) -> None:
        """Create FileParser.

        Args:
            file_path: Path to file
        """
        self.file_path = file_path
        self.file_data = {}

    @abstractmethod
    def parse(self) -> dict:
        """Parse data from file.

        Returns:
            File data.
        """
        raise NotImplementedError
