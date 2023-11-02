#!/usr/bin/python3
import sys
sys.path.append('../')
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "hbtn", "Holberton")
print(mc.hbtn)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

class MyClass(int):
    pass

try:
    a = MyClass()
    add_attribute(a, "hbtn", "Holberton")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

