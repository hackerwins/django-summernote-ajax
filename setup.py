import os

from setuptools import (
    setup, find_packages
)

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(name='django-summernote-ajax',
      version='0.0.1',
      packages=find_packages(exclude=['docs', 'sandbox', 'sandbox_app']),
      description='Django plugin for summernote',
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
          'Framework :: Django :: 1.8',
          'Framework :: Django :: 1.11',
          'Framework :: Django :: 2.0',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],

      install_requires=[
          'Django',
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
