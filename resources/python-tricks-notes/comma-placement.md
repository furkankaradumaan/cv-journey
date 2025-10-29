# Comma Placement In Lists

## Code Style For Iterables

When you define a list, set, dictionary or another iterable,
most of the time it is a good idea to spread the list into multiple lines.

```python
names = ['Furkan', 'Betül', 'Yasir', 'Talha']
```
When you add or remove items in this list, it may be hard what was modified by looking at
a git diff.

```python
names = [
    'Furkan',
    'Betül',
    'Talha',
    'Yasir'       
]
```

This code style is more good looking and you can recognize modified items by looking a git diff easily.

## Comma Placement After Last Item Of The List

Have you ever got an error message because of that you added a new item
at the end of a list but you forgot to add comma after last item??

```python
names = [
    'Furkan',
    'Betül',
    'Yasir',
    'Talha'
]
```

```python
names = [
    'Furkan',
    'Betül',
    'Yasir',
    'Talha' # No comma in here.
    'Gürkan'
]
```

If our list consists of strings, python will not raise an error and implement this
list as the following:
```python
names = [
    'Furkan',
    'Betül',
    'Yasir',
    'TalhaGürkan' # Python contantenate the two strings
]
```

Thanks to the Python's string literal concatenation feautre,
the two strings will be merged.

* To not forget the comma we can write a list that has a comma after its last element
```python
names = [
    'Furkan',
    'Betül',
    'Talha',
    'Yasir',
]
```

As you can see, this is perfectly valid in Python.
This code habit may prevent to forget the comma when adding new elements in lists, sets or dictionaries in Python.
