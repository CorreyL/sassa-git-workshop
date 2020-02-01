from unittest import mock
from inputs import get_year_input, get_month_input, get_currency_input


@mock.patch("builtins.input")
@mock.patch("builtins.print")
@mock.patch("rates.Rates.get_supported_years")
@mock.patch("rates.Rates.check_valid_year")
def test_get_year_input_valid_input(
    check_valid_year, get_supported_years, builtins_print, builtins_input,
):
    builtins_input.return_value = 2017
    rates = mock.MagicMock
    rates.get_supported_years = get_supported_years
    rates.check_valid_year = check_valid_year
    get_supported_years.return_value = [builtins_input.return_value]
    captured_return = get_year_input(rates)
    builtins_print.assert_called_once_with(
        "What year would you like to get your currency rate from?\n"
        f"Supported years include: {get_supported_years.return_value}"
    )
    check_valid_year.assert_called_once_with(builtins_input.return_value)
    assert captured_return == builtins_input.return_value


@mock.patch("builtins.input")
@mock.patch("builtins.print")
@mock.patch("rates.Rates.get_supported_years")
@mock.patch("rates.Rates.check_valid_year")
def test_get_year_input_invalid_input(
    check_valid_year, get_supported_years, builtins_print, builtins_input,
):
    builtins_input.return_value = 2016
    rates = mock.MagicMock
    rates.get_supported_years = get_supported_years
    rates.check_valid_year = check_valid_year
    error_message = "errmsg"
    check_valid_year.side_effect = Exception(error_message)
    get_supported_years.return_value = [2017]
    captured_error_message = None
    try:
        get_year_input(rates)
    except Exception as err:
        captured_error_message = err

    builtins_print.assert_has_calls(
        [
            mock.call(
                "What year would you like to get your currency rate from?\n"
                f"Supported years include: {get_supported_years.return_value}"
            ),
            mock.call(f"{error_message}\n"),
        ],
    )
    assert (
        str(captured_error_message)
        == "Number of tries exceeded. Exitting program."
    )
