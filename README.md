# prefect-pokemon

## Welcome!

Tasks for retrieving Pokemon information

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-pokemon` with `pip`:

```bash
pip install prefect-pokemon
```

### Write and run a flow

```python
from prefect import flow
from prefect_pokemon.tasks import (
    goodbye_prefect_pokemon,
    hello_prefect_pokemon,
)


@flow
def example_flow():
    hello_prefect_pokemon
    goodbye_prefect_pokemon

example_flow()
```

## Resources

If you encounter any bugs while using `prefect-pokemon`, feel free to open an issue in the [prefect-pokemon](https://github.com/desertaxle/prefect-pokemon) repository.

If you have any questions or issues while using `prefect-pokemon`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-pokemon` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/desertaxle/prefect-pokemon.git

cd prefect-pokemon/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
