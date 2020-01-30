import csv


class Rates:
    def __init__(self):
        """
        Reads the currency conversion rate spreadsheet and builds the data
        structures necessary to get the conversion rate of different currencies
        at different times
        """
        with open("FX_RATES_MONTHLY-sd-2017-01-01.csv") as csvfile:
            csv_contents = list(csv.reader(csvfile))
            line_idx = 0
            while line_idx < len(csv_contents):
                # Unimportant line, continue parsing the CSV
                line_idx = line_idx + 1
