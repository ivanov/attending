"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup

setup(
	name='attending',
	version='0.0.1',
	description='A manager for offline documentation',
	url='https://github.com/ivanov/attending',
	packages=['attending'],
	python_requires='>=3.6',
	package_data={
        'attending': ['index.csv'],
    },
)
