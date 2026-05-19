from setuptools import setup

setup(name='wos_explorer',
      version='0.11.0',
      description='Utility scripts to find article records within the Web of Science data set.',
      long_description='Explore the JSON converted data representation of the Clarivate Web of Science data set. Requires institutional access to the data set.',
      classifiers=[ 'Topic :: Text Processing' ],
      keywords='search analysis citations',
      url='https://github.com/UW-Madison-Library/wos-explorer',
      author='UW-Madison Library Technology Group',
      author_email='ltghelpdesk@library.wisc.edu',
      license='MIT',
      packages=['wos_explorer'],
      install_requires=['nltk'],
      zip_safe=False)
