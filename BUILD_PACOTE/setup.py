from setuptools import setup

setup(
    name='meupacote',
    packages=['package'],
    version='0.0.2',
    install_requires=['httpx'],
    entry_points={
        'console_scripts':['my-cli = package.myLib:cli']
    }
)