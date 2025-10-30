# Context Managers In Python

## Quick Start Explanation - What is A Context Manager in Python?

Context mangers are classes(or functions) that manages some resources in our programs.

The open function in Python's standard library is an example for context managers:
```python
with open("filename.txt", "w") as file:
    content = file.read()
```

Using context managers, we are able to manage the file resource successfully.

The file will be opened after the with ... as statement and the file object will be assigned
to variable file.
When the block ended, the file will be closed automatically.

By using this way, we can manage our resources in this way.

## How Do Context Managers Work In Python

Actually, there is no magic in Python's context managers. Here is the
work logic of context managers:

A class context manager must have implement __enter__ and __exit__ methods.
The __enter__ method is automatically called by Python interpreter in with statement.
After the with block ended the __exit__ method will be called.

## Implementing Custom Context Managers In Python

So, if we want to implement a custom context manager, we should implement an
__enter__ and an __exit__ method.

```python
class FileManager:
    """
    This class manages a file.
    """
    def __init__(self, filename, filemode='w'):
        self.file = open(filename, filemode)    
        return self.file        

    def __enter__():
        self.file = open(filename, filemode)
        return file
    
    def __exit__():
        if self.file:
            self.file.close() 
```

Now we can use this FileManager class to manage our files, so we will never forget
to close our files:
```python
with FileManager("file.txt", "r") as file:
    content = file.read()
```

* We created a FileManager object with FileManager("file.txt", "r").
* __enter__ method is called on FileManager object by Python interpreter and the
  return value is assigned to variable file (we don't have to assign the return value to a variable).
* We read the file content in with block.
* When the with block ended, the __exit__ method is called on the FileManager object.

## How To Use and When To Use Context Managers?

* If you need to do an operation before starting a job, and you
  need to do another related operation after finishing the job, then
  it may be a good idea to use context managers.

```python
import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self) -> int:
        self.end_time = time.time()
        print(f"Operation ended after {self.end_time - self.start_time: .2f} seconds")

with Timer():
    do_some_job()

```

## contextmanager decorator

* contextlib module in python gives us a quick way to create simple context managers.
* We can do the Timer context manager by using this module.

```python
from contextlib import contextmanager
import time

@contextmanager
def time():
    start_time = time.time()
    yield

    end_time = time.time()
    print("Operation ended after {end_time - start_time: .2f} seconds") 

with timer:
    do_dome_job()  
```

As you can see, we can write the same context manager by using
a generator function.

Here it how it works:
    * In the with statement, the timer function is called once. The function
      calculated the time and store it in `start_time` variable.
    * Then yield statement is executed and function pauses.
    * In with block we did some jobs.
    * At the end of the with block, the timer function is called again.
      It calculated the time, stored it in  `end_time`.
    * Then prints how many second lasted the operations.


