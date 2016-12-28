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





































# ##############
# ##############
# ##############
