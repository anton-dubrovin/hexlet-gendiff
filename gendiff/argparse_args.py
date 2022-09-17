"""Args parse for gendiff package."""
import argparse


def get_args():
    """Create args for gendiff package.

    Returns:
        Args for gendiff package.
    """
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument(
        "-f",
        "--format",
        default="stylish",
        help="set format of output",
    )
    parser.add_argument("first_file", metavar="first_file", type=str)
    parser.add_argument("second_file", metavar="second_file", type=str)
    return parser.parse_args()
