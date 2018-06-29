# #2.1
# print(list(range(1,10,3)))
#
# #2.2
# key=lambda x: len(str(x))
# print(key(111))
#
# #2.3
# print(list(range(6))[::2])
#
# #2.7 8 9
# x = {'a':'b', 'c':'d'}
# print('b' in x.values())
#
# #2.10
# print(1<2<3)

# #2.12
# x = [1, 2, 3, 2, 3]
# x.remove(2)
# print(x)

# #2.14
# x = [1, 2, 3]
# x[len(x)-1:] = [4, 5, 6]
# print(x)

# #2.13
# x = {1:2, 2:3}
# print(x.get(3, 4))
# print(x.get(2, 4))

# #2.17 18
# print({1, 2, 3} | {3, 4, 5} )
# print( {1, 2, 3} | {2, 3, 4} )

# #2.19
# f = lambda x: 5
# print(f(3))

# #2.20
# print(not 3)

# #3.1
# for i in range(1,9):
#     print('\n')
#     for j in range(1,9):
#         if j <= i :
#             print( j,'*',i,'=',j*i,end = '  ')

# #3.2
# for i in range(100,999):
#     a = i // 100
#     b = (i - a * 100 )// 10
#     c = i - a * 100 - b * 10
#     if i == a*a*a + b*b*b + c*c*c :
#         print(i ,end=' ')

# #3.3.1
# f = open('test99.txt','w')
# for i in range(1,9):
#     for j in range(1,9):
#         if j <= i :
#             print(j,'*',i,'=',j*i,end = '  ',file=f)
#     print('\n', file=f)
# f.close()

# #3.3.2
# f = open('test99.txt','r').read()
# print(f)

##