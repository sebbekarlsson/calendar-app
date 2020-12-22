from setuptools import setup, find_packages


setup(
    name='calendarapp',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'mock',
        'pytest-cov'
    ]
)