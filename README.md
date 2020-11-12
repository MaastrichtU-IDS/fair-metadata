[![Run tests](https://github.com/MaastrichtU-IDS/python-template/workflows/Run%20tests/badge.svg)](https://github.com/MaastrichtU-IDS/python-template/actions?query=workflow%3A%22Run+tests%22)

## How to use this template

* For the directory name, *Dockerfile*, *setup.py* and *test_application.py*, Replace all instances of **my_package** and **fair-metadata** to the package name of your choice using [snake case](https://en.wikipedia.org/wiki/Snake_case) or dash depending on the convention.
* Leave the headers as is and update the instructions below to the specifics of your tool.
* Remove this *How to use this template section*

## My package

Write a short description of the software here.

## Prerequisites

* Python 3.6 or higher, with [pip](https://pip.pypa.io/en/stable/)
* Docker (optional)

## Installation

> Provide instructions to install the package

The package can be installed from the source code, see below to run with Docker. Using `-e` means that changes to the source code will be automatically update the package locally.

```bash
pip3 install -e .
```

## Usage

> Provide working examples on how to run the package

Run the `fair-metadata` CLI in your terminal:

```bash
fair-metadata create -o dataset_metadata.ttl
```
Or in a Python script:

```python
from fair_metadata.generate_metadata import create_dataset

create_dataset(metadata_object)
```

## Test and Publish

> Document how to run the tests, and if they are run automatically.

### Continuous Integration

This repository uses [GitHub Actions](/actions) to:

* Automatically run tests at each push to the `main` branch
* Publish the package to [PyPI](https://pypi.org) when a release is created (N.B.: the version of the package needs to be increased in [setup.py](/blob/main/setup.py#L6) before).

> You will need to provide your login credentials using [secrets in the repository settings](/settings/secrets) to publish to [PyPI](https://pypi.org): `PYPI_USERNAME` and `PYPI_PASSWORD`

### Test locally

Install PyTest:

```bash
pip3 install -U pytest
```

Run the tests:

```bash
pytest
```

Run a specific test in a file, and display `print` in the output:

```bash
pytest tests/test_application.py::TestApplication::test_return_value -s
```

## Docker

Build the image:

```bash
docker build -t fair-metadata .
```

Run a container:

```bash
docker run -it --rm -v $(pwd):/root fair-metadata create -o dataset_metadata.ttl
```

