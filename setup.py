from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='echostatenetwork',
    version='0.1',
    description='Echo State Network package using python 2.7',
    author='Nathaniel Rodriguez',
    packages=['echostatenetwork'],
    url='https://github.com/Nathaniel-Rodriguez/echostatenetwork.git',
    install_requires=[
          'networkx',
          'numpy',
          'matplotlib'
      ],
    include_package_data=True,
    zip_safe=False)
