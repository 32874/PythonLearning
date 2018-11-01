
# while循环
- 一个循环语句
- 表示当某条件成立的时候，就循环
- 不知道具体循环次数，但能确定循环的成立条件的时候用while循环
- while语法：

        while 条件表达式
            语句块
            
        #另外一种表达方法：
        while 条件表达式：
            语句块1
        else：
            语句块2


```python
# 如果说年利率是6.7%，本利是每年翻滚，则多少年后本钱会翻倍

benqian = 100000
year = 0
while benqian < 200000:
    benqian = benqian*(1+0.067)
    year += 1 # year = year + 1
    print("第{0}年拿了{1}钱".format(year,benqian))
```

    第1年拿了106700.0钱
    第2年拿了113848.9钱
    第3年拿了121476.77629999998钱
    第4年拿了129615.72031209998钱
    第5年拿了138299.97357301068钱
    第6年拿了147566.07180240238钱
    第7年拿了157452.99861316333钱
    第8年拿了168002.34952024528钱
    第9年拿了179258.5069381017钱
    第10年拿了191268.8269029545钱
    第11年拿了204083.83830545243钱



```python
# 如果说年利率是6.7%，本利是每年翻滚，则多少年后本钱会翻倍
# 如果拿到的钱翻倍，则用print庆祝一下
benqian = 100000
year = 0
while benqian < 200000:
    benqian = benqian*(1+0.067)
    year += 1 # year = year + 1
    print("第{0}年拿了{1}钱".format(year,benqian))
else:
    print("终于翻倍了，很开心")
    print("当年10万可以盖个房子，现在儿子结婚，20万可以给他盖个厨房了")
```

    第1年拿了106700.0钱
    第2年拿了113848.9钱
    第3年拿了121476.77629999998钱
    第4年拿了129615.72031209998钱
    第5年拿了138299.97357301068钱
    第6年拿了147566.07180240238钱
    第7年拿了157452.99861316333钱
    第8年拿了168002.34952024528钱
    第9年拿了179258.5069381017钱
    第10年拿了191268.8269029545钱
    第11年拿了204083.83830545243钱
    终于翻倍了，很开心
    当年10万可以盖个房子，现在儿子结婚，20万可以给他盖个厨房了


# 函数
- 代码的一种组织形式
- 一个函数一般完成一项特定的功能
- 函数使用
    - 函数需要先定义
    - 使用函数，俗称调用


```python
# 定义一个函数
# 只是定义的话不会执行
# 1. def关键字，后跟一个空格
# 2. 函数名，自己定义，起名需要遵循变量命名规则，约定俗成，大驼峰命名只给类用
# 3. 后面括号和冒号不能省，括号内可以有参数
# 4. 函数内所有代码缩进

def func():
    print("我是一个函数")
    print("我要完成一定功能")
    print("我结束了")
```


```python
# 函数的调用
# 直接函数名后面跟括号
func()
```

    我是一个函数
    我要完成一定功能
    我结束了



```python

def func():
    print("我是一个函数")
    print("我要完成一定功能")
print("我结束了")
```

    我结束了



```python
func()
```

    我是一个函数
    我要完成一定功能


### 函数的参数和返回值
- 参数： 负责给函数传递一些必要的数据或信息
    - 形参（形式参数）：在函数定义的时候用到的参数没有具体值，只是一个占位的符号，成为形参
    - 实参（实际参数）：在调用函数的时候输入的值
- 返回值： 函数的执行结果
    - 使用return关键字


```python
# 参数的定义和使用
# 参数person只是一个符号，代表的是调用的时候的某一个数据
# 调用的时候，会用p的值代替函数中所有的person
def hello(person):
    print("{0},你肿么咧".format(person))
    print("Sir，你不理我我就走咧")
    
p = "明月"
hello(p)
```

    明月,你肿么咧
    Sir，你不理我我就走咧



```python
# return语句的基本使用
# 函数打完招呼后返回一句话
def hello(person):
    print("{0},你肿么咧".format(person))
    print("Sir，你不理我我就走咧")
    return "我已经跟{0}打招呼了，{0}不理我".format(person)
p = "明月"
rst = hello(p)
print(rst)
```

    明月,你肿么咧
    Sir，你不理我我就走咧
    我已经跟明月打招呼了，明月不理我



```python
# return案例2
def hello(person):
    print("{0},你肿么咧".format(person))
    return "哈哈，我提前结束了"
    print("Sir，你不理我我就走咧")
    return "我已经跟{0}打招呼了，{0}不理我".format(person)
p = "明月"
rst = hello(p)
print(rst)
```

    明月,你肿么咧
    哈哈，我提前结束了



```python
# 查找函数帮助文档
# 1. 用help函数
help(print)
```

    Help on built-in function print in module builtins:
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    



```python
# 九九乘法表
# version 1.0
for row in range(1,10):
    for col in range(1,row+1):
        # print函数默认任务打印完毕后换行
        print(str(row)+"x"+str(col)+"="+ str(row*col),end="\t")
    print()
```

    1x1=1	
    2x1=2	2x2=4	
    3x1=3	3x2=6	3x3=9	
    4x1=4	4x2=8	4x3=12	4x4=16	
    5x1=5	5x2=10	5x3=15	5x4=20	5x5=25	
    6x1=6	6x2=12	6x3=18	6x4=24	6x5=30	6x6=36	
    7x1=7	7x2=14	7x3=21	7x4=28	7x5=35	7x6=42	7x7=49	
    8x1=8	8x2=16	8x3=24	8x4=32	8x5=40	8x6=48	8x7=56	8x8=64	
    9x1=9	9x2=18	9x3=27	9x4=36	9x5=45	9x6=54	9x7=63	9x8=72	9x9=81	



```python
# 定义一个函数，打印一行九九乘法表
def printLine(row):
    for col in range(1,row+1):
        # print函数默认任务打印完毕后换行
        print(str(row)+"x"+str(col)+"="+ str(row*col),end="\t")
    print()
    
# 九九乘法表
# version 2.0
for row in range(1,10):
    printLine(row)
```

    1x1=1	
    2x1=2	2x2=4	
    3x1=3	3x2=6	3x3=9	
    4x1=4	4x2=8	4x3=12	4x4=16	
    5x1=5	5x2=10	5x3=15	5x4=20	5x5=25	
    6x1=6	6x2=12	6x3=18	6x4=24	6x5=30	6x6=36	
    7x1=7	7x2=14	7x3=21	7x4=28	7x5=35	7x6=42	7x7=49	
    8x1=8	8x2=16	8x3=24	8x4=32	8x5=40	8x6=48	8x7=56	8x8=64	
    9x1=9	9x2=18	9x3=27	9x4=36	9x5=45	9x6=54	9x7=63	9x8=72	9x9=81	


## 参数详解
- [参考资料](https://www.cnblogs.com/bingabcd/p/6671368.html)
- python参考资料： headfirst python -> 零基础入门学习python（小甲鱼）--> 习题 -->后期可以考虑腾讯公开免费课
- 参数分类
    - 普通参数
    - 默认参数
    - 关键字参数
    - 收集参数
- 普通参数
    - 参见上个例子
    - 定义的时候直接定义变量
    - 调用的时候直接把变量或者值放入指定位置
    
                def 函数名(参数1,参数2,...):
                    函数体
                    
                # 调用
                函数名(value1,value2,...)
                
                # 调用的时候，具体值参考的是位置，按位置赋值
- 默认参数
    - 形参带有默认值
    - 调用的时候，如果没有对相应的形参赋值，则使用默认值
    
                def  func_name(p1=v1,p2=v2......):
                    func_block
                    
                # 调用1
                func_name()
                
                # 调用2
                value1 = 100
                value2 = 200
                func_name(value1,value2)


```python
# 默认参数示例
# 报名函数，需要知道学生性别
# 学习python的学生基本都是男生，所以，报名的时候瑞国没有特别指定，我们认为是男生
def reg(name,age,gender='male'):
    if gender == 'male':
        print("{0} is {1}, and he is a good student".format(name,age))
    else:
        print("{0} is {1}, and she is a good student".format(name,age))
    
```


```python
# 调用默认参数函数案例1
reg("mingyue",21)
reg("xiaojing",23,"female")
```

    mingyue is 21, and he is a good student
    xiaojing is 23, and she is a good student

