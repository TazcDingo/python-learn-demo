'''this is a demo of string'''
import sys
import string


class DemoStr:
    '''这是一个Demo Str类'''
    @staticmethod
    def learn_method():
        '''this is a method'''
        # 构造函数有两种，直接字面化常量赋值和str()构造
        # str.capitalize() string 首字母大写,其余全小写
        example = "exAmple iS Example"
        example_cap = example.capitalize()
        print(example_cap)

        # str.casefold() 全小写
        big_dog = "Big DOg"
        big_dog_case = big_dog.casefold()
        print(big_dog_case)
        # str.center(width[, fillchar])，将字符串居中，并用fillchar填充左右
        abba = "abba"
        abba_center = abba.center(10, "-")
        print(abba_center)

        # str.count(sub[, start[, end]])计算sub的个数
        many_str = "abbacddc2abbacddc"
        count_abba = many_str.count("abba")
        count_abba_start = many_str.count("abba", 3)
        count_def = many_str.count("def")
        print(count_abba)
        print(count_abba_start)
        print(count_def)

        # str.endswith(suffix[, start[, end]])
        http_str = "http://www.google.com"
        print(http_str.endswith("com"))
        print(http_str.endswith("abc"))
        print(http_str.endswith(":", 1, 5))

        dict_example = {'name': 'xiao', 'age': 8}
        print(dict_example.get('name'))
        print(sys.path)
        print(sys.argv)
        print(dir(string))

    def foo_method_bd(self):
        '''foo'''


if __name__ == "__main__":
    DemoStr.learn_method()
