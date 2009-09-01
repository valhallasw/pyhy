from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pyhy',
      version=version,
      description="Library to access Hyves using its API",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Merlijn van Deen',
      author_email='valhallasw@arctus.nl',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
	'oauth',
	'enum'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
