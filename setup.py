import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smath2018b",
    version="0.0.1",
    author="Eric Appelt",
    author_email="eric.appelt@gmail.com",
    description="Serious Math",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/appeltel/smath2018b",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': ['fib=smath2018b.fib:fib_cli']
    },
)
