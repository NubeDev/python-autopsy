# Exceptions & Files

## Exceptions

\You have already seen __exceptions__ in previous code, They occur when something goes wrong, due to incorrect code or input.
When an exception occurs, the program immediately stops. The following code produces the ZeroDivisionError exception by trying to divide 42 by 0.
```python
num1 = 42
num2 = 0
print(num1 / num2)
```
Result:
```
ZeroDivisionError: integer division or modulo by zero
```
Different exception are raised for different reasons.

Common exceptions:
 * ImportError: an import fails
 * IndexError: a list is indexed with an out-of-range number
 * NameError: an unknown variable is used
 * SyntaxError: the code can't be parsed properly
 * TypeError: a function is called on a value of an inappropriate type
 * ValueError: a function is called on a value of the correct type, but with an inappropriate value

Python has several other built-in exceptions, such as ZeroDivisionError and OSError. Third-party libraries also often define their own exceptions.

## Exception Handling

To handle exceptions, and to call code when an exception occurs, you can use a `try/except`statement.

The `try` block contains code that might throw an exception. If that exception occurs, the code in the `try` block stops being executed, and the code in the `except` block is run.
If no error occurs, the code in `except` block doesn't run.

For example:
```python
try:
  num1 = 42
  num2 = 0
  print(num1 / num2)
  print("Done calculation")
except ZeroDivisionError:
  print("An error occurred")
  print("due to zero division")
```
Result:
```
An error occurred
due to zero division
```
In the code above, the except statement defines the type of exception to handle (in our case, the __ZeroDivisionError__).

A `try` statement can have multiple different `except` blocks to handle different exceptions. Multiple exceptions can also put into single `except` block using parentheses, to have the `except` block handle all of them.
```python
try:
  variable = 42
  print(variable + "hello")
  print(variable / 2)
except ZeroDivisionError:
  print("Divided by zero")
except(ValueError, TypeError):
  print("Error occurred")
```
Result:
```
Error occurred
```
An `except` statement without any exception specified will catch all errors. These should be used sparingly, as they can catch unexpected errors and hide programming mistake.
For example:
```python
try:
  word = "spam"
  print(word / 0)
except:
  print("An error occurred")
```
Result:
```
An error occurred
```
Exception handling is particularly useful when dealing with user input.

## `finally`

To ensure some code runs no matter what errors occur, you can use a `finally` statement.
The `finally` statement is placed at the bottom of a `try/except` statement. Code within a `finally` statement always runs after execution of the code in the `try`, and possibly in the `except` blocks.
```python
try:
  print("Hello")
  print(1 / 0)
except ZeroDivisionError:
  print("Divided by zero")
finally:
  print("This code will run no matter what")
```
Result:
```
Hello
Divided by zero
This code will run no matter what
```
Code in a `finally` statement even runs if an uncaught exception occurs in one of the preceding blocks.
```python
try:
  print(1)
  print(10 / 0)
except ZeroDivisionError:
  print(unknown_var)
finally:
  print("This is executed last")
```
Result:
```
1
This is executed last
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
NameError: name 'unknown_var' is not defined
```

## Raising Exceptions

You can raise exception by using the `raise` statement.
```python
print(1)
raise ValueError
print(2)
```
Result:
```  
1
ValueError
```
You need to specify the __type__ of the exception raised.
Exceptions can be raised with arguments that give detail about them.

For example:
```python
name = "123"
raise NameError("Invalid name!")
```
Result:
```
NameError: Invalid name!
```

In `except` blocks, the `raise` statement can be used without arguments to re-raise whatever exception occurred.
```python
try:
  num = 5 / 0
except:
  print("An error occurred")
  raise
```
Result:
```
An error occurred
ZeroDivisionError: integer division or modulo by zero
```

## Assertions

An __assertion__ is a sanity-check that you can turn on or off when you have finished testing the program.
An expression is tested, and if the result comes up false, an exception is raised.
Assertions are carried out through use if the `assert` statement.
```python
print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)
```
Result:
```
1
2
AssertionError
```
Programmers often place assertions at the start of a function to check for valid input, and after a function call to check for valid output.

The `assert` can take a second argument that is passed to the AssertionError raised if the assertion fails.
```python
temp = -10
assert (temp >= 0), "Colder than absolute zero!"
```
Result:
```
AssertionError: Colder than absolute zero!
```
AssertionError exceptions can be caught and handled like any other exception using the `try/except` statement, but if not handled, this type of exception will terminate the program.

## Opening Files

You can use Python to read and write the contents of __files__. Text files are the easiest to manipulate. Before a file can be edited, it must be opened, using the `open` function.
```python
myfile = open("filename.txt")
```
The argument of the `open` function is the __path__ to the file. If The file is in the same directory as the program, you can specify only its name.

You can specify the __mode__ used to open a file by applying a second argument to the `open` function.
Sending "r" means open in read mode, which is default.
Sending "w" means write mode, for rewriting the content of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in __binary__ mode, which is used for non-text files (such as images and sound files).

For example:
```python
# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary mode
open("filename.txt", "wb")
```
Once a file has been opened and used, you should close it.
This is done with the `close` method of the file object.
```python
file = open("filename.txt", "w")
# do stuff to the file
file.close()
```
We will read/write content to files in the upcoming lessons.

## Reading Files
The contents of a file that has been opens in text mode can be read using the `read` method.
```python
file = open("filename.txt", "r")
content = file.read()
print(content)
file.close()
```
This will print all of the content of the file "filename.txt".

To rad only a certain amount of a file, you can provide a number as an argument to the `read` method. This determines the number of __bytes that__ should be read.

You can make more calls to `read` on the same file object to read more of the file byte by byte. With no argument, `read` returns the rest of the file.
```python
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()
```

After all contents in a file have been read, any attempts to read further from that file will return an empty string, because you are trying to read from the end of the file.
```python
file = open("filename.txt")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()
```
Result:
```
Re-reading

Finished
```
To retrieve each line in a file, you can use the `readlines` method to return a list in which each element is a line in a file.
```python
file = open("filename.txt", "r")
print(file.readlines())
file.close()
```
Result:
```
['Line 1 \n', 'Line 2 \n', 'Line 3']
```
You can also use a `for` loop to iterate through the lines in the file:
```python
file = open("filename.txt", "r")
for line in file:
  print(line)

file.close()
```
Result:
```
Line 1

Line 2

Line 3
```
Notice in the output, the lines are separated by blank lines, as the `print` function automatically adds a new line at the end of its output.

## Writing files

To write files you use the `write` method, which writes a string to the file.

For example:
```python
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()
```
Result:
```
This has been written to a file
```
The "w" mode will create a file, if it does not already exist.

When a file is opened in write mode, the file's existing content is deleted.
```python
file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt","w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()
```
Result:
```
Reading initial contents
some initial text
Finished
Reading new contents
Some new text
Finished
```
As you can see, the content of the file has been overwritten.

The `write` method returns the number of __bytes__ written to a file, if successful.
```python
msg = "Hello world"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
```
Result:
```
12
```

## Working with Files

It is good practice to avoid wasting resources by making sure that files are always closed after they have been used. One way of doing this is to use `try` and `finally`.
```python
try:
  f = open("filename.txt")
  print(f.read())
finally:
  f.close()
```
This ensures that the file is always closed, even if an error occurs within it.
