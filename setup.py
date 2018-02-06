from setuptools import (
    setup, find_packages
)

from django_summernote_ajax import (
    VERSION, PROJECT, AUTHOR
)

setup(
    name=PROJECT,
    version=VERSION,
    description='Yet another Summernote plugin for Django',
    keywords='Django,Summernote,jQuery',
    author=AUTHOR,
    maintainer='django-summernote-ajax maintainers',
    url='http://github.com/summernote/django-summernote-ajax',
    license='MIT',
    zip_safe=False,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    packages=find_packages(exclude=['sandbox', 'sandbox_app', 'docs', 'tests']),
    include_package_data=True,

    install_requires=[
        'Django',
    ],
    setup_requires=[
    ],
    scripts=[
    ],

    test_suite='runtests.runtests',
    tests_require=[
    ],
),
