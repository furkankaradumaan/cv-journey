# Underscores In Python

## Single Undescore Before Identifier

* Using a single undescore when naming your variables or methods
  means that that variable or method is for internal use.

```python
class TestClass:
    def external_function():
        return 'external'
    
    def _internal_function():
        return 'internal'
```

* The single underscore before the method name indicates that
  this method shouldn't be accessed from outside the class.
  Although, it doesn't prevents to calling it.

```python
int main():
    test_class = TestClass()

    print(test_class.external_function()) # 'external'
    print(test_class._internal_function()) # 'internal'

if __name__ == '__main__':
    main()
```

* When importing a module with import keyword, python interpreter
  does not import internal functions or variables. (there are some exceptions.)

## Single Underscore After Identifier

* Conventionally, we use a single underscore after an identifier
  if the name want to use is already a Python keyword, another
  already taken identifier.

```python
set_ = {1, 2, 3, 4, 5}
list_ = list(set)

print(list_)
```

As we can see in the example, we used `set_` for our identifier because `set` is
a built-in Python function and we may want to use it later our program.

Also we used `list_` identifier for our list because `list` is a
built-in Python function.

## Double Underscore Before Identifier

* A double underscore is used to prevent name conflicts with subclasses.

Let me explain it:
```python
class TestClass:
    def __init__(self):
        self.regular_var = 10
        self._internal_var = 20
        self.__double_var = 30

test_obj = TestClass()
dir(test_obj)

# Output:
#[
#'_TestClass__double_var', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
#'__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#'__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
#'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_internal_var', 'regular_var'
#]
```

Did you see our variable `__double_var`?
Python interpreter converted it into `_Test_Class__double_var`. So we can not reach `__double_var` by
its this name:

```python
print(test_obj.__double_var) # NameError: __double_var is not defined
```
```python
print(test_obj._TestClass__double_var) # 30
```

* This is called name mangling. Python interpreter mangles
  the identifier.

So, what would you want such a thing, right?

Well, it is sometimes useful in cases such that you have
a class and a variable in that class (for example 'variable').
There is another class that inherits from this class and you want
to use an identifier 'variable' in this class also.

So,i if you do that, you cannot use 'variable' in the base class because it is overriden.
If you define your variables with two underscores at beginning, the variables names will be change
to this form: '_<class_name>__<variable>'. So, now tou can use both variables.

```python
class BaseClass:
    def __init__(self):
        self.__variable = 10 # This identifier mangled to -> '_BaseClass__variable'
    
class TestClass(BaseClass):
    def __init__(self):
        self.__variable = 20 # This identifier mangled to -> '_TestClass__variable'

def main():
    test_obj = TestClass()
    
    print(test_obj._BaseClass__variable) # 10
    print(test_obj._TestClass__variable) # 20
```
So, we can prevent name conflicts by using this technique.
This technique also can used with method names.

## Double Underscores Before and After Identifier

Probably you commonly see method names in this form, right?
For example, __init__, __repr__, __eq__,...

Actually this kind of Python identifiers is acutally reserved
for special use in the language.

So, conventionally you should not use them in your programs.

### What are these special methods?

Methods like __init__, __str__, __call__ are called 'dunder methods'
in Python community. They are used for special cases like initializing an object(__init__)
and so on.

## Single Underscore

You may see that sometimes we use just a single underscore for variable names.

```python
for _ in range(10):
    print("Life is beautiful")
```

In this code example, we are printing a string on the console 10 times.
We can use `_` as the variable name in here to indicate that that is just a useless variable.
You are not using that variable, just you want a loop and you must put an identifier.

* Single underscore also used in match case statements in Python to indicate the default case.

```python
match("Furkan"):
    case "Ali":
        print("You are Ali")
    case "Fatih":
        print("You are Fatih")
    case "Betül":
        print("You are Betül")
    case _:  # This is the default case
        print("I don't know you.")
```
