import argparse
import json
from collections import OrderedDict


def generate_diff(first_file, second_file):
    print(f"{first_file} and {second_file} diff here...")
    first_file_data = json.load(open(first_file))
    second_file_data = json.load(open(second_file))
    diff_data = {}
    for line_key, line_value in first_file_data.items():
        diff_data[line_key] = [dict(value=line_value, status="-")]
    for line_key, line_value in second_file_data.items():
        diff_line_data = diff_data.get(line_key, None)
        if diff_line_data is None:
            diff_data[line_key] = [dict(value=line_value, status="+")]
        elif line_value == diff_line_data[0]["value"]:
            diff_data[line_key][0]["status"] = " "
        else:
            diff_data[line_key].append(dict(value=line_value, status="+"))

    print("{")
    for diff_item_key, diff_item_list in OrderedDict(sorted(diff_data.items())).items():
        for diff_item_data in diff_item_list:
            print(
                f"  {diff_item_data['status']} {diff_item_key}: {str(diff_item_data['value']).lower()}"
            )
    print("}")


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument(
        "-f",
        "--format",
        default="plain",
        help="set format of output",
    )
    parser.add_argument("first_file", metavar="first_file", type=str)
    parser.add_argument("second_file", metavar="second_file", type=str)
    args = parser.parse_args()

    generate_diff(args.first_file, args.second_file)


if __name__ == "__main__":
    main()
