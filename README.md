# PyHelper - A packages that provide more helper tools for Python


这是一个为Python提供更多辅助工具的包

This is a Packages that provide more helper tools for Python

## 下载包  Downloading packages
此包暂时没有发布到PyPi(名称重名),因此无法使用pip安装。如果你的电脑安装了Git，请使用
方法2或方法3安装，如果没有安装Git，请使用方法1。

This package has not yet been published to PyPi(the name is the same),
so it cannot be installed using pip. If Git is installed on your computer, use
Method 2 or Method 3 install, or Method 1 if you don't have Git installed.
### 方法1  Method 1:
首先访问此包的官方网站：https://github.com/nanocode38/pyhelper.git
点击网站里的绿色Code按钮，这将展开一个菜单。选择Local模块，然后单击菜单最下方
的Download ZIP按钮即可下载源代码ZIP版。

First visit to the package's official website: https://github.com/nanocode38/pyhelper.git
Click the green Code button on the site, which opens a menu.
Select the Local module, and then click at the bottom of the menu
Download ZIP button to download the source code ZIP version.

解压ZIP,将pyhelper文件夹复制/移动到Python目录下的Lib目录下的site-packages目录,即:

Unzip the ZIP and copy/move the pyhelper folder to the site-packages directory
in the Lib directory inside the Python directory, that is:
```commandline
[Python Path]\Lib\site-packages
```
### 方法2  Method 2:
在终端来到以下目录:

In the terminal, go to the following directory:
```commandline
[Python Path]\Lib\site-packages
```
其中[Python Path]是你的Python所在目录

Where [Python Path] is the directory where your Python is located

接着执行以下命令:

Next, execute the following command:
```commandline
git clone https://github.com/nanocode38/pyhelper.git
```

### 方法3  Method 3:
新建Python文件,输入以下内容:

In a new Python file, enter the following:
```python
import os
import sys

_PYTHON_PATH = sys.executable[:-11]
if os.name == 'nt' and _PYTHON_PATH[-6:] == 'Script':
    _PYTHON_PATH = _PYTHON_PATH[:-7]
elif os.name == 'posix' and _PYTHON_PATH[-3:] == 'bin':
    _PYTHON_PATH = _PYTHON_PATH[:-4]
_PYTHON_PATH = os.path.join(_PYTHON_PATH, 'Lib', 'site-packages', 'pyhelper')

os.chdir(_PYTHON_PATH)
try:
    os.chdir(r".\pyhelper")
except FileNotFoundError:
    pass
else:
    os.chdir('..')
    os.system('rd /s /q pyhelper')
os.system('git clone https://github.com/nanocode38/pyhelper.git')
os.system("is_pause")
```
使用Python运行此程序,即可安装。

*注:如果需要在虚拟环境中安装,请使用虚拟环境的Python来运行此程序!*

To install, run this program using Python.

*Note: If you need to install in a virtual environment, use the virtual environment's Python to run this program!*


## 贡献 contribution
如果您想为PyHelper做出贡献，请查看 https://github.com/nanocode38/pyhelper.git

If you want to contribute to PyHelper, see https://github.com/nanocode38/pyhelper.git