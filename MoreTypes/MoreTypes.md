# More Types

## None

The `None` object is used to represent the absence of a value,
It is similar to __null__ in other programming languages. Like other "empty" values, such as 0, [] and the empty string, it is `False` when converted to a Boolean variable.
When entered at the Python console, it is displayed as the empty string.
```python
>>> None == None
True
>>> None
>>> print(None)
None
>>>
```
The `None` object is returned by any function that doesn't explicitly return anything else.
```python
def some_func():
  print("Hi")

var = some_func()
print(var)
```
Result:
```
Hi
None
```

## Dictionaries

__Dictionaries__ are data structures used to map arbitrary keys to values.
List can be thought of as dictionaries with integer keys within certain range.
Dictionaries can be indexed in the same way as lists, using __square brackets__ containing keys.

Example:
```python
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
```
Result:
```
24
42
```
Each element in a dictionary is represented by a __key:value__ pair.

Trying to index a key that isn't part of the dictionary returns a `KeyError`.

Example:
```python
primary = {
  "red": [255, 0, 0],
  "green": [0, 255, 0],
  "blue": [0, 0, 255],
}

print(primary["red"])
print(primary["yellow"])
```
Result:
```
[255, 0, 0]

KeyError: 'yellow'
```
As you can see, a dictionary can store any types of data as values.
An empty dictionary is defined as `{}`.

Only __immutable__ objects can be used as keys to dictionaries. __Immutable__ objects are those that can't be changed. So far, only mutable objects you've come across are `lists` and `dictionaries`.
Trying to use a mutable objects as a dictionary key causes a `TypeError`.
```python
bad_dict = {
  [1, 2, 3]: "one two three",
}
```
Result:
```
TypeError: unhashable type: 'list'
```
## Dictionary Functions

Just like lists, dictionary keys can be assigned to different values. However, unlike lists, a new dictionary key can also be assigned a value, not just ones that already exist.
```python
squares = {1:1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)
```
Result:
```
{8: 64, 1: 1, 2: 4, 3: 9, 4: 16}
```

To determine whether a key is in a dictionary, you can use `in` and `not in`, just as you can for a list.

Example:
```python
nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)
```
Result:
```
True
False
True
```

A useful dictionary method is `get`. It does the same thing as indexing, but if the key is not found in the dictionary it returns another specified value instead(`None`, by default).

Example:
```python
pairs = {
  1: "apple",
  "orange": [2, 3, 4],
  True: False,
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))
```
Result:
```
[2, 3, 4]
None
not in dictionary
```

## Tuples
__Tuples__ are very similar to list, except that they are immutable (they cannot be changed).
Also, they are created using __parentheses__, rather than square brackets.

Example:
```python
words = ("spam", "eggs", "sausages",)
```

You can access the values in the tuple with their index, just as you did with lists:
```python
print(words[0])
```

Trying to reassign a value in a tuple causes a TypeError.
```python
words[1] = "cheese"
```
Result:
```
TypeError: 'tuple' object does not support item assignment
```
Like list and dictionaries, tuples can be nested within each other.

Tuples can be created without the parentheses, by just separating the values with commas.
```python
my_tuple = "one", "two", "three"
print(my_tuple[0])
```
Result:
```
one
```
An empty tuple is created using an empty parenthesis pair.
```python
tuple = ()
```
Tuples are faster then list, but they cannot be changed.

## List Slices

__List slices__ provide a more advanced way of retrieving values from a list.
Basic list slicing involves indexing a list with __two column separated integers__.
This returns a new values in the old list between the indices.

Example:
```python
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
```
Result:
```
[4, 9, 16, 25]
[9, 16, 25, 36, 49]
[0]
```
Like arguments to __range__, the first index provide in a slice is included in the result, but the second isn't.

If the first number in a slice is omitted, it is takes to be the start of the list.
If the second number is omitted, it is taken to be the end.

Example:
```python
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])
```
Result:
```
[0, 1, 4, 9, 16, 25, 36]
[49, 64, 81]
```
Slicing can also be don on tuples.

List slices can also have a third number, representing the step, to include only, alternate values in the slice.
```python
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])
```
Result:
```
[0, 4, 16, 36, 64]
[4, 25]
```
`[2:8:3]` will include elements starting from the 2nd index up to the 8th with step of 3.

__Negative__ values can be used in list slicing (end normal list indexing).
When negative values are used for the first and second values in a slice (or a normal index), they count from the end of the list.
```python
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])
```
Result:
```
[1, 4, 9, 16, 25, 36, 49, 64]
```
If negative value is used for the step, the slice is done backwards.
Using `[::-1]` as a slice is a common and idiomatic way to reverse a list.

## List Comprehensions

__List comprehensions__ are a useful way of quickly creating lists whose contents obey a simple rule.

For example, we can do the following:
```python
# a list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)
```
Result:
```
[0, 1, 8, 27, 64]
```
List comprehension are inspired by set-builder notation in mathematics.

A list comprehension can also contain an `if` statement to enforce a condition on values in the list.

Example:
```python
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)
```
Result:
```
[0, 4, 16, 36, 64]
```

Trying to create a list in a vary extensive range will result in a OverflowError.
This code shows an example where the list comprehension runs out of memory.
```python
even = [2*i for i in range(10**100)]
```
Result:
```
OverflowError: range() result has too many items
```
This issue is solver by __generators__, which are covered in next modules.

## String Formatting

So far, to combine strings and non-strings, you've converted the non-strings to string and added them.
String formatting provides a more powerful way to embed non-string within strings.
String formatting uses a __format__ method to substitute a number of arguments in the string.

Example:
```python
# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)  
```
Result:
```
Numbers: 4 5 6
```
Each argument of the format function is placed in the string at the corresponding position, which is determined using the curly braces `{}`.

String formatting can also be done with named arguments.
```python
a = "{x}, {y}".format(x = 5, y = 12)
print(a)
```
Result:
```
5, 12
```

## Useful Functions

### *String Functions*

Python contains many useful built-in functions and methods to accomplish common tasks.
* `join` - joins a list of strings with another string as a separator
* `replace` - replace one substring in a string with another.
* `startswith` and `endswith` - determine if there is a substring at the start and end of a string, respectively.
* `lower` and `upper` - change case of characters
* `split` - is opposite of `join`, turning string with a certain separator into a list.

Examples:
```python
print(",".join(["spam", "eggs", "ham"]))
print("Hello ME".replace("ME", "world"))
print("This is a sentence.".startswith("This"))
print("This is a sentence.".endswith("sentence."))
print("This is a sentence.".upper())
print("This is a sentence.".lower())
print("spam,eggs,ham".split(","))
```
Result:
```
spam,eggs,ham
Hello world
True
True
THIS IS A SENTENCE.
this is a sentence.
['spam', 'eggs', 'ham']
```

### *Numeric Function*

* `max` and `min` - To find maximum and minimum of some numbers or list.
* `abs` - distance of a numbers from zero (its absolute value).
* `round` - round a number to a certain number of decimal places.
* `sum` - total of a list

```python
print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))
```
Result:
```
0
9
99
42
15
```

### *List Functions*

Often used in conditional statements, `all` and `any` take a list as an argument, and return `True` if all or any(respectively) of their arguments evaluate to `True`(and `False` otherwise).
The function `enumerate` can be used to iterate through the values and indices of a list simultaneously.

Example:
```python
nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
  print("All larger than 5")

if any([i % 2 for i in nums]):
  print("At least one is even")
for v in enumerate(nums):
  print(v)
```
Result:
```
All larger than 5
At least one is even
(0, 55)
(1, 44)
(2, 33)
(3, 22)
(4, 11)
```
