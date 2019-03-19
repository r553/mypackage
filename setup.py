from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='This library was created for recursive functions and sorting functions',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<r553>/<mypackage>',
    author='<Rethabile Mphahlele>',
    author_email='<rethabile553@gmail.com>'
    )
