# Python Assertion Statements

## Quick Explanation

* Python asseert statements is a mechanism used for debugging our Python programs.
* We use assert statements to detect bugs in our programs.

## Examples

```python
def apply_discount(amount, discount):
    price = int(amount * (1.0 - discount))
    assert 0 <= price <= amount
    return price
```

In here the assert statement will guarantee that the calculated price is between
0 and actual amount.

* If the condition in assert statement will become True, then we will know that there is
  a bug in the program about this. Because it is impossible to happen in normal circumstances.

## Assert Statement Structure

The assert statement is formally looks like this:

assert-stmt::="assert" expression1 [", " expression2]

* We have an assert keyword.
* An expression must be appear after the assert keyword, it is generally a condition.
* We can give an optional expressio2, which is the error message that will be showed if expression1 become True.

## How Assert Statement Works

Actually we can say that the following statement is  the same as assert statements:

```python
if __debug__:
    if not expression1:
        raise AssertionError(expression2)
```

* __debug__ is a built-in boolean flag, it is generally True but may False in some conditions.
* If you run your program with optimization flags __debug__ would be probably False and
  your assertion statements will be ignored as you can see in the code.

## When To Use Assertions

* If a condition can be False and that means there is an error in the program, use an assertion.
* Don't forget that whenever you receive an AssertionError, it should mean that there is a
  bug in your program. If it is the case, use assert statement.

```python
def calculate_rectangle_area(side1, side2):
    area = side1 * side2
    assert area > 0, "Area must be greater than 0"
    return area
```

We used assert statement to guarentee that the value of area is greater than 0.
It is obvious that if the area is equal to or less than 0, there should be a bug somewhere, right?

## When Not To Use Assertions

* Since assertions can be ommited when __debug__ flag is False, you should not use assert
  statements to validation. It can cause serious problems and security holes.

```python
class Person:
    def __init__(self, name, age):
        self._validata_name(name)
        self._validate_age(age)
        
        self.name = name.strip()
        self.age = age
    
    def _validate_name(self, name):
        assert isinstance(name, str), "Name must be a string value"
        assert name is None, "Name cannot be None"
        assert len(name.strip()) > 0, "Name must contain at least one letter"
    
    def _validate_age(self, age):
        assert isinstance(age, int), "Name must be an integer value"
        assert age >= 0, "Age cannot be negative"
```

Now think that we run our program with flag -O (so __debug__ flag is False).
In this case no assertion statements will be executed. So, daa validation will not be done
and our Person objects may have age attribute with value -10 for example.

## Summary Keys

* Put your assertion statements if it means a bug that a condition is False.
* When your program completed, no assert expressions should evaluate False, NEVER.
* If an assertion is False, it means there is bug, go nd fix it.
* Do not use assert statements to validation, use if statements and raise a proper exception
  for that.
* Asserts can be disabled if __debug__ is False, this shouldn't be a problem for you. If it would be
  a problem for you, then probably you put an assertion where you shouldn't did.
