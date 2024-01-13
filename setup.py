from setuptools import setup, find_packages
from version import __version__


# setup.py for the dog_app project
# This setup is primarily configured to facilitate testing across different modules.
# By packaging dog_app, other modules or test suites can easily import and test its components.

setup(
    name='dog_app',
    version=__version__,
    packages=find_packages(),
)
