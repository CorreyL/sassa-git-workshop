from unittest import mock
from argparser import get_args


@mock.patch("argparse.ArgumentParser")
@mock.patch("argparse.ArgumentParser.add_argument")
def test_get_args(add_argument, ArgumentParser):
    ArgumentParser.return_value.add_argument = add_argument
    ArgumentParser.return_value.parse_args.return_value = []
    captured_return_value = get_args()
    ArgumentParser.assert_called_once_with(
        description="Historical Currency Converter"
    )
    add_argument.assert_has_calls(
        [
            mock.call(
                "-y",
                "--year",
                help=(
                    "The year in which you are interested in the currency "
                    "rate"
                ),
                type=int,
                default=None,
            ),
            mock.call(
                "-m",
                "--month",
                help=(
                    "The month in which you are interested in the currency "
                    "rate (1-12)"
                ),
                type=int,
                default=None,
            ),
            mock.call(
                "-c",
                "--currency",
                help="The three letter currency code (eg. AUD, BRL, JPY)",
                type=str,
                default=None,
            ),
        ]
    )
    assert (
        captured_return_value
        == ArgumentParser.return_value.parse_args.return_value
    )
