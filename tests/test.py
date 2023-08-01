"""
以下内容均译制于官网文件，侵权必删
"""

import pyttsx3

engine = pyttsx3.init()  # 创建对象

"""语速"""
rate = engine.getProperty('rate')
print(rate)  # 打印当前语速
engine.setProperty('rate', 125)

"""音量"""
volume = engine.getProperty('volume')  # 获取当前音量（最小为0，最大为1）
print(volume)  # 打印当前音量
engine.setProperty('volume', 1.0)  # 在0到1之间重设音量

# """发音"""
# voices = engine.getProperty('voices')  # 获取当前发音的详细信息
# # engine.setProperty('voice',voices[0].id) #更改发音参数
# engine.setProperty('voice', voices[1].id)  # 更改发音参数

"""朗读"""  # 这里朗读的内容没有翻译，因为翻译的话可能运行时会有问题

engine.say("兄弟们!全体目光向我看齐!看我看我!我宣布个事!我, 就是个傻逼!!没毛病啊!")
engine.runAndWait()

engine.runAndWait()
# 请将一下Python代码翻译成C++代码:
print("Hello World!")
