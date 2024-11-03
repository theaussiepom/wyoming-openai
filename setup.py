"""Python setup.py for wyoming_openai package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("wyoming_openai", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="wyoming_openai",
    version=read("wyoming_openai", "VERSION"),
    description="Awesome wyoming_openai created by theaussiepom",
    url="https://github.com/theaussiepom/wyoming-openai/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="theaussiepom",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["wyoming_openai = wyoming_openai.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
