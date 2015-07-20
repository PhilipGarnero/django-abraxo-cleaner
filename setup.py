from setuptools import setup, find_packages

setup(
    name='django-abraxo-cleaner',
    version=__import__('abraxo_cleaner').__version__,
    description=__import__('abraxo_cleaner').__doc__,
    long_description=open('README.rst').read(),
    author='Philip Garnero',
    author_email='philip.garnero@gmail.com',
    url='https://github.com/PhilipGarnero/django-abraxo-cleaner',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'django>=1.4.0'
    ],
    include_package_data=True,
    zip_safe=False,
)
