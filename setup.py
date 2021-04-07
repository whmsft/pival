from setuptools import setup

with open("readme.rst", "r") as fh:
   long_description = fh.read()

setup(
    name='pyval',
    version='1.0',    
    description= "python module for pi's value!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Whirlpool-Programmer/pival',
    author='Whirlpool-Programmer',
    author_email='whirlpool.programmer@outlook.com',
    license='MIT License',
    packages=['pival'],
    classifiers =[
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    ]
)
