import pytest


class Testobj():
    def test02(self):
        print("第二条测试用例")

def test01():
    print("第一条测试用例")

def test03():
    print("第三条测试用例")

if __name__ == "__main__":
    pytest.main(["-s", "-vv", "testcase.py"])
