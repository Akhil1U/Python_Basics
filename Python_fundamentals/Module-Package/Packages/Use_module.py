import Module1


message = Module1.greet("Alice")
print(message)

obj = Module1.MyClass(10)
print(obj.get_value())



### for sub packages you can import as below syntax


# my_package/
#     __init__.py
#     module_a.py
#     module_b.py
#     sub_package/
#         __init__.py
#         module_c.py
# 


# #######imports

# from my_package import module_a
# from my_package.sub_package import module_c
