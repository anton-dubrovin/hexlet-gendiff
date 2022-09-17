"""Interface for Diff formatter."""
from abc import ABC, abstractmethod
from typing import Optional

from gendiff.gendiff import DiffDict


class DiffFormatter(ABC):
    """Create interface for Diff formatter."""

    def __init__(self, diff_data: DiffDict, diff_format: str) -> None:
        """Create DiffFormatter.

        Args:
            diff_data: Diff data dict
            diff_format: Format - stylish, plane, json
        """
        self.diff_data = diff_data
        self.diff_format = diff_format
        self.formatted_diff_data = ""

    @abstractmethod
    def format_diff_data(self, diff_data: Optional[DiffDict]) -> str:
        """Get formatted diff data.

        Args:
            diff_data: Diff data dict

        Returns:
            Formatted diff data.
        """
        raise NotImplementedError
