#coding:utf-8
'''
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中.
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
'''
'''访问字典里的值'''
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

'''修改字典：向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对'''
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8;  # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

'''删除字典元素'''
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del dict['Name']  # 删除键 'Name'
dict.clear()  # 清空字典
del dict  # 删除字典

#print("dict['Age']: ", dict['Age'])
#print("dict['School']: ", dict['School'])

'''
字典键的特性
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
两个重要的点需要记住：
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住；
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行。
'''
dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}

print("dict['Name']: ", dict['Name'])

dict = {['Name']: 'Runoob', 'Age': 7}  #键值不能用列表，不然会报错

print("dict['Name']: ", dict['Name'])