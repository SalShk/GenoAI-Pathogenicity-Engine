from importlib.metadata import version

# This file's main job is to define the package version.
# The main.py launcher will handle other imports when it needs them.
__version__ = version("genoai_pathogenicity_engine")

__all__ = ["__version__"]