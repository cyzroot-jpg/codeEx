lst = list(range(10))               # 从 range 对象
for i in lst:
    print(i)
print("---------------------")
lst = list("hello")                 # 从字符串
for i in lst:
    print(i)
print("---------------------")
lst = list({1, 2, 3})               # 从集合（顺序不确定）
for i in lst:
    print(i)
print("---------------------")
lst = list((1, 2, 3))               # 从元组
for i in lst:
    print(i)