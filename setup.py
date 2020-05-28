from distutils.core import setup

setup(
    name='trie',
    version='0.1poc',
    packages=setuptools.find_packages(),
    install_requires=[
        'flask',
        'sqlalchemy',
        'flask_sqlalchemy',  
    ],
)