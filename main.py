from argparser import get_args
from inputs import get_year_input, get_month_input, get_currency_input
from rates import Rates

args = get_args()
rates = Rates()


def main():
    print("Welcome to the Historical Rate Calculator")
    year = args.year if args.year else get_year_input(rates)
    month = args.month if args.month else get_month_input(rates)
    currency = args.currency if args.currency else get_currency_input(rates)
    conversion_rate = rates.get_rate(year, month, currency)
    print(f"Conversion rate of {currency} to CAD: {conversion_rate}")


if __name__ == "__main__":
    main()
