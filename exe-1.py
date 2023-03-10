# 整数，浮点数（小数，8，16，32，64），字符串，list，tuple，dict，set，bool

a = 10 + 2
a = 10 ** 3

b = 10.1
# b = b**2

c = int(b+0.5)

d = "adfa"
e = 'dsdf\'asdasd' #

f = "1234567"
print(f[1:5:1])

print(f[-1:-3])

list1 = [12,3,4,5,6,"asdfas",23.3,[123],["sadfs"]]

list2 = [[1,2,0],[3,4,5],[4,5,7]]
print(list2[0])

list2[0] = "sdfsdf"  # malloc
print(list2)

# t1 = (3,4,5,6)
# print(t1[0])
# # t1[0] = 43
#
# f = "123稍等4567asdfasdfa1335657" #
# print(f[0])
#
# f[0] = "s"

a = (1,3)
b = (10)
c = (2,)
d = 3,4,5,7



print(type(d))

# list1 = [1,2,(3,4,[5,6])]
#
# # j = list1
# # e,f = list1  # 解包
# # g,h,i = list1
# # g,h,i,e,c = list1
#
# # a,b,c,d = list1  # 解包
#
# a,b,(c,d,(e,f)) = list1
#
# a,b,c = list1
# a,b,(c,d,e) = list1
#
# print(a,b,c,d,e,f)


list1 = [(1,2,"a"),(3,4,"b"),(5,6,"c"),(7,8,"d")]

a,b,c = zip(*list1)

print(a)
print(b)
print(c)

# d = {"a":0,"b":1,"c":2}
#
# v = tuple(d.values())
# k = list(d.keys())
#
# print(type(d.values()))





# print(d.get("f","sdfs"))
#
# print(d["f"])
#
# d["f"] = 1000


# print(d)

# d["asdf"] = 123
# d["a"] = 456
# print(type(d))
# print(d)
#
# d.pop("a")
# print(d)
#
# del d["asdf"]
#
# print(d)

list1 = [ {"学号":1234,"姓名":"布丁","sex": "nan"} ,
          {"学号":123,"姓名":"张三","sex": "nan"},
          {"学号":12345,"姓名":"李四","sex": "nv"} ]

# list2 = [1234,123,12345]
# list3 = ["布丁","张三","李四"]

nums,names,sexes = zip(*[i.values() for i in list1])

print(nums)
print(names)
print(sexes)


set1 = {1,2,3,4,5,1} #

list1 = [12,234,54,56,1,2,43,1,2]
list2 = list(set(list1))
print(list2)

# print(set1[0])

# for i in set1:
#     print(i)


# for i in range(len(set1)):
#     print(set1[i])

#
# a = True
# b = False
# c = 10
#
#
# if "2": # 0 None False [] "" {}
#     print("hello")
#
# if b:
#     print("world")

# list1 = [12,3,4,5]
# list2 = [12,3,4,6]
#
# set1 = {1,2,3,1}
# set2 = {3,2,1,3,1,}
#
# print(id(set1))
# print(id(set2))

a = 30000000000000000
b = 30000000000000000
print(id(a))
print(id(b))

c = "123"
d = "123"
print(id(c))
print(id(d))  # 深拷贝  浅拷贝




# print(set1)
# print(set2)
#
# if set1 == set2:
#     print("hello")

a = range(0,10,1)

for i in a:
    print(i)