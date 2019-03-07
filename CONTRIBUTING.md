# Contributing

Thanks for contributing ! Here is some guidelines to make your life easier during the development process.

## Installation

This project uses `pipenv` as a package manager.

For development purposes, you can install the package in editable mode with the development requirements.

```
make install-dev
```

## Syntax checking

You can check the syntax using flake8 :

```
make lint
```

## Type checking

If you used annotations to do static type checking with mypy :

```
make type
```

## Test coverage

You can run the coverage with the following command :

```
make test
```

## Documentation

The documentation of the project can be found under the directory `./docs/_build/html`.

To rebuild the configuration, you can use the following command :

```
make doc
```

## Version bumping

To update the version of the project, just run the following command according to the nature of the change.

```
bumpversion [ major | minor | patch ]
```
