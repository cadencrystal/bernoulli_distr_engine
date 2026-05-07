# Bernoulli Distribution Engine

A simple command-line Python program for working with Bernoulli sample data.

The script `bernoulli_distr_engine.py` lets a user enter observed successes and sample size, choose a confidence level, and compute sample statistics such as:
- sample proportion (`p-hat`)
- failure proportion (`q-hat`)
- standard error
- confidence interval

## Requirements

- Python 3.13 or later
- `matplotlib` (if the script uses plotting features)

## Recommended setup

From the `Bernoulli_distr_engine` folder:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install matplotlib
```

## Usage

Run the script from the project folder:

```bash
python bernoulli_distr_engine.py
```

Then follow the prompts to enter:
1. Number of observed successes (`x`)
2. Sample size (`n`)
3. Confidence level choice (`1`, `2`, or `3`)

The program will print the sample summary and calculated confidence interval.

## Notes

- `x` should be an integer between `0` and `n`.
- `n` should be a positive integer.
- If `matplotlib` is required and not installed, add it with:

```bash
python -m pip install matplotlib
```