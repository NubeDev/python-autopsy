# Functions & Modules

## Reusing Code

__Code reuse__ is a very important part of programming in any language. Increasing code size makes it harder to maintain.

For a large programming project to be successful, it is essential to abide by the __Don't Repeat Yourself__, or __DRY__, principle.
We've already looked at one way of doing this: by using loops. In this module, ewe will explore two more: functions and modules.

Bad, repetitive code is said to abide by the __WET__ principle, which stands for __Write Everything Twice__, or __We Enjoy Typing__.

## Functions

You've already used __functions__ in  previous lessons.
Any statement that consists of word followed by information in __parentheses__ is a function call.

Here are some examples that you've already seen:
```python
print("Hello world!")
range(2,20)
str(12)
range(10,20,3)
```
The words in front of the parentheses are function __names__, and the comma-separated values inside the parentheses are function __arguments__.

In addition to using pre-defined functions, you can create your own function by using the `def` statement.
Here is an example of a function named `my_func`. It takes no arguments, and prints "spam" three times. It is defined, and then called. The statements in the function are executed only when the function is called.
```python
def my_func():
  print("spam")
  print("spam")
  print("spam")

my_func()
```
Result:
```
spam
spam
spam
```
Notice that the code block within every function starts with a colon (`:`) and is __indented__.

You must define functions before they are called, in the same way that must assign variables before using them.
```python
hello()

def hello():
  print("Hello world")
```
Result:
```
>>> hello()
NameError: name 'hello' is not defined
>>>
```

## Function Arguments

All the functions definitions we've looked at so far have been functions of zero arguments, which are called with empty parentheses.
However, most functions take arguments. The example below defines a function that takes one argument:
```python
def print_with_exclamation(word):
  print(word + "!")

print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")
```
Result:
```
spam!
eggs!
python!
```
As you can see, the argument is defined inside the parentheses.

You can also define functions with more than one argument; separate them with commas.
```python
def print_sum_twice(x, y):
  print(x + y)
  print(x + y)

print_sum_twice(5, 8)
```
Result:
```
13
13
```
Function arguments can be used as variables inside the function definition. However, they cannot be referenced outside of the function's definition.
This also applies to other variables created inside a function.
```python
def function(variable):
  variable += 1
  print(variable)

function(7)
print(variable)
```
Result:
```
8
NameError: name 'variable' is not defined
```
Technically, __parameters__ are the variables in a function definition, and __arguments__ are the values put into parameters when functions are called.

## Returning From Function

Certain functions, such as `int` or `str`, return a value that can be used later.
To do this for your defined functions, you can use the `return` statement.

For example:
```python
def max(x, y):
  if x >= y:
    return x
  else:
    return y

print(max(4, 7))
z = max(8, 5)
print(z)
```
Result:
```
7
8
```
The `return` statement cannot be used outside of a function definition.

Once you return a value from a function, it immediately stops being executed. Any code after the `return` statement will never happen.
```python
def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")

print(add_numbers(4, 5))
```
Result:
```
9
```

## Comments & Docstrings

__Comments__ are annotations to code used to make it easier to understand. They don't affect how code is run.
In Python, a comment is created by inserting an __octothorpe__(aka pound sign or hash symbol: `#`). All text after it on that line is ignored by interpreter.

For example:
```python
x = 365
y = 7
# this is a comment

print(x % y) # find the remainder
# print(x // y)
# another comment
```
Result:
```
1
```
Python doesn't have general purpose multiline comments, as do programming languages such as C.

__Docstring__ (documentation string) serve a similar purpose to comment, as they are designed to explain code.
However, they are more specific and have a different syntax. They are created by putting a multiline string containing an explanation of the function below the __function's first line__.
```python
def shout(word):
  """
  Print a word with an
  exclamation mark following it.
  """
  print(word + "!")

shout("spam")
```
Result:
```
spam!
```
Unlike conventional comments, __docstrings__ are retained throughout the runtime of the program. This allows the programmer to inspect these comments at run time.

## Functions as Objects

Although functions are created differently from normal variables, __functions__ are just like any other kind of value.
They can be assigned and reassigned to variables, and later referenced by those names.
```python
def multiply(x, y):
  return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b))
```
Result:
```
28
```
The example above assigned the function `multiply` to a variable `operation`. Now, the name `operation` can also be used to call the function.

Functions can also be used as __arguments__ of other functions.
```python
def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))
```
Result:
```
30
```
As you can see, the function `do_twice` takes a function as its argument and calls it in its body.

## Modules

__Modules__ are pieces of the code that other people have written to fulfill common tasks, such as generating random numbers, performing mathematical operations, etc.

The basic way to use module is to add `import module_name` at the top of your code, and than using `module_name.var` to access functions and values with the name `var` in the module.
For example, the following code uses the `random` module to generate random numbers:
```python
import random

for i in range(5):
  value = random.randint(1, 6)
  print(value)
```
Possible result:
```
2
5
3
4
2
```   
The code above uses the `randint` function defined in the `random` module to print 5 random numbers in the range 1 to 6.

There is another kind of `import` that can be used if you only need certain functions/variables from a module.
These take the form `from module_name import var`, and then `var` can be used as if it were defined normally in your code.
For example. to import only the `pi` constant from the `math` module:
```python
from math import pi

print(pi)
```
Result:
```
3.14159265359
```
Use comma separated list to import multiple objects. For example:
```python
from math import pi, sqrt
```
`*` imports all objects from a module. For example: `from math import *`. This is generally discouraged, as it confuses variables in your code with variables in the external module.

Trying to import a module that isn't available causes an ImportError.
```python
import some_module
```
Result:
```
ImportError: No module named some_module
```
You can import module or object under a different name using the `as` keyword. This mainly used when a module or object has a long or confusing name.

For example:
```python
from math import sqrt as square_root

print(square_root(100))
```
Result:
```
10.0
```

## The Standard Library

There are three main types of modules in Python, those you write yourself, those you install from external sources, and those that are preinstalled with Python.
The last type is called __standard library__, and contains many useful modules.
Some of the standard library's useful modules include __string__, __re__, __datetime__, __math__, __random__, __os__, __multiprocessing__, __subprocess__, __socket__, __email__, __json__, __doctest__, __unittest__, __pdb__, __argparse__, and __sys__.
Tasks that can be done by the standard library include string parsing, data serialization, testing, debugging and manipulation dates, emails, command arguments, and much more!
Python's extensive standard library is one of its main strengths as a language.

Some of the modules in the standard library are written in Python, and some are written in C. Most are available on all platforms, but some are Windows or Unix specific.

We won't cover all of the modules in the standard library: there are simply too many. The complete documentation for standard library is available online at __www.python.org__.

### *pip*

Many third-party Python modules are stored on __Python Package Index__(__PyPI__). The best way to install these is using a program called `pip`.
This comes installed by default with modern distributions of Python, If you don't have it, ask google, or duckduckgo, or some other preferred search engine.
Once you have it, installing libraries from __PyPI__ is easy. Look up the name of library you want to install, go to the command line, and enter `pip install library_name`.
Once you done this, import the library and use it in your code.

Using `pip` is the standard way of installing libraries on most operating systems, but some libraries have prebuilt binaries for Windows. These are normal executable files that let install libraries with a GUI the same way you would install other programs.

It's important to enter `pip` commands at command line, not the Python interpreter.
