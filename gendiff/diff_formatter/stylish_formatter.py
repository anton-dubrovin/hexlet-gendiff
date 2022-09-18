"""Stylish formatter module."""
from typing import Final, Optional

from gendiff.diff_dict import DiffDict

from .diff_formatter import DiffFormatter

DIFF_STATUS: Final = "status"
DIFF_VALUE: Final = "value"

INDENT: Final = "  "
OFFSET: Final = 2


class StylishFormatter(DiffFormatter):
    """Create StylishFormatter definition."""

    def __init__(self, diff_data: DiffDict):
        """Create StylishFormatter.

        Args:
            diff_data: Diff data dict
        """
        super().__init__(diff_data, "stylish")
        self.line_format = "$indent$status $node_key: $node_value"

    def format_diff_data(
        self,
        diff_data: Optional[DiffDict] = None,
        deep: int = 0,
    ) -> str:
        """Get stylish formatted diff data.

        Args:
            diff_data: Diff data dict
            deep: Dict data deep for iteration

        Returns:
            Formatted diff data.
        """
        diff_data = self.diff_data if diff_data is None else diff_data

        output = ["{"]

        for item_key, item_list in sorted(diff_data.items()):
            for item_data in item_list:
                if isinstance(item_data[DIFF_VALUE], DiffDict):
                    output.append(
                        self._get_line(
                            item_data[DIFF_STATUS],
                            item_key,
                            self.format_diff_data(
                                item_data[DIFF_VALUE],
                                deep + OFFSET,
                            ),
                            deep,
                        ),
                    )
                elif isinstance(item_data[DIFF_VALUE], dict):
                    output.append(
                        self._get_line(
                            item_data[DIFF_STATUS],
                            item_key,
                            self._format_dict_value(
                                item_data[DIFF_VALUE],
                                deep + OFFSET,
                            ),
                            deep,
                        ),
                    )
                else:
                    output.append(
                        self._get_line(
                            item_data[DIFF_STATUS],
                            item_key,
                            str(item_data[DIFF_VALUE]),
                            deep,
                        ),
                    )

        output.append(f"{INDENT * deep}}}")

        if deep == 0:
            return (
                "\n".join(output)
                .replace("True", "true")
                .replace("False", "false")
                .replace("None", "null")
            )

        return "\n".join(output)

    def _format_dict_value(self, dict_value: dict, deep: int = 0) -> str:
        output = ["{"]

        for item_key, item_value in sorted(dict_value.items()):
            if isinstance(item_value, dict):
                output.append(
                    self._get_line(
                        " ",
                        item_key,
                        self._format_dict_value(
                            item_value,
                            deep + OFFSET,
                        ),
                        deep,
                    ),
                )
            else:
                output.append(
                    self._get_line(" ", item_key, str(item_value), deep),
                )

        output.append(INDENT * deep + "}")
        return "\n".join(output)

    def _get_line(self, status, node_key, node_value, deep):

        return (
            self.line_format.replace("$indent", INDENT * (deep + 1))
            .replace("$status", status)
            .replace("$node_key", node_key)
            .replace("$node_value", node_value)
        )
