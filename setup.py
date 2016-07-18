import setuptools

setuptools.setup(
    name='starter_api',
    version='0.0.1',
    author='Artur Geraschenko',
    author_email='arturgspb@gmail.com',
    summary='Client for Starter Server API',
    description_file='README.rst',
    license='MIT',
    home_page='https://github.com/rw-meta/starter_api-py-client',
    setup_requires=['requests'],
    packages=setuptools.find_packages(),
    pbr=True,
)
