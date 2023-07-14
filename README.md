# STATISTICS_small_sample_python_code
by using this program we can calculate single mean of small sample data and it'll tell weather it reject or accept hypothesis
# Hypothesis Test using Z-Test Statistic

## Description
This Python script performs a hypothesis test using the z-test statistic. It calculates the z-value and compares it to a critical value (TABLE) to determine whether to accept or reject the null hypothesis.

## Dependencies
- Python 3.x
- scipy.stats
- math
- statistics

## Usage
1. Run the script in a Python environment.
2. When prompted, enter the following input values:
   - `n1`: Sample size for dataset 1.
   - `n2`: Sample size for dataset 2.
   - `TABLE`: Critical value for the test.
   - `x`: Space-separated values for dataset 1 (e.g., "1 2 3").
   - `y`: Space-separated values for dataset 2 (e.g., "4 5 6").
   - `s1`: Standard deviation for dataset 1.
   - `s2`: Standard deviation for dataset 2.

## Output
The script calculates the z-value based on the provided inputs and compares it to the critical value (TABLE). It then outputs whether to accept or reject the null hypothesis.

Note: This script assumes that the provided input is in the correct format and does not perform extensive error handling.

## Example
```python
n1 = 30
n2 = 40
TABLE = 1.96
x = "1 2 3 4 5"
y = "6 7 8 9 10"
s1 = 2.5
s2 = 3.0
