import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Historical Currency Converter"
    )

    parser.add_argument(
        "-y",
        "--year",
        help="The year in which you are interested in the currency rate",
        type=int,
        default=None,
    )

    parser.add_argument(
        "-m",
        "--month",
        help="The month in which you are interested in the currency rate (1-12)",
        type=int,
        default=None,
    )

    return parser.parse_args()
