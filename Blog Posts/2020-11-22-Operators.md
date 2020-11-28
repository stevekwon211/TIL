---
title: Operators
author: Hyukil (Steve) Kwon
date: 2020-11-22 22:31:00 +0900
categories: [C]
tags: [c, Basic]
comments: true
---
# Operators in 'C'

An operator is a symbol that tell the compiler to perform a certain mathematical or logical manipulation on the operands<br>

|                   |       Operator        |                       Type                        |
| :---------------: | :-------------------: | :-----------------------------------------------: |
|  Unary operators  |        ++, --         | Increment and decrement operator (Unary operator) |
| Binary operators  |     +, -, *, /, %     |               Arithmetic operators                |
| Binary operators  | <, <=, >, >=, ==, !=  |               Relational operators                |
| Binary operators  |      &&, \|\|, !      |                 Logical Operators                 |
| Binary operators  |  &, \|, <<, >>, ~, ^  |                 Bitwise operators                 |
| Binary operators  | =, +=, -=, *=, /=, &= |               Assignment operators                |
| Ternary operators |          ?:           |               Conditional operators               |

  <br>

| Precedence |                           Operator                           |                         Description                          | Associativity |
| :--------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :-----------: |
|     1      |       ++ -- <br>()<br>[]<br>.<br/>-><br/>(type){list}        | Suffix/postfix increment and decrement<br/>Function call<br/>Array subscripting<br/>Structure and union member access<br/>Structure and union member access through pointer<br/>Compound literal | Left-to-right |
|     2      | ++ --<br/>+ -<br/>! ~<br/>(type)<br/>*<br/>&<br/>sizeof<br/>_Alignof | Prefix increment and decrement<br/>Unary plus and minus<br/>Logical NOT and bitwise NOT<br/>Type case<br/>Indirection (dereference)<br/>Address-of<br/>Size-of<br/>Alignment requirement | Right-to-left |
|     3      |                            * / %                             |           Multiplication, division, and remainder            | Left-to-right |
|     4      |                             + -                              |                   Addition and subtraction                   | Left-to-right |
|     5      |                            << >>                             |              Bitwise left shift and right shift              | Left-to-right |
|     6      |                        < <=<br/>> >=                         | For relational operators < and <= respectively<br/>For relational operators > and >= respectively | Left-to-right |
|     7      |                            == !=                             |             For relational = and != respectively             | Left-to-right |
|     8      |                              &                               |                         Bitwise AND                          | Left-to-right |
|     9      |                              ^                               |                  Bitwise XOR (exclusive or)                  | Left-to-right |
|     10     |                              \|                              |                  Bitwise OR (inclusive or)                   | Left-to-right |
|     11     |                              &&                              |                         Logical AND                          | Left-to-right |
|     12     |                             \|\|                             |                          Logical OR                          | Left-to-right |
|     13     |                              ?:                              |                     Ternary conditional                      | Right-to-left |
|     14     |      =<br/>+= -=<br/>*= /= %=<br/><<= >>=<br/>&= ^= \|=      | Simple assignment<br/>Assignment by sum and difference<br/>Assignment by product, quotient, and remainder<br/>Assignment by bitwise left shift and right shift<br/>Assignment by bitwise AND, XOR, and OR | Right-to-left |
|     15     |                              ,                               |                            Comma                             | Left-to-right |

  <br>

# Unary Operator in 'C'

++ is an unary operator and it can appear on either side of an expression

```c
uint32_t x,y;  
x=5;  
y=++x;
```

__=> Pre-incrementing__  
y = 6 , x = 6  
First, value of x will be incremented by 1  
Then value of x will be assigned to y   

```c
 uint32_t x,m;  
x=5;  
m=x++;   
```

__=> Post-incrementing__  
m = 5 , x = 6  
First, value of x will be assigned to m  
Then value of x will be incremented by 1  

```c
uint32_t x,y;
x=5;
y=--x;
```

 __=> Pre-decrementing__  
y = 4 , x = 4  

```c
uint32_t n,m;
n=5;
m=n--;
```

__=> Post-decrementing__  
m = 5 , n = 4

<br>

# Unary operators with pointer variables

```c
uint32_t *pAddress = (uint32_t*) 0xFFFF0000;  

pAddress = pAddress +1;
```

 __=> this is arithmetic add operation__  
Result: pAddress = 0xFFFF0004   

```c
pAddress++;
```

__=>This is unary increment operation__  
pAddress = 0xFFFF0004  

<br>

# Relational Operators in 'C'

- Relational operators do some kind of evaluation on the operands and then return value 1 (for true) or 0 (for false)
- Relational operators are binary operators because they require two operands to operate
- The relational operators are evaluated left to right

| ==<br>><br/><<br/>>=<br/><=<br/>!= | Equal to<br/>Greater than<br/>Less than<br/>Greater than or equal to<br/>Less than or equal to<br/>Not equal to | a==b returns 1 if a and b are the same<br/>a>b returns 1 if a is larger than b<br/>a<b returns 1 if a is smaller than b<br/>a>=b returns 1 if a is larger than or equal to b<br/>a<=b return 1 if a is smaller than or equal to b<br/>a!=b returns 1 if a and b not the same |
| ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                    |                                                              |                                                              |

<br>  

## True and False in 'C'

- In 'C' Zero is interpreted as __false__ and anything non-zero is interpreted as __true__.
- Expressions using relational operators evaluate to a value of either TRUE (1) or FALSE (0).
- Relational expressions are often used within __if__ and __while__ statements.

<br>

## Examples

```c
A=10, B=20

C = (A!=B);
```

__=> C=1__

<br>  

# Logical Operators in 'C'

- The logical operators perform logical-AND __(&&)__, logical-OR __(||)__ and logical -NOT __(!)__ operations.

- These are binary operators except NOT (!).  

| &&<br>\|\|<br/>! | And<br/>Or<br/>Not(unary) | a&&b returns 1 if a is nonzero and b is nonzero<br/>a\|\|b returns 1 if a is nonzero or b is nonzero<br/>!a returns 1 if a is zero |
| ---------------- | ------------------------- | ------------------------------------------------------------ |
|                  |                           |                                                              |

<br>  

## logical AND Operator : &&

- The __logical-AND__ operator produces the value 1 if both operands have nonzero values.
- if either operand is equal to 0, the result is 0. If the first operand of a logical-AND operation is equal to-, the second operand is not evaluated.

```c
A= -10, B=20;
C= (A && B);
```


__=> C=1__
<br>

## logical OR Operator: ||

- The logical-OR operator performs an inclusive-OR operation on its operands
- The result is 0 if both operands have 0 values
- If either operand has a nonzero value, the result is 1
- If the first operand of a logical-OR operation has a nonzero value, the second operand is not evaluated

<br>

## logical NOT Operator: !

- It reverses the state of the operand
- If a condition or expression is true, then Logical NOT operator will make it false

<br>