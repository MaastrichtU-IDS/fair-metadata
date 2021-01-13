[![Run tests](https://github.com/MaastrichtU-IDS/fair-metadata/workflows/Run%20tests/badge.svg)](https://github.com/MaastrichtU-IDS/fair-metadata/actions?query=workflow%3A%22Run+tests%22) [![Publish package](https://github.com/MaastrichtU-IDS/fair-metadata/workflows/Publish%20package/badge.svg)](https://github.com/MaastrichtU-IDS/fair-metadata/actions?query=workflow%3A%22Publish+package%22) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=MaastrichtU-IDS_fair-metadata&metric=coverage)](https://sonarcloud.io/dashboard?id=MaastrichtU-IDS_fair-metadata) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=MaastrichtU-IDS_fair-metadata&metric=alert_status)](https://sonarcloud.io/dashboard?id=MaastrichtU-IDS_fair-metadata)

## FAIR Metadata generator

This Python library can be used from the commandline, it automatically generates descriptive metadata about a RDF knowledge graph (classes, instances, relations between classes).

We run [SPARQL queries](https://github.com/MaastrichtU-IDS/fair-metadata/tree/master/fair_metadata/queries) against the SPARQL endpoint provided by the user to produce [HCLS dataset statistics](https://www.w3.org/TR/hcls-dataset/) for the dataset in the RDF Turtle format.

## Prerequisites

* Python 3.6 or higher, with [pip](https://pip.pypa.io/en/stable/)
* Docker (optional)

## Installation

> Provide instructions to install the package

Install directly from GitHub to try it:

```bash
pip3 install git+https://github.com/MaastrichtU-IDS/fair-metadata.git
```

Or install from source code for development. Using `-e` means that changes to the source code will be automatically update the package locally.

```bash
pip3 install -e .
```

## Usage

> Provide working examples on how to run the package

Check the commands available:

```bash
fair-metadata
fair-metadata analyze --help
```

### Analyze a SPARQL endpoint

Generate descriptive metadata, about types and relations, for a SPARQL endpoint

```bash
fair-metadata analyze https://graphdb.dumontierlab.com/repositories/test-vincent -o metadata.ttl
```

### Create dataset metadata description

Create complete metadata description for your dataset, you will be asked a few questions (such as homepage, license and reference for this dataset)

```bash
fair-metadata create -o dataset_metadata.ttl
```
### Run as a Python library

You can also import and use this library in Python:

```python
from fair_metadata.generate_metadata import generate_hcls_from_sparql

sparql_endpoint = 'https://graphdb.dumontierlab.com/repositories/test-vincent'
dataset_uri = 'https://w3id.org/d2s/distribution/default'

g = generate_hcls_from_sparql(sparql_endpoint, dataset_uri)
```

## Continuous Integration

This repository uses [GitHub Actions](/actions) to:

* Automatically run tests at each push to the `main` branch
  * It uploads the test coverage to SonarCloud (requires to set the `SONAR_TOKEN` secret)
* Publish the package to [PyPI](https://pypi.org) when a release is created (N.B.: the version of the package needs to be increased in [setup.py](/blob/main/setup.py#L6) before).

> You will need to provide your login credentials using [secrets in the repository settings](/settings/secrets) to publish to [PyPI](https://pypi.org): `PYPI_USERNAME` and `PYPI_PASSWORD`

## Test locally

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

