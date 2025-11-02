# WEEK01 - REPORT
**Date:** October 28 - November 3, 2025
**Status:** ✅ Completed

---

## Summary

**Completed:** 100%
**Projects:** 2 projects, QuoteScraper and Github Trending Scraper
**Blog Posts:** 0, no blog posts
**LinkedIn Posts:** 2 LinkedIn posts
![First post](https://www.linkedin.com/feed/update/urn:li:activity:7388479630585798656/)
![Second post](https://www.linkedin.com/feed/update/urn:li:activity:7390747126198214656/)

---

## ✅ Completed Tasks

### Learning Materials

**Videos**
 - ✅ ![Python for Data Science - Full Course (First 8 hours)](https://www.youtube.com/watch?v=LHBE6Q9XlzI&t=35216s)
  - What I've learned:
    * Python Basics
    * Data Structures in Python
    * Regex

 - ✅ ![Git & Github Crash Cource](https://www.youtube.com/watch?v=RGOj5yH7evk&t=2906s) 
  - What I've learned:
   * Version Control Systems
   * Initializing git repositories
   * Basic git commands (git add, git commit, git log)
   * git branching
   * Pushing local repositories to remote repositories(Github)

**Books**
 - ✅ Python Tricks by Dan Bader (Chapter 1-3)
  - What I've learned:
   * How to use assertions effectively
   * Python decorators
   * Best practice for writing list, dict, set literals

**Articles**
 - ✅ ![Real Python - Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
  - What I've learned:
   * Meaning of first-class-function
   * Why decorators are effective and powerful
   * How to write basic decorators
   * How to write decorators with parameters
   * Real world examples of decorators

 - ✅ ![Real Python - Introduction to Python Generators](https://realpython.com/introduction-to-python-generators/)
  - What I've learned:
   * What are generators
   * Why and when to use generators
   * Syntax of generators
   * Advanced uses of generators (.throw, .send, .close)

**Mathematics**
 - ✅ 3Blue1Brown - Essence of Linear Algebra (Video 1-3)
   ![Video 1](https://www.youtube.com/watch?v=fNk_zzaMoSs)
   ![Video 2](https://www.youtube.com/watch?v=k7RM-ot2NWY)
   ![Video 3](https://www.youtube.com/watch?v=kYB8IZa5AuE)
  - What I've learned:  
   * What are vectors
   * Vectors on coordinate system
   * Vector addition
   * Multiplication of a vector and scalar
   * Basis vectors
   * Matrices

### 💻 Projects

#### **Project 1: QuoteScraper**
- **Status:** ✅ Completed
- **GitHub Link:** ![QuoteScraper](https://github.com/furkankaradumaan/cv-journey/tree/main/week01/QuoteScraper)
- **Technologies:** Python, BeautifulSoup, Pandas, pytest, requests
- **Features:**
  - Abstract base classes with OOP design.
  - Logging system for debugging
  - Pandas analysis
- **The Hardest Part:** Writing test code for testing all units of the program.
- **What I'm most proud of:** Using abstract classes and giving one job for one class and good OOP design.

#### **Project 2: Github Trending Scraper**
- **Status:** ✅ Completed
- **GitHub Link:** ![Github Trending Scraper](https://github.com/furkankaradumaan/cv-journey/tree/main/week01/Github_Trendings_Scraper)
- **Technologies:** Python, BeautifulSoup, Pandas, pytest, requests
- **Feautes:**
  - Advanced dataclass qith runtime type validation
  - `slots=True` for memory optimization
  - `frozen=True` for immutability
  - Comprehensive test suite with mocking
  - Parameteized tests
- **The Hardest Part:**: Writing comprehensive test cases for all units
- **What I'm most proud of:** A professional dataclass implementatin with dynamic type cheking and input validation.

### 🌐 Blog & Social Media:

**LinkedIn:**
- ✅ Journey başlangıç postu (October 27)
  -Engagement: 0 likes, 0 comments

- ✅ Mid-week update (November 3)
  - Engagement: 0 likes, 0 comments

**GitHub:**
- ✅ Created profile ![README.md](https://github.com/furkankaradumaan)
- ✅ Created cv-journey repository
- ✅ Created README.md for each project
- ✅ Added code screenshots to README.md

## 💡 What I've Learned

### 🐍 Python Advanced Topics:

**1. Decorators:**

- **What I've learned**:

Functions are first class objects in python. This means that functions can
return other functions, functions can be passed to functions, functions can be stored
in variables, functions can be defined in other functions.

This features gives the programmer to create dynamic and creative programs.
Using these feature of Python, we can create functions dynamically in other functions,
then return them and store in a variable.

Decorators are functions that takes a function as parameter. Modifies that functions(this is not compulsory),
then returns the modified function. So we can create functions dynamically.

- ** Example Usage:**
```python
def log(func):
    '''
    Returns a modified function such that prints
    a log message before and after execution of the function.
    '''
    def wrapper(*args, **kwargs):
        print(f'Called {func.__name__}')
        func_result = func(*args, **kwargs)
        print(f'{func.__name__} returned {func_result}')
        return func_result
    
    return wrapper 
```

- **When to use decorators:**
  - If you create custom functions according to user input.
  - If you want to add additional features to more than one function.(We can use log decorator for all functions.)

- **Why it is important:**
  - Decorators are so powerful because when you write it one time, you can use it with multiple functions.
  - You can create custom functions by giving different parameters.

**2. Generators:**

- **What I've kearned:**
 
Generators are a powerful feature in Python. It's syntax is so similar to
regular functions, but we use `yield` keyword instead of `return`. When a generator
object is called, it will execute the statements until `yield`, then pause the function
there. Whem you call the function again, it will continue the line after that `yield`

- **Memory Advantage:**

The size of a generator is so small than a list, or set object
that keeps same number of items. Because list objects stores all the
information in memory in the same time. But generator objects produces
the next result on every call. So, they are extremely memory efficient.

- **yield vs return**

When a return statement is executed in a function, the function immediately
terminates. If we call the same function again, the statements will be executed
starting from same line.

If a yield statement is executed in a function, the function immediately
terminates. But if we call the function again, it will continue execution
after the last executed yield statement.

- **When to use generators:**
  - If you need to read a large file and you can't store all the content
    in memory.
  - If you don't want to access any item and you just want to access them in
    order

**3. Context Managers:**

  - **What I've learned:**

Context managers are good tools to manage resources.
They close resources for us automatically when our job is done.

- **with statement:**

When a with statement executed with an object,
the __enter__ method of the object is called. After the with
block executed, the __exit__ method is called on the object.
So, we open the resource and close it automatically when our job is done.

So, we can say that if we want to implement a custom context manager,
we need to implement __enter__ and __exit__ methods.

- **Type Hints Advanced:**

- **What I've learned:**

Type hints are powerful tools for type safety in Python. They are not
just some useless type specifications. We can specify the proper type
for a variable and we can dynamically access that and validate
the type of the object in that variable.

In this way, we can write type safe programs.

- **Runtime type checking:**

For example, if we implement a Person class in Python:
```python
class Person(self):
    def __init__(self, name: str, age: int):
        for var_name, var_val in self.__dict__.items():
            var_type = type(var_val)
            expected_type = type(self.__init__.__annotations__[var_name])
            if var_type != expected_type:   
                raise ValueError('Invalid type')
        
        self.name = name
        self.age = age
```

**5. Dataclasses Advanced:**

- **slots=True:**
When you specify slots=True, you specify the data of your class.
You specify the variable names that your dataclass will have.
Also it is more memory efficient because you cannot add additional
attributes to the objects of that class.

- **frozen=True:**
This makes your dataclass immutable. It is sometimes important
because, for example, if you want to store your objects in
a set, your object must be hashable. When you set frozen=True,
the __hash__ and __eq__ methods are automatically defined
for your class.

- **__post__init__**:
This function is executed after the execution of the __init__
function. It's purpose is validating the data of your class.
For example, you can do None checks for your data in this
function.

---
