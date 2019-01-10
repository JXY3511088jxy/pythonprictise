#coding:utf-8
'''
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''
'''创建格式：
parame = {value01,value02,...}
或者
set(value)
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 这里演示的是去重功能
{'orange', 'banana', 'pear', 'apple'}

print('orange' in basket)  # 快速判断元素是否在集合内

print('crabgrass' in basket)


 # 下面展示两个集合间的运算.

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # 集合a中包含而集合b中不包含的元素
print(a | b)  # 集合a或b中包含的所有元素
print(a & b)  # 集合a和b中都包含了的元素
print(a ^ b)  # 不同时包含于a和b的元素

'''集合的基本操作'''
'''1、添加元素'''
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)
'''还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：'''
thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1,3})
print(thisset)
thisset.update([1,4],[5,6])
print(thisset)

'''2、移除元素'''
thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
print(thisset)
#thisset.remove("Facebook")   # 不存在会发生错误
'''此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：'''
thisset = set(("Google", "Runoob", "Taobao"))
#thisset.discard("Facebook")  # 不存在不会发生错误
print(thisset)
'''我们也可以设置随机删除集合中的一个元素，语法格式如下：'''
thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset.pop()

print(x)
print(thisset)

'''3、计算集合元素个数'''
thisset = set(("Google", "Runoob", "Taobao"))
len(thisset)

'''4、清空集合'''
thisset = set(("Google", "Runoob", "Taobao"))
thisset.clear()
print(thisset)

'''5、判断元素是否在集合中存在'''
thisset = set(("Google", "Runoob", "Taobao"))
print("Runoob" in thisset)

print("Facebook" in thisset)


