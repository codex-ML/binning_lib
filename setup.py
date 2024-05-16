from setuptools import setup, find_packages

setup(
    name='bin_lookup',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='ANISH',
    description='A module for performing BIN lookup using the binlist.net API and CC genrator ',
    url='https://github.com/codex-ML/CreaditsCardTools',
)
