from setuptools import setup, find_packages

setup(
    name="pineapple-pager-api",       
    version="0.1.0",                         
    author="tpollard64",
    description="Python library for interacting with WiFi Pineapple Pager devices",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tpollard64/pineapple-pager-python-api",
    packages=find_packages(),
    install_requires=[
        "paramiko",                            
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
