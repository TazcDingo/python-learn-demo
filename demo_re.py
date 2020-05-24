"""This is a demo of re"""
import re


class DemoRe:
    """this is DemoRe class"""
    def __init__(self):
        pass

    def match(self):
        """learn how to use match"""
        github_url = "https://github.com/TazcDingo/python-learn-demo"
        target = "https"
        m = re.match(target, github_url)
        print(m.string)
        print(m.expand)
        print(m.group(0))

    def search(self):
        """learn how to use search"""


if __name__ == "__main__":
    demo = DemoRe()
    demo.match()
