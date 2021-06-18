import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ds-tools-vnhso",
    version="1.0.0",
    author="vnhso",
    author_email="vchsiao36@gmail.com",
    description="Test Package for building data structures easily",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vnhso/datastructurestool",
    project_urls={
        "Bug Tracker": "https://github.com/vnhso/datastructurestool/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)