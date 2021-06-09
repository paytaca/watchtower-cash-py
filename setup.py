from setuptools import setup

setup(
    name='watchtower-cash-py',
    version='0.1.0',    
    description='Library for building Python applications that integrate with Watchtower.cash',
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
