# Basic Concepts

## What is Python?

Python is high-level language, its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.

Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles. It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.

Python is processed at runtime by the interpreter. There is no need to compile your program before executing it.

### *Bit of History*
Python was conceived in the late 1980s, and its implementation began in December 1989 by Guido van Rossum in the Netherlands.

> I chose Python as a working title for the project, being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus) - <cite>Guido van Rossum</cite>

### *Versions*
The three major versions of Python are 1.x, 2.x and 3.x. These are divided into minor version like 2.6, 2.7 or 3.3.
Code written for Python 3.x is guaranteed to work with all future versions.
Both 2.x and 3.x are in use currently. This course is for Python 2.7, but it isn't hard to change from one version to another.

## The Python Console
In this part we will start using Python via the Python console on Unix system.
Open terminal emulator and type `python`

You should get output something like:
```python
Python 2.7.12 (default, Nov 19 2016, 06:48:10)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

What you see on screen is the Python Console. The Python console is program that allows you to enter one line of Python code, repeatedly executes that line, and displays the output. This is known as a REPL - a read-eval-print-loop.

Type in `print('Hello world!')` and press enter. You should see the following:
```python
>>> print('Hello World!')
Hello World!
>>>
```

Now you can reenter same code by typing or by pressing `up` key or you can change it, like:
```python
>>> print('Hello World!')
Hello World!
>>> print('Hello World!')
Hello World!
>>> print('Weeeeee!')
```
When we finished with the Python console, you will want to close it. You can do this by typing `quit()` or `exit()` or just send end of file (EOF) control character. On Unix system this is done by pressing Ctrl+D.

## Simple Operations
Python has the capability of carrying out simple calculations. Enter calculation directly into console, and it will output result:
```python
>>> 2 + 2
4
>>> 2 - 3 + 4
3
```
*The spaces around the plus and minus signs are __optional__ (the code would work without them), but they make it easier to read.*

Python also carries out multiplication and division, using `*` and `/` respectively.
Use parentheses to determine which operations are preformed first:
```python
>>> 2 * (3 + 4)
14
>>> 12 / 6
2
```

The minus sign indicate a negative number. Operations are preformed on negative numbers, just as they are on positive ones.
```python
>>> 2 * (3 + 4)
14
>>> 12 / 6
2
```
*The plus signs can be also put in front of numbers, but this has no effect*

Dividing by zero in Python produces an **error**, as no answer can be calculated
```python
>>> 11 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
```

## Floats
Floats are used in Python to represent numbers that aren't integers. Some examples are `3.2`, `0.5` or `4.`.
To use floats in simple calculation at least one of operands must be float.
```python
>>> 3. / 4
0.75
>>> 1 + 1.0
2.0
```
## Other Numerical Operations

### *Exponentiation*
Besides addition, subtraction, multiplication and division, Python also supports exponentiation, which is the rising of one number to the power of another. This operation is preformed using two asterisks.
```python
>>> 2 ** 5
32
>>> 9 ** (1. / 2)
3.0
```
*Taking a square root of number is same as doing power of 1/2 of same number*

### *Quotient & Remainder*

To determent the quotient and remainder of division, use the floor division and modulo operators, respectively.
Floor division for integers is done by using operator `/` and for floats is done by using operator `//`.
The modulo operator is carried out with percent (`%`), this one can be used on integers and floats.
```python
>>> 20 / 6
3
>>> 20. / 6
3.3333333333333335
>>> 20. // 6
3.0
>>> 20 % 6
2
>>> 1.25 % 0.5
0.25
```
## Strings
If you want to use text in Python, you have to use strings. A `string` is created by entering text between two single or double quotation marks.

When console displays a string, it generally uses single quotes. The delimiter used for a string doesn't affect how it behaves in any way.
```python
>>> 'Python is fun'
'Python is fun'
>>> "Python is fun"
'Python is fun'
```

Some characters can't be directly included in a string. For instance, single quotes can't be directly included in a single quote string; this would cause it to end prematurely.

Characters like these must be escaped by placing a **backslash** before them. Other common characters that must be escaped are newlines and backslashes. Double quotes only need to be escaped in double quoted string, and same apply to single quote.
```python
>>> 'Monty Python\'s Life of Brian'
"Monty Python's Life of Brian"
```

`\n` represents a new line character. Backslashes can also be used to escape arbitrary Unicode characters and various other things that can't be reliably printed.

### *Newlines*
Python provides an easy way to avoid manually writing `\n` to escape newlines in a string. Create string using three sets of quotes.
```python
>>> """Life's a piece of shit
... When you look at it
... Life's a laugh and death's a joke, it's true.
... You'll see it's all a show
... Keep 'em laughing as you go
... Just remember that the last laugh is on you.
... """
"Life's a piece of shit\nWhen you look at it\nLife's a laugh and death's a joke, it's true.\nYou'll see it's all a show\nKeep 'em laughing as you go\nJust remember that the last laugh is on you.\n"
```   
## Simple Input & Output
Usually, program take input and process it to produce output. In Python, you can use the `print` function to produce output. This displays a textual representation of something to the screen.
```python
>>> print(1 + 1)
2
>>> print('Hello\nWorld!')
Hello
World!
>>>
```
*When string is printed, the quotes around it are not displayed.*

### *Input*
To get input from the user in Python, you can use `raw_input` function.
The function prompts the user for input, and returns what they enter as a string(with the contents automatically escaped).
```python
>>> raw_input("Enter something please:")
Enter something please:This is what\nthe user enters!
'This is what\\nthe user enters!'
```

## String Operations

### *Concatenation*
As with integers and floats, strings in Python can be added, using a process called **concatenation**, which can be done on any two strings.

When concatenating strings, it doesn't matter whether they've been created with single or double quotes.
```python
>>> 'Spam'+"eggs"
'Spameggs'
>>> print("First string" + "," + "second string")
First string,second string
```
Even if your strings contain numbers, they are still added as strings rather then integers. Adding a string to a number produces an error, as even though they might look similar, they are two different entities.
```python
>>> "2" + "2"
'22'
>>> 1 + '2' + 3 + '4'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Strings can also be multiplied by integers. this produces a repeated version of the original string.The order of the string and the integer doesn't matter, but the string usually comes first.

Strings can't be multiplied by other strings. Strings also can't be multiplied by floats, even if floats are whole numbers.
```python
>>> print('spam'  * 3)
spamspamspam
>>> 4 * "2"
'2222'
>>> '17' * '87'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> 'python is fun' * 7.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
```   
## Type Conversion

In Python, it's impossible to complete certain operation due to the types involved. For instance, you can't add two strings containing 2 and 3 together to produce the integer 5, as the operation will be preformed on strings, making the result '23'.

The solution to this is **type conversation**. In that example, you will use the `int` function.
```python
>>> "2" + "3"
'23'
>>> int("2") + int("3")
5
```  
To this point we have used types `integer`, `float` and `string`. The functions used to convert to these are `int`, `float` and `str`, respectively.

Another example of type conversation is turning user input (which is a string) to numbers (integers or floats), to allow for the performance of calculation.
```python
>>> float(raw_input("Enter a number:")) + float(raw_input("Enter another number:"))
Enter a number:40
Enter another number:5
45.0
```

## Variables
**Variables** play a very important role in most programming languages, and Python is no exception. A variable allows you to store a value by assigning it to name, which can be used to refer to the value later in the program.

To assign a variable, use **one equals sign**. Unlike most lines of code we've looked at so far, it doesn't produce any output at the Python console.
```python
>>> print(x)
7
>>> print(x + 3)
10
>>> print(x)
7
```
Variables can be reassign as many times as you want, in order to change their value. In Python, variables don't have specific types, so you can assign string to a variable, and later on assign an integer to the same variable.
```python
>>> x = 234.567
>>> print(x)
234.567
>>> x = "Some string"
>>> print(x + "!")
Some string!
```
### *Variable Names*
Certain restrictions apply in regard to the characters that may be used in Python variable names. The only characters that are allowed are letters, numbers, and underscores. Also, they can't start with numbers.
Not following these rules result in errors.
```python
>>> this_is_normal_name = 7
>>> 2pac = 42
  File "<stdin>", line 1
    2pac = 42
       ^
SyntaxError: invalid syntax
>>>
>>> U2 = "OK!"
>>>
>>> spaces are not allowed = 12
  File "<stdin>", line 1
    spaces are not allowed = 12
             ^
SyntaxError: invalid syntax
```
Python is case sensitive, so `caMel` and `camel` are two different variable names.

Trying to reference a variable you haven't assigned to will cause error. Deleted variables can be reassigned to later as normal.
```python
>>> eggs
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'eggs' is not defined
>>> del spam
>>> spam
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
```
You can take the value of the variable from the user input.
```python
>>> spam = raw_input("Number:")
Number:42
>>> print(spam)
42
```
## In-Place Operators
**In-Place operators** allow you to write code like `x = x + 3` more concisely, as `x += 3`. The same thing is possible with other operators such as `-`, `*`, `/` and `%` as well.
```python
>>> x = 2
>>> print(x)
2
>>> x += 40
>>> print(x)
42
```
These operators can be used on types other than numbers, as well, such as strings.
```python
>>> x = "spam"
>>> print(x)
spam
>>> x += "eggs"
>>> print(x)
spameggs
```
*Many other languages have special operators like `++` as shortcut for `x += 1`. Python __does not__ have these.*

## Using an Editor
 
































.
