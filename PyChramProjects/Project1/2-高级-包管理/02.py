# 借助于importlib包可以实现导入以数字开头的模块名称
import importlib
tuling = importlib.import_module('01')
stu = tuling.Student()
stu.say()