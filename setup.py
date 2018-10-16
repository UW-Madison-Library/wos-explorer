from setuptools import setup

setup(name='wos_explorer',
      version='0.1',
      description='Utility scripts to find article records within the Web of Science data set.',
      long_description='Explore the JSON converted data representation of the Clarivate Web of Science data set. Requires institutional access to the data set.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python 3.5',
        'Topic :: Text Processing',
      ],
      keywords='search analysis',
      url='https://gitlab.library.wisc.edu/ltg/wos-explorer',
      author='UW-Madison Library Technology Group',
      author_email='ltghelpdesk@library.wisc.edu',
      license='MIT',
      packages=['wos_explorer'],
      install_requires=[],
      tests_require=['pytest'],
      zip_safe=False)
