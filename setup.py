from os.path import dirname, join, realpath
from setuptools import setup


__version__ = '1.3.2'


with open('README.md') as f:
    readme = f.read()

with open(join(dirname(realpath(__file__)), 'requirements.txt')) as f:
    PACKAGE_INSTALL_REQUIRES = [line[:-1] for line in f]


setup(
    version=__version__,
    name='Fever-FuelSDK',
    description='Fever Salesforce Marketing Cloud Fuel SDK for Python',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Feverup',
    py_modules=['ET_Client'],
    python_requires='>=3',
    packages=['FuelSDK'],
    url='https://github.com/Feverup/FuelSDK-Python',
    license='MIT',
    install_requires=PACKAGE_INSTALL_REQUIRES,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.7',
    ],
)