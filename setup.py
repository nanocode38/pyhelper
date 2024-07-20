from distutils.core import setup
from setuptools import find_packages

with open('README.md', 'r', encoding='utf-8', errors='replace') as f:
    long_description = f.read()

setup(name='pyhelper',  # 包名
      version='2.1.0',  # 版本号
      description='A tool set for complementing Python and Pygame',
      long_description=long_description,
      author='nanocode38',
      author_email='2602422835@qq.com',
      url='https://github.com/nanocode38/pyhelper.git',
      install_requires=['pghelper', 'requests'],
      license='BSD License',
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
