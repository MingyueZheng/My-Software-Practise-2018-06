# #Momning 
# # 有这样的三个列表，即：
# # list1=[1,2,3,4,5,6,6]
# # list2=['ab','bc','bb','bc','dd','ef','kk']
# # list3=['abc','def','ccc','ddd']
# # 要求：
# # 1. 将list1和list2组成一个字典dict1，以list1为键，list2为值（需运用集合考虑键值重复问题）；
# # 2. 将list1和list3组成一个字典dict2，以list1为键，list3为值；
# # 3. 根据list1生成元组T1，要求T1的值和list1的内容完全一致；
# # 4. 想list1中添加元素‘7’，并进行相应的处理，使之最后list1的内容为[1，2，3，5，7](注不允许直接赋值）。
#
# list1=[1,2,3,4,5,6,6]
# list2=['ab','bc','bb','bc','dd','ef','kk']
# list3=['abc','def','ccc','ddd']
#
# list1 = set(list1)
# list2 = set(list2)
#
# #1
# dict1 = dict(zip(list1,list2))
# print('dict1:',dict1)
# #2
# dict2 = dict(zip(list1,list3))
# print( 'dict2:',dict2)
# #3
# T1 = tuple(list1)
# print('T1:',T1)
# #4
# list1 = [1,2,3,4,5,6,6]
# list1.append(7)
# list1.remove(6)
# list1.remove(6)
# print(list1)
# #5
# list1 = [1,2,3,4,5,6,6]
# count = {}
# for i in list1:
#     count[i] = count.get(i,0) +1
# print(count)

#Afternoon
# 2.1
alist=[10,20,'a','bcd',[1,2,3]]
print(alist[-1])
print(alist[4][-2])
print(alist[0])
#print(alist[6])

#3.1
alist=[1,2,3,'abc','def',3,5]
print(alist[::-1])

#3.2
#第一种方法:直接赋值
member = ['金鱼', '黑夜', '迷途', '怡静', '太阳']
member.insert(1,88)
member.insert(3,90)
member.insert(5,85)
member.insert(7,90)
member.insert(9,88)
print('第一种方法：',member)

#第二种方法：
num = [88,90,85,90,88]
member = ['金鱼', '黑夜', '迷途', '怡静', '太阳']
new = []
for i in range(5):
        new.append(member[i])
        new.append(num[i])
print(new)

#3.3
list1 = [1, [1, 2, ['小金鱼']], 3, 5, 8, 13, 18]
list1[1][2] = '章鱼保罗'
print(list1)

#3.4
list2 = [1, 8, 2, 3, 5, 8, 13, 18]
list2.sort()
print(list2)

#3.5
dict1 = {1:'tony',2:'tom',3:'john',4:'tony'}
list1 = ['a','b','c','d']
list2 = ['aaaa','cccc','dddd','eeee']
dict2 = dict(zip(list1,list2))
print('dict1[3]:',dict1[3])
print('dict2[b]',dict2['b'])
dict1[3] = dict2['b']
dict2['b'] = 'ffff'
print('dict1',dict1,'\ndict2',dict2)

