import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="khoaikeyex",
    version="0.0.1",
    author="Lê Huỳnh Đức",
    author_email="lhduc94@gmail.com",
    description="Keyword Extraction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lhduc94",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
