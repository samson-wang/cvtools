from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'cvtools',
    packages = ['cvtools'], 
    version = '0.0.2',
    description = 'OpenCV tools for CV applications',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Samson Wang',
    author_email = 'samson.c.wang@gmail.com',
    url = 'https://github.com/samson-wang/cvtools.git', 
    keywords = ['opencv', 'image', 'http'], # arbitrary keywords
    classifiers = [],
)

