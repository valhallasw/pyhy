from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pyhy',
      version=version,
      description="Library to access Hyves using its API",
      long_description="""\
""",
      classifiers=[
      "Development Status :: 2 - Pre-Alpha",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Natural Language :: English",
      "Operating System :: OS Independent",
      "Programming Language :: Python :: 2.5",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Merlijn van Deen',
      author_email='valhallasw@arctus.nl',
      url='http://github.com/valhallasw/pyhy',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
	'oauth >= 1.0',
	'enum >= 0.4'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
