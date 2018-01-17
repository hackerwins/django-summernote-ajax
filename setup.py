import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(name='tutorial-python-build',
      version='0.1',
      packages=find_packages(exclude=['docs', 'sandbox']),
      description='A Django Library for jQuery File Upload',
      long_description=README,
      url='https://www.pincoin.info/',
      author='Jonghwa Seo',
      author_email='mairoo' '@' 'pincoin.info',
      license='MIT',

      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],

      install_requires=[
      ],
      setup_requires=[
      ],
      scripts=[
      ],

      test_suite='tests.get_test_suite',
      tests_require=[
      ],

      zip_safe=False,
      ),
