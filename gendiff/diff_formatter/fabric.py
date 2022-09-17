"""Fabric for diff formatter module."""
from gendiff.diff_dict import DiffDict

from .stylish_formatter import StylishFormatter


def get_formatted_diff(diff_data: DiffDict, diff_format: str) -> str:
    """Get formatted diff data.

    Args:
        diff_data: Diff data dict
        diff_format: Format - stylish, plane, json

    Returns:
        Formatted diff data.
    """
    if diff_format == "stylish":
        return StylishFormatter(diff_data).format_diff_data()
