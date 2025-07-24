# PyHelper - A Package Providing Additional Utility Tools for Python  

[Chinese Version - 中文版本](README-chinese.md)

PyHelper is a powerful toolkit that complements Python and Pygame development. It enhances your coding experience with our practical utilities and helpers.  

## Why Choose PyHelper?  
PyHelper streamlines Python and Pygame development by providing a comprehensive set of utility tools designed to:  
- Accelerate development time  
- Simplify complex tasks  
- Enhance code performance  
- Reduce boilerplate code  

## Download the Package  
This package has been published to PyPI, so you can install it directly using pip.  

For Windows, use the following command:  
```commandline  
python -m pip install nanocode38-pyhelper  
```  

For UNIX-like systems, use the command:  
```bash  
pip3 install nanocode38-pyhelper  
```  

In a virtual environment, you can directly use pip. Remember to activate the virtual environment first!  
```commandline  
pip install nanocde38-pyhelper  
```  

To check if the installation was successful, you can try importing it with Python:  
```bash  
$ python  
Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32  
Type "help", "copyright", "credits" or "license" for more information.  
>>> import pyhelper  
PyHelper 2.6.1 (Microsoft Windows, Python 3.13.5)  
Hello from the PyHelper community! https://githun.com/nanocode38/pyhelper.git  
>>>  
```  
*Note: The prompt printed during import may vary depending on your Python version and PyHelper version, and might not exactly match what is shown here.*  

If the installation fails, the import will also fail:  
```bash  
$ python  
Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32  
Type "help", "copyright", "credits" or "license" for more information.  
>>> import pyhelper  
Traceback (most recent call last):  
  File "<python-input-0>", line 1, in <module>  
    import pyhelper  
ModuleNotFoundError: No module named 'pyhelper'  
>>>   
```  

## Why Is It Called nanocode38-pyhelper Instead of pyhelper?  
Since 2023, PyPI has rejected the publication of new package names that are visually or spelling-wise too similar to existing projects (even if not identical), aiming to prevent imitation packages and user confusion. Since PyHelper and PythonHelper-like packages already exist on PyPI, the package is published under the format of "main developer name-package name," but you should still use `import pyhelper` for importing.  

## Contribution  

If you'd like to contribute to PyHelper, please visit on [GitHub](https://github.com/nanocode38/pyhelper.git)
