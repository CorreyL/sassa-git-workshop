import csv


class Rates:
    def __init__(self):
        self.currency_to_series_id = {}
        self.series = {}
        self.observations = {}
        self.parse_csv()

    def parse_csv(self):
        """
        Reads the currency conversion rate spreadsheet and builds the data
        structures necessary to get the conversion rate of different currencies
        at different times
        """
        with open("FX_RATES_MONTHLY-sd-2017-01-01.csv") as csvfile:
            csv_contents = list(csv.reader(csvfile))
            line_idx = 0
            while line_idx < len(csv_contents):
                line = csv_contents[line_idx]
                # Parse the contents under the SERIES header
                if len(line) > 0 and line[0] == "SERIES":
                    # Start at the first row of the SERIES data
                    line_idx = line_idx + 2
                    line = csv_contents[line_idx]
                    while len(line) > 0:
                        id = line[0]
                        label = line[1]
                        description = line[2]
                        self.series[id] = {
                            "label": label,
                            "description": description,
                        }
                        currency = label.split("/")[0]
                        self.currency_to_series_id[currency] = id
                        line_idx = line_idx + 1
                        line = csv_contents[line_idx]
                    # Once we are done parsing the SERIES data, continue parsing
                    # the rest of the CSV
                    continue
                if len(line) > 0 and line[0] == "OBSERVATIONS":
                    # Store the list of column headers, allowing the logic to
                    # use the index of a row to map back to the column the index
                    # corresponds to
                    column_headers = csv_contents[line_idx + 1]
                    # Start at the first row of the OBSERVATIONS data
                    line_idx = line_idx + 2
                    line = csv_contents[line_idx]
                    while len(line) > 0:
                        date = line[0].split("-")
                        year = int(date[0])
                        month = int(date[1])
                        self.observations.setdefault(year, {})[month] = {}
                        for column_idx in range(1, len(line) - 1):
                            id = column_headers[column_idx]
                            self.observations[year][month][id] = line[
                                column_idx
                            ]
                        line_idx = line_idx + 1
                        line = csv_contents[line_idx]
                    # Once we are done parsing the OBSERVATION data, continue
                    # parsing the rest of the CSV
                    continue
                # Unimportant line, continue parsing the CSV
                line_idx = line_idx + 1

    def get_supported_currencies(self):
        """
        Returns a list of supported currencies, identified by their
        internationally recognized three letter code (i.e. 'USD', 'AUD', 'SGD')

        Returns:
        list[string]: A list of strings that correspond to a list of supported
        currencies
        """
        return list(self.currency_to_series_id.keys())

    def check_valid_year(self, year):
        """
        Checks if a given year is supported in this instance of the class

        Raises:
        Exception: If the inputted year is not supported
        """
        if year not in self.observations:
            raise Exception(
                f"Unsupported year: {year}\n"
                f"Supported years include: {list(self.observations.keys())}"

    def check_valid_month(self, month):
        """
        Checks if a given month is supported in this instance of the class

        Raises:
        Exception: If the inputted month is not supported
        """
        if month < 1 or month > 12:
            raise Exception(
                f"Invalid month: {month}\n"
                f"Month must be a value between 1-12",
            )

    def check_valid_currency(self, currency):
        """
        Checks if a given currency is supported in this instance of the class

        Raises:
        Exception: If the inputted currency is not supported
        """
        if currency not in self.get_supported_currencies():
            raise Exception(
                f"Unsupported currency: {currency}\n"
                f"Supported currencies include: "
                f"{list(self.currency_to_series_id.keys())}"
            )

    def get_rate(self, year, month, currency):
        """
        Returns the conversion rate to CAD for a given year, month and currency

        Parameters:
        year (int): The year of the desired currency rate
        month (int): The month of the desired currency rate
        currency (string): The desired currency to convert to CAD (supported
          currencies will be stored in `self.currency_to_series_id`)

        Returns:
        float: The currency exchange rate based on the given year, month and
        currency
        """
        self.check_valid_year(year)
        self.check_valid_month(month)
        self.check_valid_currency(currency)

        series_id = self.currency_to_series_id[currency]
        return self.observations[year][month][series_id]
