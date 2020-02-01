from unittest import mock, TestCase


class Test_Rates_Init(TestCase):
    @mock.patch("rates.Rates.parse_csv")
    def test_init(self, parse_csv):
        """
        Only import within the scope of this test so that subsequent tests can
        remove the __init__ call, ensuring the __init__ lines and the functions
        invoked therein are properly unit tested
        """
        from rates import Rates

        self.rates = Rates()
        assert self.rates.currency_to_series_id == {}
        assert self.rates.series == {}
        assert self.rates.observations == {}
        parse_csv.assert_called_once()


class Test_Rates(TestCase):
    def setUp(self):
        """
        Ensures that `utils.pog_converter.PogConverter.__init__` is not executed
        when

        `from rates import Rates`

        Occurs, which would erroneously report that `rates.Rates.__init__` has
        been covered when just running pytest on `test_rates.py`
        """
        with mock.patch("rates.Rates.__init__") as RatesInit:
            RatesInit.return_value = None
            from rates import Rates

            self.rates = Rates()

    @mock.patch("csv.reader")
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    def test_parse_csv(self, mock_open, csv_reader):
        mock_csv_contents = [
            ["STUFF"],
            [],
            [],
            ["THAT"],
            [],
            ["SHOULD BE IGNORED"],
            [],
            [],
            ["SERIES"],
            ["id", "label", "description"],
            ["somefakeid", "AUD/CAD", "AUD to CAD"],
            ["anotherfakeid", "JPY/CAD", "JPY to CAD"],
            ["onemorefakeid", "EUR/CAD", "EUR to CAD"],
            [],
            ["OBSERVATIONS"],
            ["date", "somefakeid", "anotherfakeid", "onemorefakeid"],
            ["2017-01-01", 1.00, 0.50, 0.25],
            ["2018-01-01", 0.50, 0.25, 0.125],
            ["2019-01-01", 0.75, 0.33, 0.15],
            [],
        ]
        real_csv_filename = "FX_RATES_MONTHLY-sd-2017-01-01.csv"
        csv_reader.return_value = mock_csv_contents
        self.rates.currency_to_series_id = {}
        self.rates.series = {}
        self.rates.observations = {}
        self.rates.parse_csv()

        mock_open.assert_called_once_with(real_csv_filename)
        csv_reader.assert_called_once_with(mock_open.return_value)
        assert self.rates.series == {
            "somefakeid": {"label": "AUD/CAD", "description": "AUD to CAD"},
            "anotherfakeid": {"label": "JPY/CAD", "description": "JPY to CAD"},
            "onemorefakeid": {"label": "EUR/CAD", "description": "EUR to CAD",},
        }
        assert self.rates.currency_to_series_id == {
            "AUD": "somefakeid",
            "JPY": "anotherfakeid",
            "EUR": "onemorefakeid",
        }
        assert self.rates.observations == {
            2017: {1: {"somefakeid": 1.0, "anotherfakeid": 0.5}},
            2018: {1: {"somefakeid": 0.5, "anotherfakeid": 0.25}},
            2019: {1: {"somefakeid": 0.75, "anotherfakeid": 0.33}},
        }

    def test_get_supported_years(self):
        mock_supported_years = [2017, 2018, 2019]
        self.rates.observations = {}
        for year in mock_supported_years:
            self.rates.observations[year] = {}

        assert self.rates.get_supported_years() == mock_supported_years

    def test_get_supported_currencies(self):
        mock_supported_currencies = ["AUD", "EUR", "JPY"]
        self.rates.currency_to_series_id = {}
        for currency in mock_supported_currencies:
            self.rates.currency_to_series_id[currency] = {}

        assert (
            self.rates.get_supported_currencies() == mock_supported_currencies
        )

    @mock.patch("rates.Rates.get_supported_years")
    def test_check_valid_year_input_valid_year(self, get_supported_years):
        captured_error = None
        get_supported_years.return_value = [2017, 2018, 2019]
        try:
            self.rates.check_valid_year(get_supported_years.return_value[0])
        except Exception as err:
            captured_error = err
        get_supported_years.assert_called_once()
        assert captured_error == None

    @mock.patch("rates.Rates.get_supported_years")
    def test_check_valid_year_input_invalid_year(self, get_supported_years):
        get_supported_years.return_value = [2017, 2018, 2019]
        inputted_year = 2016
        captured_error = None
        try:
            self.rates.check_valid_year(inputted_year)
        except Exception as err:
            captured_error = err
        get_supported_years.assert_called_once()
        assert str(captured_error) == (
            f"Unsupported year: {inputted_year}\n"
            f"Supported years include: {get_supported_years.return_value}"
        )
