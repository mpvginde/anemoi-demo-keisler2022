# Learn Anemoi with Keisler (2022)

A lightweight demo introducing the [Anemoi Framework](https://github.com/ecmwf/anemoi) 
and inspired by [Keisler (2022)](https://arxiv.org/abs/2202.07575), the seminal work 
that applied Graph Neural Networks (GNNs) to global weather forecasting.

## Objective

This repository provides a hands-on demonstration of how to use the Anemoi framework to
reproduce and extend key ideas from Keisler (2022): Forecasting Global Weather with Graph
Neural Networks.

It is designed to help users:
- Learn how to structure, configure, and run ML experiments with Anemoi.
- Explore data ingestion, model training, and evaluation pipelines in a reproducible way.
- Serve as an onboarding and educational tool for new users within the Anemoi ecosystem.

Note: this is not an exact reproduction of Keisler’s model. Instead, it’s a simplified demo
illustrating the principles, workflow, and integration possibilities offered by Anemoi.

## Getting started

Clone the repository with:

```bash
git clone https://github.com/mpvginde/anemoi-demo-keisler2022.git
cd anemoi-demo-keisler2022
```

Create and activate a virtual environment using a recent version of Python:

```bash
python -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Note the `requirements.txt` includes `ipykernel`, which allows you to run notebooks
from VS Code. If you prefer to use the classic Jupyter interface, myou can install it
manually with:

```bash
pip install jupyter
```

### Option 1 — Using VS Code (recommended)

VS Code provides an integrated experience for running and editing notebooks.
You can follow the official [VS Code Jupyter documentation](https://code.visualstudio.com/docs/datascience/jupyter-notebooks), but in short:

1, Open the cloned folder in VS Code.
2. Make sure the Python and Jupyter extensions are installed.
3. When prompted, select your virtual environment (venv) as the kernel.
4. Open notebooks sequentially, starting with `01_create_dataset.ipynb`.

### Option 2 — Using Jupyter Notebook (browser interface)
  
If you prefer the classic Jupyter interface, run:

```bash
jupyter notebook
```

Then open notebooks sequentially, starting with `01_create_dataset.ipynb`.