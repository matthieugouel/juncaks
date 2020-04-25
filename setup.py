"""Setup for juncaks package."""

from setuptools import setup, find_packages

setup(
    name="juncaks",
    version="0.1.0",
    author="Matthieu Gouel",
    author_email="matthieu.gouel@gmail.com",
    url="https://github.com/matthieugouel/juncaks",
    description="Markov chain-based generator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[],
)
