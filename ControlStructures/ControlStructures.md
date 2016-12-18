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
## Boolean Algebra & De Morgan Law

In mathematics and mathematical logic, Boolean algebra is the branch of algebra in which the values of the variables are the truth values true and false, or 1 and 0 respectively.
The main operations of Boolean algebra are the *conjunction* `and` denoted as `∧`, the *disjunction* `or` denoted as `∨`, and the *negation* `not` denoted as `¬`.
Boolean algebra was introduced by George Boole in his first book The Mathematical Analysis of Logic (1847).

In Boolean algebra 0 and 1 do not behave like integers 0 and 1, for which `1 + 1 = 2`. Boolean algebra may be identified as *integer arithmetic modulo 2*, for which `1 + 1 = 0`.
Addition and multiplication then play the Boolean roles of `XOR` (exclusive-or) and `AND` (conjunction) respectively, with disjunction `x ∨ y` (inclusive-or) definable as `x + y + xy`.

### *Basic operations*

The basic operations of Boolean calculus are as follows.
 * AND (conjunction), `x ∧ y` (`x AND y`), satisfies `x ∧ y = 1` if `x = y = 1` and `x ∧ y = 0` otherwise.
 * OR (disjunction), `x ∨ y` (`x OR y`), satisfies `x ∨ y = 0` if `x = y = 0` and `x ∨ y = 1` otherwise.
 * NOT (negation), `¬x` (`NOT x` or `!x`), satisfies `¬x = 0` if `x = 1` and `¬x = 1` if `x = 0`.

If the truth values 0 and 1 are interpreted as integers, these operations may be expressed with the ordinary operations of arithmetic, or by the minimum/maximum functions:
```
x ∧ y = x * y = min(x,y)
x ∨ y = x + y - (x * y) = max(x,y)
¬x = 1 - x
```
Alternatively the values of `x ∧ y`, `x ∨ y`, and `¬x` can be expressed by tabulating their values with truth tables as follows.

| __`x`__	| __`y`__	| __`x ∧ y`__ | __`x ∨ y`__	|
|:--------|:-------:|:-----------:|:-----------:|
| __`0`__ | __`0`__ |      0      |      0      |
| __`1`__ | __`0`__ |      0      |      1      |
| __`0`__ | __`1`__ |      0      |      1      |
| __`1`__ | __`1`__ |      1      |      1      |

| __`x`__ | __`¬x`__ |
|:--------|:--------:|
| __`0`__ |     1    |
| __`1`__ |     0    |

### *Lows*

A law of Boolean algebra is an identity such as `x ∨ (y ∨ z) = (x ∨ y) ∨ z` between two Boolean terms, where a Boolean term is defined as an expression built up from variables and the constants 0 and 1 using the operations `∧`, `∨`, and `¬`.

#### *Monotone laws*

Boolean algebra satisfies many of the same laws as ordinary algebra when one matches up `∨` with extended addition and `∧` with multiplication.

|Basic laws                     |                            |
|:------------------------------|:--------------------------:|
|Associativity of `∨`           | `x ∨ (y ∨ z) = (x ∨ y) ∨ z`|
|Associativity of `∧`           | `x ∧ (y ∧ z) = (x ∧ y) ∧ z`|
|Commutativity of `∨`           |       `x ∨ y = y ∨ x`      |
|Commutativity of `∧`           |       `x ∧ y = y ∧ x`|
|Distributivity of `∧` over `∨` | `x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z)`|
|Identity for `∨`               |       `x ∨ 0 = x`|
|Identity for `∧`               |       `x ∧ 1 = x`|
|Annihilator for `∧`            |       `x ∧ 0 = 0`|
|Idempotence of `∨`             |       `x ∨ x = x`|
|Idempotence of `∧`             |       `x ∧ x = x`|
|Absorption 1                   | `x ∧ (x ∨ y) = x`|
|Absorption 2                   | `x ∨ (x ∧ y) = x`|
|Distributivity of `∨` over `∧` | `x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z)`|
|Annihilator for `∨`            | `x ∨ 1 = 1`|

#### *Nonmonotone laws*

The complement operation is defined by the following two laws.

|Complementation | |
|:-----------------|:-----------:|
|Complementation 1 | `x ∧ ¬x = 0`|
|Complementation 2 | `x ∨ ¬x = 1`|

In both ordinary and Boolean algebra, negation works by exchanging pairs of elements, whence in both algebras it satisfies the double negation law (also called involution law).
 * Double negation | `¬(¬x) = x`

Boolean algebra also satisfies De Morgan's lows:

| De Morgan's lows| |
|:-----------|:-------------------:|
|De Morgan 1 |`¬x ∧ ¬y = ¬(x ∨ y)`|
|De Morgan 1 |`¬x ∨ ¬y = ¬(x ∧ y)`|

#### *Boolean searches*

Search engine queries also employ Boolean logic. For this application, each web page on the Internet may be considered to be an "element" of a "set".
The following examples use a syntax supported by Google.
 * Double quotes are used to combine whitespace-separated words into a single search term.
 * Whitespace is used to specify logical AND, as it is the default operator for joining search terms:
 ```
 "Search term 1" "Search term 2"
 ```
 * The OR keyword is used for logical OR:
 ```
 "Search term 1" OR "Search term 2"
 ```
 * A prefixed minus sign is used for logical NOT:
 ```
 "Search term 1" −"Search term 2"
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

|__`X and Z`__|__`True`__|__`False`__|
| :---------- |:--------:| :--------:|
|__`True`__   |   True   |   False   |
|__`False`__  |   False  |   False   |


### *Boolean `or`*
The `or` operator also takes two arguments.
It evaluates to `True` if either (or both) of its arguments are `True`, and `False` if both arguments are `False`.
```python
>>> 1 == 1 or 2 == 2
True
>>> 1 == 1 or 2 == 3
True
>>> 1 != 1 or 2 == 2
True
>>> 2 < 1 or 3 > 6
False
```
|__`X or Y`__|__`True`__|__`False`__|
| :--------- |:--------:| :--------:|
|__`True`__  |   True   |   True    |
|__`False`__ |   True   |   False   |


### *Boolean Not*
Unlike other operators we've seen so far, `not` only takes one argument, and inverts it.
The result of `not True` is `False`, and `not False` goes to `True`.
```python
>>> not 1 == 1
False
>>> not 1 > 7
True
```
You can chain multiple conditional statements in an `if` statement using the Boolean operators.

## Operator Precedence

__Operator Precedence__ is very important concept in programming. It is an extension of the mathematical idea or order of operations (multiplication is being preformed before addition, etc.),
to include other operators, such as those in Boolean logic.

The below code shows that `==` has higher precedence than `or`:
```python
>>> False == False or True
True
>>> False == (False or True)
False
>>> (False == False) or True
True
```
Python's order of operations is the same as that of normal mathematics: parentheses first, than exponentiation, then multiplication/division, and than addition/subtraction.

The following table lists all of  Python's operators, from highest precedence to lowest.

|Operator                    | Description|
|:---------------------------|:-----------|
| `**`                       |Exponentiation (raise to the power)|
| `~ + -`                    |Complement, unary plus and minus |
| `* / % //`                 |Multiply, divide, modulo and floor division|
| `+ -`                      |Addition and subtraction|
| `<< >>`                    |Right and left bitwise shift|
| `&`                        |Bitwise `AND`|
| `^ |`                      |Bitwise exclusive `OR` and regular `OR`|
| `<= < > >=`                |Comparison operators|
| `<> == !=`                 |Equality operators|
| `= %= /= //= -= += *= **=` |Assignment operators|
| `is  is not`               |Identity operators|
| `in  not in`               | Membership operators|
| `not or and`               | Logical operators|

## `while` Loop

An `if` statement is run once if its condition evaluates to `True`, and never if it evaluates to `False`.

A `while` statement is similar, except that it can be run more than once. The statements inside it are repeatedly executed, as long as the condition holds.
Once it evaluates to `False`, the next section of code is executed. Below is a `while` loop containing a variable that counts up from 1 to 5, at which point loop terminates.
```python
i = 1
while i <= 5:
  print(i)
  i = i + 1

print("Finished")
```
Result:
```
1
2
3
4
5
Finished
```
The code in the body of a `while` loop is executed repeatedly. This is called __iteration__.
The __infinite loop__ is a special kind of while loop; it never stops running. Its condition always remains `True`.

An example of an infinite loop:
```python
while 1 == 1:
  print("In the loop")
```
This program would indefinitely print *"In the loop"*.
You can stop the program's execution by using the `Ctrl+C` shortcut or by closing the IDE.

### *`break`*

To end a `while` loop prematurely, the `break` statement can be used.
When encountered inside loop, the `brake` statement causes the loop to finish immediately.
```python
i = 0
while 1 == 1:
  print(i)
  i += 1
  if i >=5:
    print("Breaking")
    break

print("Finished")
```
Result:
```
0
1
2
3
4
Breaking
Finished
```
Using the `break` statement outside of a loop causes an __error__.

### *`continue`*

Another statement that can be used within loops is `continue`.
Unlike `brake`, `continue` jumps back to the top of the loop, rather than stopping it.
```python
i = 0
while True:
  i += 1
  if i == 2:
    print("Skipping 2")
    continue
  if i == 5:
    print("Breaking")
    break
  print(i)

print("Finished")
```
Result:
```
1
Skipping 2
3
4
Breaking
Finished
```
Basically, the `continue` statement stops the current iteration and continues with the next one.
Using the `continue` statement outside of a loop causes an __error__.

## Lists

__Lists__ are another type of object in Python. They are used to store an indexed list of items.
A List is created using __squared brackets__ with __commas__ separating items.

The certain item in the list can be accessed by using its index in squared brackets.
```python
words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])
```
Result:
```
Hello
world
!
```
The first list item's index is `0`, rather than 1, as might be expected.

An empty list is created with an empty pair of square brackets.
```python
empty_list = []
print(empty_list)
```
Result:
```
[]
```
Most of the time, a comma won't follow the last item in a list. However, it is perfectly valid to place one there, and it is encountered in some cases.

Typically, a list will contain items of a single item type, but it is also possible to include several different types. List can also be nested within other lists.
```python
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])  
print(things[2])  
print(things[2][2])
```
Result:
```
0
[1, 2, 3]
3
```
List of lists are often used to represent 2D grids, as Python lacks the multidimensional arrays that would be used for this in other languages.

Indexing out of the bounds of possible list values causes an IndexError.
Some types, such as __strings__, can be indexed like lists. Indexing __strings__ behaves as though you are indexing a list containing each character in the string.

For other types, such as integers, indexing them isn't possible, and it causes a TypeError.
```python
string = "Hello world!"
print(string[6])
```
Result:
```
w
```

## List operators
The item at a certain index in a list can be reassigned.
For example:
```python
numbers = [42, 42, 42, 42, 42]
numbers[2] = 5
print(numbers)
```
Result:
```
[42, 42, 5, 42, 42]
```
Lists can be added and multiplied in the same way as strings.
```python
numbers = [1, 2, 3]
print(numbers + [4, 5, 6])
print(numbers * 3)
print(2 * numbers)
```
Result:
```
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 1, 2, 3, 1, 2, 3]
[1, 2, 3, 1, 2, 3]
```
Lists and strings are similar in many ways - strings can be thought of as list of characters that can't be changed.

To check if an item is in a list, the `in` operator can be used. It returns `True` if the item occurs one or more times in the list, and `False` if it doesn't.
```python
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)
```
Result:
```
True
True
False
```
The `in` operator is also used to determine weather or not a string is a substring of another string.

To check if an item is not in a list, you can use the `not` operator in one of the following ways:
```python
numbers = [1, 2, 3]
print(not 4 in numbers)
print(4 not in numbers)
print(not 3 in numbers)
print(3 not in numbers)
```
Result:
```
True
True
False
False
```

## List Functions

Another way of altering lists is using the __append__ method. This adds an item to the end of an existing list.
```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
```
Result:
```
[1, 2, 3, 4]
```
The __dot__ before append is there because it is method of the list class. Methods will be explained in a later lesson.

To get the number of items in a list, you can use the __len__ function.
```python
numbers = [1, 2, 3, 5, 8, 13]
print(len(numbers))
```
Result:
```
6
```
Unlike __append__, __len__ is a normal function rather than a method. This means it is written before the list it is being called on, without a dot.

The __insert__ method is similar to __append__, except that it allows you to insert a new item at any position in the list, as opposed to just at the end.
```python
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)
```
Result:
```
['Python', 'is', 'fun']
```
The index method finds the first occurrence of a list item and returns its index.
If the item isn't in the list, it raises a ValueError.
```python
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('z'))
```
Result:
```
2
0
ValueError: 'z' is not in list
```
There are few more useful functions and methods for lists.
* `max(list)`: Returns the list item with the maximum value
* `min(list)`: Returns the list item with the minimum value
* `list.count(obj)`: Returns a count of how many times an item occurs in a list
* `list.remove(obj)`: Removes first occurrence of an object from list
* `list.reverse()`: Reverses objects in a list

## Range
The __range__ function creates a sequential list of numbers.
The code below generates a list containing all of the integers, up to 10.
```python
numbers = list(range(10))
print(numbers)
```
Result:
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
The call to __list__ is necessary because __range__ by itselfe creates __range object__, ant this must be converted to a __list__ if you want to use it as one.

If __range__ is called with one argument, it produces an object with values from 0 to that argument.
If it is called with two arguments, it produces values from the first to the second.

For example:
```python
numbers = list(range(3, 8))
print(numbers)
print(range(20) == range(0, 20))
```
Result:
```
[3, 4, 5, 6, 7]]
True
```
__range__ can have third argument, which determines the interval of the sequence produced. This third argument must be an integer.
```python
numbers = list(range(5, 20, 2))
print(numbers)
```
Result:
```
[5, 7, 9, 11, 13, 15, 17, 19]
```

## `for` Loops

Sometimes, you need to perform code on each item in a list, This is called iteration, and it can be accomplished with a `while` loop and a counter variable.
```python
words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
  word = words[counter]
  print(word + !)
  counter += 1
```
Result:
```
hello!
world!
spam!
eggs!
```
The example above iterates through all items in the list, accesses them using their indices, and prints them with exclamation marks.

Iterating through a list using `while` loop requires quite a lot of code, so Python provides the `for` loop as a shortcut that accomplishes the same thing.
The same code from previous example can be written with a `for` loop, as follows:
```python
words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")
```
Result:
```
hello!
world!
spam!
eggs!
```
The `for` loop in Python is like the `foreach` loop in other languages.
This loop is commonly used to repeat some code a certain number of times. This is done by combining `for` loop with `range` objects.
```python
for i in range(5):
  print("hello!")
```
Result:
```
hello!
hello!
hello!
hello!
hello!
```
You don't need to call `list` on the `range` object when it is used in `for` look, because it isn't being indexed, so a list isn't required.

## Creating Calculator

This lesson is about an example Python project: a simple calculator.
Each part explains a different section of the program.
The first section is the overall menu. This keeps on accepting user input until the user enters *"quit"*, so a `while` loop is used.
```python
while True:
    print("Options.")
    print("Enter 'add' to add two numbers")
    print("Enter 'sub' to subtract two numbers")
    print("Enter 'mul' to multiply two numbers")
    print("Enter 'div' to divide two numbers")
    print("Enter 'quit' to end the program")

    user_input = raw_input(':')

    if user_input == "quit":
        break
    elif user_input == "add":
        ...
    elif user_input == "sub":
        ...
    elif user_input == "mul":
        ...
    elif user_input == "div":
        ...
    else:
        print("Unknown input")
```
The code above is the starting point for our program. It accepts user input, and compares it to the options in the `if`/`elif` statements.
The `break` statement is used to stop the `while` loop, in case the user inputs *"quit"*.

The next part of the program is getting the numbers the user wants to do something with.
The code below shows this fro the addition section of calculator. Similar code would have to be written for the other sections.
```python
elif user_input == "add":
    number1 = float(raw_input("Enter a number: "))
    number2 = float(raw_input("Enter another number: "))
```
Now, when the user inputs "add", the program prompts to enter two numbers, and stroes them in the corresponding variables.
As it is, This code crashes if the user enters a non-numeric input when prompted to enter a number. We will look at fixing problems like this in a later module.

The final part of the program processes user input and displays it. The code for addition part is shown here.
```python
elif user_input == "add":
    number1 = float(raw_input("Enter a number: "))
    number2 = float(raw_input("Enter another number: "))
    result = str(number1 + number2)
    print("The answer is " + result)
```
We now have a working program that prompts for user input, and then calculates and prints the sum of input.

Similar code would have to be written for the other branches (for subtraction, multiplication and division). The output could be put outside the `if` statement to omit repetition of code.
