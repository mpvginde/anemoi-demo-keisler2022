# Learn Anemoi with Keisler (2022)

A lightweight demo introducing the [Anemoi Framework](https://github.com/ecmwf/anemoi)
and inspired by [Keisler (2022)](https://arxiv.org/abs/2202.07575), the seminal work
that applied Graph Neural Networks (GNNs) to global weather forecasting.

## Objective

This repository provides a hands-on demonstration of how to use the Anemoi framework to
reproduce and extend key ideas from Keisler (2022): Forecasting Global Weather with Graph
Neural Networks.

It is designed to help users:

* Learn how to structure, configure, and run ML experiments with Anemoi.
* Explore data ingestion, model training, and evaluation pipelines in a reproducible way.
* Serve as an onboarding and educational tool for new users within the Anemoi ecosystem.

Note: this is not an exact reproduction of Keisler’s model. Instead, it’s a simplified demo
illustrating the principles, workflow, and integration possibilities offered by Anemoi.

## Getting started

Clone the repository with:

```bash
git clone https://github.com/mpvginde/anemoi-demo-keisler2022.git
cd anemoi-demo-keisler2022
```

### Install and set up the environment with `uv`

This project uses [uv](https://docs.astral.sh/uv/) to manage environments and dependencies.
Make sure you have `uv` installed (see [installation instructions](https://docs.astral.sh/uv/getting-started/)).

Create and activate the virtual environment:

```bash
uv venv
source .venv/bin/activate
```

Install all dependencies defined in `pyproject.toml`:

```bash
uv sync
```

The `uv sync` command will also install `ipykernel`, allowing you to run the notebooks
directly from VS Code.

If you prefer to use the classic Jupyter interface, you can install it manually with:

```bash
uv pip install jupyter
```

### Option 1 — Using VS Code (recommended)

VS Code provides an integrated experience for running and editing notebooks.
You can follow the official [VS Code Jupyter documentation](https://code.visualstudio.com/docs/datascience/jupyter-notebooks), but in short:

1. Open the cloned folder in VS Code.
2. Make sure the Python and Jupyter extensions are installed.
3. When prompted, select your virtual environment (under `.venv`) as the kernel.
4. Open notebooks sequentially, starting with `notebooks/01_create_dataset.ipynb`.

### Option 2 — Using Jupyter Notebook (browser interface)

If you prefer the classic Jupyter interface, run:

```bash
jupyter notebook
```

Then open the notebooks sequentially, starting with `notebooks/01_create_dataset.ipynb`.
