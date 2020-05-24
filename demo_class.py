"""This is a demo of class"""
import sys
import traceback


class Demo:
    """This is a class"""
    def __init__(self, name, age):
        """init func"""
        if isinstance(name, str) and isinstance(age, int):
            self._name = name
            self._age = age
        else:
            raise TypeError("初始化参数类型错误")

    @property
    def name(self):
        """name property"""
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name 必须为字符型")

    @name.deleter
    def name(self):
        del self._name

    @property
    def age(self):
        """age property"""
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError("age 必须为整型")
        if age < 1 or age > 100:
            raise ValueError("age 必须在1到100之内")
        self._age = age

    @age.deleter
    def age(self):
        del self._age

    def say(self):
        """say something"""
        print("I'm {0} and I'm {1} years old".format(self._name, self._age))


class Product(Demo):
    """this is product class"""
    def __init__(self, name, age, wight):
        super().__init__(name, age)
        self._wight = wight

    @property
    def wight(self):
        """attribute wight"""
        return self._wight

    @wight.setter
    def wight(self, wight):
        self._wight = wight

    @wight.deleter
    def wight(self):
        del self._wight

    def say_wight(self, wight_basic):
        """this"""
        wight_new = self._wight - wight_basic
        print("I have {} wight".format(wight_new))


def single_demo():
    """单独一个类的方法演示，增加了error的try方法"""
    demo = Demo("demo", 12)
    demo.say()
    try:
        demo.age = 101
    except ValueError as exception:
        exc_type, exc_value, exc_obj = sys.exc_info()
        print(exc_type)
        print(exc_value)
        print(exc_obj)
        print(exception.with_traceback)
        print("----------------------")
        traceback.print_exc(3, file=sys.stdout)
        print("----------------------")
    demo.say()
    try:
        demo2 = Demo(124, "little")
        demo2.say()
    except TypeError as err_init:
        print(err_init)


def product_demo():
    """演示子类的使用"""
    product = Product("big", 22, 120)
    print(product.name)
    product.say_wight(2)
    product.say()


def test_add():
    """test demo"""
    assert False


if __name__ == "__main__":
    single_demo()
    # product_demo()
