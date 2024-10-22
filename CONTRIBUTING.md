# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue.

When contributing to this repository, please first discuss the change you wish to make via an [issue](https://github.com/MaastrichtU-IDS/fair-metadata/issues) if applicable.

If you are part of the [MaastrichtU-IDS organization on GitHub](https://github.com/MaastrichtU-IDS) you can directly create a branch in this repository. Otherwise you will need to first [fork this repository](https://github.com/MaastrichtU-IDS/fair-metadata/fork).

To contribute:

1. Clone the repository:

```bash
git clone https://github.com/MaastrichtU-IDS/fair-metadata.git
cd fair-metadata
```

2. Create a new branch from the `main` branch and add your changes to this branch.

```bash
git checkout -b my-branch
```

3. See how to run the application in development at https://github.com/MaastrichtU-IDS/fair-metadata

## Pull Request process

1. Ensure the test are passing before sending a pull request:
```
pip3 install pytest
pytest tests
```
2. Update the `README.md` with details of changes, this includes new environment variables, exposed ports, useful file locations and container parameters.
3. [Send a pull request](https://github.com/MaastrichtU-IDS/fair-metadata/compare) to the `main` branch, answer the questions in the pull request message.
4. Project contributors will review your change as soon as they can!

## Versioning process

The versioning scheme for new releases on GitHub used is [SemVer](http://semver.org/) (Semantic Versioning).

Change version in `setup.py` before new release.
