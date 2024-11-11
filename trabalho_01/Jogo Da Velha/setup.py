from setuptools import setup, find_packages

setup(
    name='jogo_da_velha',
    version='1.0',
    description='Jogo da velha funcional em python',
    install_requires=['random', 'abc'],
    packages=find_packages()
)