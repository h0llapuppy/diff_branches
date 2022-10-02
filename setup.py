from setuptools import setup, find_packages
from os.path import join, dirname\

import get_diff_branches

setup(
    name='get_diff_branches',
    version=get_diff_branches.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)
