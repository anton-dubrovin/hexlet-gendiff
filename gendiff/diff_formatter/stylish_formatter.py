from collections import OrderedDict
from typing import Final, Optional

from gendiff.diff_dict import DiffDict

from .diff_formatter import DiffFormatter

INDENT: Final = "  "
OFFSET: Final = 2


class StylishFormatter(DiffFormatter):
    formatted_diff_data: str = ""

    def __init__(self, diff_data: DiffDict):
        super().__init__(diff_data, "stylish")

    @staticmethod
    def __get_line(status, key, value, deep):
        return f"{INDENT * (deep + 1)}{status} {key}: {value}"

    def format_diff_data(
        self,
        diff_data: Optional[DiffDict] = None,
        deep: int = 0,
    ) -> str:
        diff_data = self.diff_data if diff_data is None else diff_data

        output = ["{"]

        for diff_item_key, diff_item_list in OrderedDict(
            sorted(diff_data.items())
        ).items():
            for diff_item_data in diff_item_list:
                if isinstance(diff_item_data["value"], DiffDict):
                    output.append(
                        self.__get_line(
                            diff_item_data["status"],
                            diff_item_key,
                            self.format_diff_data(
                                diff_item_data["value"],
                                deep + OFFSET,
                            ),
                            deep,
                        ),
                    )
                elif isinstance(diff_item_data["value"], dict):
                    output.append(
                        self.__get_line(
                            diff_item_data["status"],
                            diff_item_key,
                            self.__format_dict_value(
                                diff_item_data["value"],
                                deep + OFFSET,
                            ),
                            deep,
                        ),
                    )
                else:
                    output.append(
                        self.__get_line(
                            diff_item_data["status"],
                            diff_item_key,
                            diff_item_data["value"],
                            deep,
                        ),
                    )

        output.append(INDENT * deep + "}")

        if deep == 0:
            return (
                "\n".join(output)
                .replace("True", "true")
                .replace("False", "false")
                .replace("None", "null")
            )

        return "\n".join(output)

    def __format_dict_value(self, dict_value: dict, deep: int = 0) -> str:
        output = ["{"]
        for item_key, item_value in OrderedDict(
            sorted(dict_value.items())
        ).items():
            if isinstance(item_value, dict):
                output.append(
                    self.__get_line(
                        " ",
                        item_key,
                        self.__format_dict_value(
                            item_value,
                            deep + OFFSET,
                        ),
                        deep,
                    ),
                )
            else:
                output.append(
                    self.__get_line(
                        " ",
                        item_key,
                        str(item_value),
                        deep,
                    ),
                )

        output.append(INDENT * deep + "}")
        return "\n".join(output)
