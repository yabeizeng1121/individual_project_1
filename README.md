
## IDS706 Individual Project 1

This library provides a set of functions to load, summarize, and visualize data from a car dataset. The main functions include loading the data from a CSV file, generating a summary of the data, and creating a boxplot visualization based on the car's origin and weight.

## Requirements

- Python 3.x
- pandas
- seaborn
- matplotlib

## Installation

1. Ensure you have Python 3.x installed.
2. Install the required packages using pip:

```bash
pip install pandas seaborn matplotlib
```

## Usage

### lib.py

This script contains the main functions for data analysis. Here's a brief overview:

- `load_data(data_path)`: Loads data from a CSV file. The data should be separated by semicolons (`;`).
- `data_summary(data)`: Returns a summary (using `describe()`) of the provided data.
- `data_visual(data)`: Displays a boxplot visualization of the data based on the car's origin and weight.
- `main()`: A demonstration function that loads data from "cars.csv", prints its summary, and displays the boxplot visualization.

To run the script:

```bash
python lib.py
```

### Test File

Ensure you have your test file in the same directory as `lib.py`. To run the tests:

```bash
python test_filename.py
```

Replace `test_filename.py` with the actual name of your test file.

### Jupyter Notebook

If you're using a Jupyter notebook to visualize and test the functions:

1. Import the necessary functions from `lib.py`:

```python
from lib import load_data, data_summary, data_visual
```

2. Use the functions as demonstrated in the `main()` function of `lib.py`.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

[MIT License](https://opensource.org/licenses/MIT)

---

Note: You might need to adjust some parts of the README, such as the test file name, or add more details if necessary.
