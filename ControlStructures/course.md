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

Basic laws are:
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
 |:-----------------|:-----------:|
 |Complementation 1 | `x ∧ ¬x = 0`|
 |Complementation 2 | `x ∨ ¬x = 1`|

In both ordinary and Boolean algebra, negation works by exchanging pairs of elements, whence in both algebras it satisfies the double negation law (also called involution law).
 * Double negation | `¬(¬x) = x`

Boolean algebra also satisfies De Morgan's lows:
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
























































 |
