"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

setup(
	name='attending',
	version='0.0.1',
	description='A manager for offline documentation',
	url='https://github.com/ivanov/attending',
	packages=find_packages(exclude=['fizbuz', 'foobar', 'latest', 'prior-work', 'tests', 'versionless']),
	python_requires='>=3.6',
)

