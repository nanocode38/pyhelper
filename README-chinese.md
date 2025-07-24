# PyHelper - 一个为Python提供更多辅助工具的包


[英文版本 - English Version](README.md)

PyHelper是补充Python和Pygame开发的强大工具集。增强你与我们的实用工具和帮助者的编码经验。

## 为什么选择PyHelper?
PyHelper精简了Python和Pygame的开发，提供了一套全面的实用工具，旨在：
- 加速开发时间
- 简化复杂任务
- 增强代码性能
- 降低样板代码

## 下载包
这个包已经发布到了PyPI, 所以可以直接使用pip安装

Windows下使用命令:
```commandline
python -m pip install nanocode38-pyhelper
```

类UNIX系统下使用命令:
```bash
pip3 install nanocode38-pyhelper
```

在虚拟环境中直接使用pip即可。记得先激活虚拟环境!
```commandline
pip install nanocde38-pyhelper
```

为检查是否安装成功, 可以使用Python来试图导入:
```bash
$ python
Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyhelper
PyHelper 2.6.1 (Microsoft Windows, Python 3.13.5)
Hello from the PyHelper community! https://githun.com/nanocode38/pyhelper.git
>>>
```
*注: 您导入过程中打印的提示取决于您使用的Python版本和PyHelper版本, 也许和这里展示的不太一样*

如果安装失败, 导入也会失败:
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

## 为什么叫nanocode38-pyhelper而不是pyhelper?
PyPI自2023年以来拒绝发布与现有项目名称视觉/拼写相似度过高的新包名（即使不完全相同），目的是防止仿冒包和用户混淆。在PyPI上已经有了PyHelper以及与PythonHelper类似的包, 所以采用主要开发者名-包名的方式发布, 但是导入是请依然使用pyhelper


## 贡献

如果您想为PyHelper做出贡献，请查看 https://github.com/nanocode38/pyhelper.git
