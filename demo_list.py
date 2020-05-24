'''This is a demo of list'''
# 如何构建一个list
# 直接用[]构造。纯数字list，纯字符串list，混合list
print("----------------------构造list-----------------------")
list_numbers = [1, 3, 4, 2, 10]
list_strs = ["a", "b", "d", "c", "f", "e"]
list_complex = [1, "a", 2, "c"]
print(list_numbers)
print(list_strs)
print(list_complex)
# 使用List工厂函数构造
list_from_range = list(range(10))
list_from_list = list(list_numbers)
print(list_from_range)
print(list_from_list)
# 使用表达式构造
list_from_iters = [x for x in list_numbers if x > 3]
list_strs_numbers = ["egg%s" % i for i in range(10)]
print(list_from_iters)
print(list_strs_numbers)
print("----------------------list中增加元素-------------------")
# 往list中增加元素
# 增加一个元素
list_numbers.append(11)
print("往list_numbers中增加一个11之后 :" + str(list_numbers))
# 增加多个元素，入参为迭代器
list_numbers.extend(range(3))
print("after extend a range :" + str(list_numbers))
# 在某个index位置增加一个元素
list_numbers.insert(1, 2)
print("insert 2 at index 1 :" + str(list_numbers))
# 修改List中的元素
list_from_list[0] = 1000
print("after modify list_from_list[0] :" + str(list_from_list))
list_from_list.reverse()
print(list_from_list)
print("--------------------------list中删除元素-----------------------")
# 删除list中某个元素，若删除的元素不存在会 raise error
list_from_list.remove(list_from_list[0])
print("after remove the value of index 0 :" + str(list_from_list))
try:
    list_from_list.remove(200)
except ValueError as err:
    print(err)
list_from_list.pop()
print(list_from_list)
list_from_list.pop(0)
print(list_from_list)
del list_from_list[0]
print(list_from_list)
list_from_list.clear()
print(list_from_list)

print("---------------------------计数----------------------------")
# 获取list中某个元素的index，元素不存在raise value error
index_a = list_complex.index("a")
print(index_a)
try:
    index_b = list_complex.index("b")
    print(index_b)
except ValueError as error:
    print(error)

# 计数
# list的总个数
length = len(list_from_range)
print(length)
list_from_range.extend(list_from_range)
print(list_from_range)
count_0 = list_from_range.count(0)
count_11 = list_from_range.count(11)
print(count_0)
print(count_11)
list_from_range.sort()
print(list_from_range)
list_copy = list_from_range.copy()
list_copy.pop()
print(list_copy)
print(list_from_range)
print(list_copy)
