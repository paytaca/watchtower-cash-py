from setuptools import setup
from watchtower import __version__
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='watchtower-cash-py',
    version=__version__,    
    description='Library for building Python applications that integrate with Watchtower.cash',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/paytaca/watchtower-cash-py',
    author='Joemar Taganna',
    author_email='joemar@paytaca.com',
    license='MIT',
    packages=['watchtower'],
    install_requires=['requests>=2.22.0'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.8',
    ],
)
