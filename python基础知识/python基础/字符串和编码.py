#-*- coding: utf-8 -*-
'''
格式化：最后一个常见的问题是如何输出格式化的字符串。我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，
余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。
占位符	替换内容
%d	    整数
%f	    浮点数
%s	    字符串
%x	    十六进制整数
'''
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

'''
另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，
不过这种方式写起来比%要麻烦得多
'''
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

'''
Python 访问子字符串，可以使用方括号来截取字符串
'''
var1 = 'Hello World'
var2 = "Runoob"
print("var1[0]:",var1[0])
print("var2[1:5]:"+var2[1:5])

'''
操作符	                                描述	                             实例
+	                                字符串连接	a + b               输出结果： HelloPython
*	                                重复输出字符串	a*2                 输出结果：HelloHello
[]	                                通过索引获取字符串中字符	a[1]            输出结果 e
[ : ]	        截取字符串中的一部分，遵循左闭右开原则，str[0,2] 
                                是不包含第 3 个字符的。	a[1:4]              输出结果 ell
in	                成员运算符 - 如果字符串中包含给定的字符返回 True	'H' in a    输出结果 True
not in	        成员运算符 - 如果字符串中不包含给定的字符返回 True	'M' not in a    输出结果 True
r/R	    原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，
        没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r
        （可以大小写）以外，与普通字符串有着几乎完全相同的语法。	
                                                                          print( r'\n' )
                                                                        print( R'\n' )
'''

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')
