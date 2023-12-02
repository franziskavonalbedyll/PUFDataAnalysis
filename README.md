# PUF Data Analysis
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![puf.png](puf.png)

This repository contains a Python tool for analyzing Physical Unclonable Functions (PUFs). PUFs are a type of security technology that uses the inherent physical variations in hardware to produce unique identifiers and cryptographic keys. This tool provides a small suite for assessing various properties of PUFs, including uniqueness, uniformity, reliability, and bit-aliasing.

## Usage

1. Install all necessary dependencies using poetry:
   ```bash
    poetry install
   ```
2. Place your raw PUF data in the DATA_DIRECTORY.
3. Run:
    ```bash
    poetry run python main.py
    ```
    The tool will convert your data to binary format and store it in BIN_DATA_DIRECTORY.
    The tool then processes the binary data to compute bit aliasing, reliability, uniqueness, and uniformity values.
4. The results for the metrics reliability, uniformity, uniqueness and bit-aliasing will be printed to the console.


## Development Tools
### Pre-commit

Pre-commit is used in this project to ensure that git commits adhere to a consistent style and prevent committing problematic code. The hooks configured in `.pre-commit-config.yaml` will automatically check and fix issues (where possible) in the staged files when you run `git commit`.
Using this project's pyproject.toml, poetry already installs pre-commit for you, so no need to take care of it manually!
If you want to run pre-commit manually, enter the poetry shell and use:


```
pre-commit run
```

### Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. If you would like to add a package, simply run:
```bash
poetry add <name-of-dependency>
```
To run a script using poetry's venv:
```bash
poetry run python main.py
```
