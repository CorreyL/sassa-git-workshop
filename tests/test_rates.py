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
