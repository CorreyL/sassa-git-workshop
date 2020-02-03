# SASSA Git Workshop - Historical CAD Currency Conversion

This repository houses the codebase used for the SASSA Git Workshop hosted on
February 3rd 2020.

---

### Table of Contents

* [Requirements](#Requirements)
* [Black](#Black)
* [Setting Up Your Virtual Environment](#Setting-Up-Your-Virtual-Environment)
* [Usage](#Usage)
* [Running Tests](#Running-Tests)

# Requirements

This codebase requires either `Python 3.7.x` or `Python 3.8.x`

Other versions of Python 3 may work, but I can only guarantee compatibility with `Python 3.7.x` and `Python 3.8.x`.

# Black

This codebase uses [`black`](https://black.readthedocs.io/en/stable/) as a
formatter to ensure code consistency.

Please ensure the following command is executed before commiting any code:

```sh
# -l 80 enforces a 80 character-per-line limit
black my_script.py -l 80
```

# Setting Up Your Virtual Environment

## Linux/Mac

```sh
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Windows

```sh
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

# Usage

To run the program:

```sh
# Provide one or more arguments via the command line
python main.py -y 2017 -m 1 -c AUD
# Or follow the program's prompts
python main.py
```

The `-h`/`--help` output is also available:

```sh
$ python main.py -h
usage: main.py [-h] [-y YEAR] [-m MONTH] [-c CURRENCY]

Historical Currency Converter

optional arguments:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR  The year in which you are interested in the currency
                        rate
  -m MONTH, --month MONTH
                        The month in which you are interested in the currency
                        rate (1-12)
  -c CURRENCY, --currency CURRENCY
```

# Running Tests

## Linux/Mac
```sh
py.test --cov=. --cov-report=term-missing tests/test_*.py
```

## Windows
```sh
py.test --cov=. --cov-report=term-missing tests\.
```
