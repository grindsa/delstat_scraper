""" setup.py """
from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

setup(name='delstat_scraper',
    version='0.1.2',
    description='a webscraper for the penny-del statistic pages',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/grindsa/delstat_scraper',
    author='grindsa',
    author_email='grindelsack@gmail.com',
    license='GPL',
    packages=['delstats'],
    platforms='any',
    install_requires=[
        'bs4',
        'requests',
    ],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: German',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    zip_safe=False,
    test_suite="test")
