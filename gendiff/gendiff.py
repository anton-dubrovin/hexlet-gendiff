"""Generate diff module."""
from typing import Final

from gendiff.diff_dict import DiffDict
from gendiff.diff_formatter.fabric import get_formatted_diff
from gendiff.file_parser.fabric import parse_file_data

DIFF_STATUS: Final = "status"
DIFF_VALUE: Final = "value"


def find_diff(first_data: dict, second_data: dict) -> DiffDict:
    """Find differences and return dict with differences.

    Args:
        first_data: Dict of first data
        second_data: Dict of second data

    Returns:
        Dict with data differences
    """
    diff_data = DiffDict()

    for first_key, first_value in first_data.items():
        diff_data[first_key] = [{DIFF_STATUS: "-", DIFF_VALUE: first_value}]

    for second_key, second_value in second_data.items():
        merge_data = diff_data.get(second_key, None)

        if merge_data is None:
            diff_data[second_key] = [
                {
                    DIFF_STATUS: "+",
                    DIFF_VALUE: second_value,
                },
            ]

        elif second_value == merge_data[0][DIFF_VALUE]:
            diff_data[second_key][0][DIFF_STATUS] = " "

        elif isinstance(second_value, dict) and isinstance(
            merge_data[0][DIFF_VALUE],
            dict,
        ):
            diff_data[second_key][0] = {
                DIFF_STATUS: " ",
                DIFF_VALUE: find_diff(merge_data[0][DIFF_VALUE], second_value),
            }

        else:
            diff_data[second_key].append(
                {
                    DIFF_STATUS: "+",
                    DIFF_VALUE: second_value,
                },
            )

    return diff_data


def generate_diff(first_file: str, second_file: str, diff_format: str) -> None:
    """Find differences and print them in following format.

    Args:
        first_file: Path to first file
        second_file: Path to second file
        diff_format: Format - plain, stylish or json
    """
    print(
        get_formatted_diff(
            find_diff(
                parse_file_data(first_file),
                parse_file_data(second_file),
            ),
            diff_format,
        ),
    )
