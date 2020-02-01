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
