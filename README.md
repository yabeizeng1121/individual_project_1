[![CI](https://github.com/yabeizeng1121/individual_project_1/actions/workflows/cicd.yml/badge.svg)](https://github.com/yabeizeng1121/individual_project_1/actions/workflows/cicd.yml)
# IDS706 Individual Project 1 

This project provides a comprehensive data analysis for a car dataset, including a Jupyter notebook, a Python script, shared library functions, and automated testing and linting via Makefile and GitHub Actions.

## Project Structure

- **Jupyter Notebook**: A detailed notebook that demonstrates the data analysis process.
- **Python Script**: A standalone script for data analysis.
- **lib.py**: A shared library that contains common functions used by both the notebook and the script.
- **Makefile**: Automates the testing, linting, and formatting processes.
- **Requirements.txt**: Lists all the necessary Python packages for this project.

## Usage

### Jupyter Notebook

The notebook provides a visual interface for data analysis. Ensure you have Jupyter installed and run:

```bash
jupyter notebook your_notebook_name.ipynb
```

### Python Script

To execute the standalone script:

```bash
python your_script_name.py
```

### lib.py

This shared library contains essential functions for data analysis. It's used by both the notebook and the script.

### Makefile

The Makefile automates several tasks:

1. **Running Tests**: This will run tests for the notebook, script, and lib.

```bash
make test
```

2. **Formatting Code**: This will format the code using Python black.

```bash
make format
```

3. **Linting Code**: This will lint the code using Ruff.

```bash
make lint
```

### Testing

- **nbval plugin for pytest**: The Jupyter notebook is tested using the nbval plugin for pytest.
- **test_script.py**: Contains tests for the Python script.
- **test_lib.py**: Contains tests for the shared library.

To install the required packages:

```bash
pip install -r requirements.txt
```

## GitHub Actions

Our repository uses GitHub Actions to automate the execution of all Makefile commands. Check the badges in this README for the status of each action.

## Demo Video

For a detailed walkthrough of the project and its functionality, please watch our [demo video](YOUR_YOUTUBE_LINK_HERE).

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

[MIT License](https://opensource.org/licenses/MIT)

---

Make sure to replace placeholders like `your_notebook_name.ipynb` and `YOUR_YOUTUBE_LINK_HERE` with the actual names and links. Adjust other parts of the README as necessary to fit your project's specifics.
