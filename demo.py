'''this is a demo'''
fruits = ["orange", "banana", "apple"]
print(all(fruits))
somethings = ["a", ""]
print(all(somethings))
print(dir())
numbers = [1, 2, 3, 200, 6, 8, 10, 11]
print(max(numbers))
list_fruits = list(enumerate(fruits, 1))
print(list_fruits)


def is_gt5(number):
    '''is number big than five'''
    return number > 5


print(pow(2, 3))
numbers_gt5 = filter(is_gt5, numbers)
print(list(numbers_gt5))
print(pow(2, 10))


class MyClass:
    '''this is my class'''
    def __init__(self):
        self._my_name = None

    @property
    def my_name(self):
        '''this is documentation'''
        return self._my_name

    @my_name.setter
    def my_name(self, value):
        self._my_name = value

    @my_name.deleter
    def my_name(self):
        del self._my_name

    def say_hello(self):
        '''say hello'''
        print(self._my_name + "say hello")


m = MyClass()
m.my_name = "linan"
print(m.my_name)
m.say_hello()
list_numbers = [2, 3, 4, 5, 7, 6, 9, 8, 1]
for number in list_numbers:
    print(number)
list_numbers.sort()
print(list_numbers)
list_numbers.append(10)
print(list_numbers)
