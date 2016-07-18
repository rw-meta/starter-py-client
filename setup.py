import setuptools


setuptools.setup(
    setup_requires=['requests'],
    packages=setuptools.find_packages(),
    pbr=True,
)