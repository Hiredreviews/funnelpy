import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="funnelpy",
    version="0.3.1",
    description="Create a funnel plot.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/lyonjust/funnelpy",
    author="Justin Lyons",
    author_email="lyonjust@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    packages=['funnelpy'],
    install_requires=["pandas", "matplotlib", "seaborn"],
)