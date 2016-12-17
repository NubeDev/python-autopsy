# Control Structures

## Booleans & Comparison
Another type in Python is the Boolean type. There are two Boolean values: `True` and `False`.
They can be created by comparing values, for instance by using equal operator `==`.
```python
>>> my_boolean = True
>>> my_boolean
True
>>> 2 == 3
False
>>> "hello" == "Hello"
False
>>> "hello" == 'hello'
True
```
*Be careful not to confuse __assignment__ (one equals sign) with __comparison__ (two equals sign).*

### *Comparison*
Another comparison operator, the __not equla__ (`!=`), evaluates to `True` if the items being compared aren't equal, and `False` if they are.
```python
>>> 1 != 1
False
>>> 'six' != 'seven'
True
>>> 2 != 10
True
```
Python also has operators that determine whether one number (`float` or `integer`) is grater than or smaller than another.
These operators are `>` and `<` respectively.
```python
>>> 7 > 5
True
>>> 10 < 10
False
```
The greater than or equal to, and smaller than or equal to are `>=` and `<=`. They are the same as the strict greater than and smaller than operators, except that they return `True` when comparing equal number.
```python
>>> 7 <= 8
True
>>> 9 >= 9.0
True
```
Greater than and smaller than operators can also be used to compare strings __lexicographically__ (the alphabetical order of words is based on alphabetical order of their component letters).

## `if` Statements

You can use `if` statements to run code if certain condition holds. If an expression evaluates to `True`, some statements are carried out. Otherwise, they aren't carried out.
An `if` statements looks like this:
```python
if expression:
  statements
```
Python uses __indentation__ (white space at beginning of a line) to delimit block of code. Other languages, such as C, use curly braces to accomplish this, but in Python indentation is mandatory; programs won't work without it. As you can see, the statements in the `if` should be indented.

Here is an example `if` statement:
```python
if 10 > 5:
  print("10 greater than 5")
print("Program ended")
```
The expression determines whether 10 is greater than 5. Since it is, the indented statement runs, and `"10 greater than 5"` is output.
Than the unindented statement, which is not part of the `if` statement, is run, and `"Program ended"` is displayed.

Result:
```
10 greater than 5
Program ended
```
Notice the __colon__(`:`) at the end of the expression in the `if` statement.

To preform more complex checks, `if` statements can be nested, one inside the other.
This means that the inner `if` statement is the statement part of the outer one. This is one way to see whether multiple conditions are satisfied.
For example:
```python
num = 12
if num > 5:
  print("Bigger than 5")
  if num <= 42:
    print("Between 5 and 42")
```
Result:
```
Bigger than 5
Between 5 and 42
```

## `else` Statements
An `else` statement follows an `if` statement, and contains code that is called when the if statement evaluates to `False`.
As with `if` statements, the code inside the block should be indented.
```python
x = 4
if x == 5:
  print("Yes")
else:
  print("Go away!")
```
```
Go away!
```

## Boolean Logic
Boolean logic is used to make more complicated conditions for `if` statements that rely on more than one condition.
Python's Boolean operators are `and`, `or`, and `not`.
### *Boolean `and`*
The `and` operator takes two arguments and evaluate to `True` if, and only if, both of its arguments are `True`.
Otherwise, it evaluates to `False`.
```python
>>> 1 == 1 and 2 == 2
True
>>> 1 == 1 and 2 == 3
False
>>> 1 != 1 and 2 == 2
False
>>> 2 < 1 and 3 > 6
False
```
Python uses words for its Boolean operators, whereas most other languages use symbols as `&&`, `||` and `!`.

|__`cond_1 and cond_2`__|__`True`__|__`False`__|
| :-------------------- |:--------:| :--------:|
|__`True`__             |   True   |   False   |
|__`False`__            |   False  |   False   |


### *Boolean `or`*
The `or` operator also takes two arguments.























































................................................................................................
