'''this is a demo of sequence '''
list_numbers = [x for x in range(3)]
# s*n
list_add = list_numbers * 2
print(list_add)

# x in s
print(2 in list_numbers)
print(3 in list_numbers)

# x not in s
print("a" not in list_numbers)
list_strs = ["a", "b", "c"]

# s+s
list_add = list_strs + list_numbers
print(list_add)

# s[i]
print(list_add[2])

# s[i:j]
print(list_add[1:3])

# s[i:j:k]
print(list_add[0:5:2])

# min(s) and max(s)
print(min(list_numbers))
print(max(list_numbers))
print(min(list_strs))
print(max(list_strs))

# s.index(x[, i[, j]]) if x not in s,raise error
print(list_numbers.index(2))
print(list_add.index(2, 3))
try:
    print(list_numbers.index(10))
except ValueError as e:
    print(e)

# s.count(x)
print(list_numbers.count(3))
print(list_numbers.count(2))
