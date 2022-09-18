"""JSON formatter module."""
from collections import OrderedDict
from json import dumps as json_dumps
from typing import Optional

from gendiff.diff_dict import DiffDict

from .diff_formatter import DiffFormatter


class JSONFormatter(DiffFormatter):
    """Create JSONFormatter definition."""

    def __init__(self, diff_data: DiffDict):
        """Create JSONFormatter.

        Args:
            diff_data: Diff data dict
        """
        super().__init__(diff_data, "json")

    def format_diff_data(
        self,
        diff_data: Optional[DiffDict] = None,
    ) -> str:
        """Get JSON formatted diff data.

        Args:
            diff_data: Diff data dict

        Returns:
            Formatted diff data.
        """
        return json_dumps(OrderedDict(sorted(self.diff_data.items())))
