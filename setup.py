from setuptools import setup, find_packages

setup(
    name='testpackage',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/d1stadeyemi/testpackage.git',
    author='Muhammad Ajagbe',
    author_email='d1stadeyemi@gmail.com'
)