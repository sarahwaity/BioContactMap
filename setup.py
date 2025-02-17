from setuptools import setup, find_packages

setup(
    name="BioContactMap",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "biopandas==0.5.1",
        "numpy==1.24.3",
        "matplotlib==3.7.2",
        "pandas==1.5.3",
        "seaborn==0.13.2"
    ],

    author="Sarah Wait",
    author_email="Sarah.j.wait@gmail.com",
    description="A package to create protein contact maps from PDB files",
    long_description=open('README.md').read(),  # Read the README file for detailed description
    url="https://github.com/sarahwaity/BioContactMap",
    classifiers=[  # Useful for PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)