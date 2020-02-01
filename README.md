# SASSA Git Workshop - Historical CAD Currency Conversion

This repository houses the codebase used for the SASSA Git Workshop hosted on
February 3rd 2020.

# Black

This codebase uses [`black`](https://black.readthedocs.io/en/stable/) as a
formatter to ensure code consistency.

Please ensure the following command is executed before commiting any code:

```sh
# -l 80 enforces a 80 character-per-line limit
black my_script.py -l 80
```

# Setting Up Your Virtual Environment

## Linux

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

# Running Tests

## Linux
```sh
py.test --cov=. --cov-report=term-missing tests/test_*.py
```

## Windows
```sh
py.test --cov=. --cov-report=term-missing tests\.
```
