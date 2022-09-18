"""Generate Diff module run script."""
from gendiff.argparse_args import get_args
from gendiff.gendiff import generate_diff


def main():
    """Gendiff main function. Print gendiff app results."""
    args = get_args()
    diff_data = generate_diff(args.first_file, args.second_file, args.format)
    print(diff_data)


if __name__ == "__main__":
    main()
