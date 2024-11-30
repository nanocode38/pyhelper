from distutils.core import setup
from setuptools import find_packages

from pyhelper import __version__

with open('README.md', 'r', encoding='utf-8', errors='replace') as f:
     long_description = f.read()

requires = list()
with open('requirements.txt', 'r', errors='replace') as f:
    line = f.readline()
    l = ''
    for i in range(len(line)):
        if (not line[i].isalpha() and line[i] != '_'):
            l = line[:i]
            break
    requires.append(l)

setup(name='pyhelper',
      version=__version__,
      description='A tool set for complementing Python and Pygame',
      long_description=long_description,
      author='nanocode38',
      author_email='2602422835@qq.com',
      url='https://github.com/nanocode38/pyhelper.git',
      install_requires=requires,
      license='MIT License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12',
          'Topic :: Software Development :: Libraries'
      ],
      )
