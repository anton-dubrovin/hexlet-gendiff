"""Plain formatter module."""
from typing import Final

from gendiff.diff_dict import DiffDict

from .diff_formatter import DiffFormatter

DIFF_STATUS: Final = "status"
DIFF_VALUE: Final = "value"
COMPLEX_VALUE: Final = "[complex value]"


class PlainFormatter(DiffFormatter):
    """Create PlainFormatter definition."""

    def __init__(self, diff_data: DiffDict):
        """Create PlainFormatter.

        Args:
            diff_data: Diff data dict
        """
        super().__init__(diff_data, "plain")

    def format_diff_data(self) -> str:
        """Get plain formatted diff data.

        Returns:
            Formatted diff data.
        """
        formatted_data = self._get_formatter_data(self.diff_data)
        return (
            "\n".join(sorted(formatted_data))
            .replace("'True'", "true")
            .replace("'False'", "false")
            .replace("'None'", "null")
            .replace("'0'", "0")
            .replace(f"'{COMPLEX_VALUE}'", COMPLEX_VALUE)
        )

    def _get_formatter_data(
        self,
        diff_data: DiffDict,
        parent_key: str = "",
    ) -> list[str]:

        output = []

        for item_key, item_list in diff_data.items():
            if len(item_list) == 1:
                diff_status = item_list[0][DIFF_STATUS]
                diff_value = item_list[0][DIFF_VALUE]

                if diff_status == "+":
                    output.append(
                        f"Property '{parent_key}{item_key}' "
                        + "was added with value: "
                        + f"'{self._if_complex(diff_value)}'",
                    )

                if diff_status == "-":
                    output.append(
                        f"Property '{parent_key}{item_key}' was removed",
                    )

                if diff_status == " " and isinstance(diff_value, DiffDict):
                    output += self._get_formatter_data(
                        item_list[0][DIFF_VALUE],
                        f"{parent_key}{item_key}.",
                    )
            else:
                diff_old_value = item_list[0][DIFF_VALUE]
                diff_new_value = item_list[1][DIFF_VALUE]

                output.append(
                    f"Property '{parent_key}{item_key}' was updated. "
                    + f"From '{self._if_complex(diff_old_value)}' "
                    + f"to '{self._if_complex(diff_new_value)}'",
                )

        return output

    def _if_complex(self, maybe_complex_value):
        if isinstance(maybe_complex_value, dict):
            return COMPLEX_VALUE
        return maybe_complex_value
