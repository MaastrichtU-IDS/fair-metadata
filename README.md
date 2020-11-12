[![Run tests](https://github.com/MaastrichtU-IDS/fair-metadata/workflows/Run%20tests/badge.svg)](https://github.com/MaastrichtU-IDS/fair-metadata/actions?query=workflow%3A%22Run+tests%22)

## FAIR Metadata generator

Python library and CLI to generate FAIR metadata for your dataset.

It runs [SPARQL queries](https://github.com/MaastrichtU-IDS/fair-metadata/tree/master/fair_metadata/queries) against the SPARQL endpoint provided by the user to produce [HCLS dataset statistics](https://www.w3.org/TR/hcls-dataset/) for the dataset.

Metadata are returned in the RDF Turtle format.

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
  * It uploads the test coverage to SonarCloud, you will need to set the `SONAR_TOKEN` secret
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
pytest tests/test_fair_metadata.py::test_create_dataset_metadata -s
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

