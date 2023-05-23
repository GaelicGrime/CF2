import pathlib

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="CSCF",
    version="0.2.3-1",
    author="GaelicGrime",
    author_email="will.angus.blaylock@gmail.com",
    url="https://github.com/ComfortableSoftware/commonFunctions_py",
    description="Opinionated wrappers around many libraries.",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    install_requires=[],
    # classifiers=[],
    python_requires=">=3.2",
)
