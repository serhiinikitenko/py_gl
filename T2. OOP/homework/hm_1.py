"""
ДЗ 1:
Нужно написать класс который будет создавать объект этого же класса если в конструкторе будет присутствовать
 str ""А"" или ""В"" но не что либо другое.
Если в конструктор передается ""С"" и  ""В"" или передается ""С"" то должен быть создан простой базовый обьект (object).

Пример выполнения:
mc1 = MyClass(""A"")   --> MyClass obj
mc2 = MyClass(""A"",""B"")        --> MyClass obj
not_mc1 = MyClass(""C"")     --> object
not_mc2 = MyClass(""B"",""C"")     --> object
"""
import unittest


class MyClass(object):
    def __new__(cls, *args, **kwargs):
        return {
            ('A',): super().__new__(cls),
            ('B',): super().__new__(cls),
            ('A', 'B'): super().__new__(cls),
            ('C',): super().__new__(object),
            ('B', 'C'): super().__new__(object),
        }.get(args)

    def __init__(self, s1=None, s2=None):
        pass


class TestMyClass(unittest.TestCase):

    def test_A(self):
        self.assertIsInstance(MyClass("A"), MyClass)  # --> MyClass obj

    def test_B(self):
        self.assertIsInstance(MyClass("B"), MyClass)  # --> MyClass obj

    def test_AB(self):
        self.assertIsInstance(MyClass("A", "B"), MyClass)  # --> MyClass obj

    def test_C(self):
        self.assertIsInstance(MyClass("C"), object)  # --> object obj

    def test_BC(self):
        self.assertIsInstance(MyClass("B", "C"), object)  # --> object obj

    def test_wrong_arg(self):
        self.assertIsNone(MyClass("W"))


if __name__ == '__main__':
    unittest.main()
