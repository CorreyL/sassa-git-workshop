max_tries = 3


def get_year_input(rates):
    tries = 0
    while tries < max_tries:
        print(
            "What year would you like to get your currency rate from?\n"
            f"Supported years include: {rates.get_supported_years()}"
        )
        year_input = input()
        try:
            rates.check_valid_year(int(year_input))
            return int(year_input)
        except Exception as err:
            tries = tries + 1
            print(f"{err}\n")
    raise Exception("Number of tries exceeded. Exitting program.")


def get_month_input(rates):
    tries = 0
    while tries < max_tries:
        print(
            f"What month would you like to get your currency rate from?\n"
            f"Supported months include: {list(range(1, 13))}"
        )
        month = input()
        try:
            rates.check_valid_month(int(month))
            return int(month)
        except Exception as err:
            tries = tries + 1
            print(f"{err}\n")
    raise Exception("Number of tries exceeded. Exitting program.")


def get_currency_input(rates):
    tries = 0
    currency = None
    while tries < max_tries:
        print(
            f"What currency do you want to convert to CAD?\n"
            f"Supported currencies include: {rates.get_supported_currencies()}"
        )
        currency = input()
        try:
            rates.check_valid_currency(currency)
            return currency
        except Exception as err:
            tries = tries + 1
            print(f"{err}\n")
    raise Exception("Number of tries exceeded. Exitting program.")
