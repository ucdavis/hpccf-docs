# HPC@UCD Docs

[![pages-build-deployment](https://github.com/ucdavis/hpccf-docs/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/ucdavis/hpccf-docs/actions/workflows/pages/pages-build-deployment)

To get started with local development, first stop, and read our [style guide](docs.hpc.ucdavis.edu/meta/style). 
Then, clone the docs and spack-ucdavis repos:

    git clone git@github.com:ucdavis/hpccf-docs.git
    git clone git@github.com:ucdavis/spack-ucdavis.git

    cd hpccf-docs
    ln -s ../spack-ucdavis .

Then create a virtual environment, either with `virtualenv`:

    python -m venv venv
    . venv/bin/activate

Or with `conda`:

    conda create -n mkdocs
    conda activate mkdocs

Then install the dependencies:

    python -m pip install -r requirements.txt

You can serve the documentation locally by running:

    mkdocs serve

Once the environment is created and dependencies installed, you only need to activate it in the future.

## Resources

-   Basic markdown syntax: https://www.markdownguide.org/basic-syntax/
-   `mkdocs` docs: https://www.mkdocs.org/
-   `mkdocs-material` docs, which provides our them and many extensions:
    https://squidfunk.github.io/mkdocs-material/reference/
