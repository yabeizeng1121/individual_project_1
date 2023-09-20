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

## Results Preview

![fa3fdf4db75f7bbeed04df7edf7c7ff](https://github.com/yabeizeng1121/individual_project_1/assets/143656459/9f2be7eb-207c-40fb-b969-0ba41fb75eec)
![e236add49ed5c7f6bf6055e0dd7b4de](https://github.com/yabeizeng1121/individual_project_1/assets/143656459/67009f50-52ba-4a33-9b5a-c5f2d99469b9)
![f916a1b82419c7d2635d4aef5abc473](https://github.com/yabeizeng1121/individual_project_1/assets/143656459/87085dc6-87e7-4aed-90b9-b393276d6007)
![398489789ca503ed1e7202aa269d2a7](https://github.com/yabeizeng1121/individual_project_1/assets/143656459/c290a8b9-346d-40b5-b8fa-2d55886b8dfb)
![300f3d230e1ce6a584c70013bb155ad](https://github.com/yabeizeng1121/individual_project_1/assets/143656459/ce469437-c82d-4904-a671-afeb9a678e5e)
![538f5fbef792e6c2a6111de6ef25136](https://github.com/yabeizeng1121/individual_project_1/assets/143656459/d0963fd9-e701-4f3e-9547-943f5902c786)


