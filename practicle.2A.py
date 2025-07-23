Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=10
>>> c=15
>>> if a<b & a<c:
...     print("a is smllest")
... elif b<a & b<c:
...     print("b is smallest")
... else:
...     print("c is smallest")
... 
...     
c is smallest
>>> for i in range(1,,11):
...     
SyntaxError: invalid syntax
>>> print(2*i)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(2*i)
NameError: name 'i' is not defined
>>> fori in range(1,11):
...     
SyntaxError: invalid syntax
>>> for i in range(1,11):
...     print(2*i)
