## Algorithm Basic

- __Algorithm__ : Procedures established to solve the problem
- __Sequential Structure__ : Structure that is processed in order by sentence
- __Conditional Expression__ : Expression which is between __if__ and __: (colon)__
- __Select Structure__ : Structure in which the execution flow changes according to the results of a conditional evaluation 

<br>

- Example of Sequential & Select Structure

```python
print('Find a maximum number')
a = int(input('Number a: '))
b = int(input('Number b: '))
c = int(input('Number c: '))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'Maximum value is {maximum}.')
```

![GIF 10-01-2021 21-01-56](https://user-images.githubusercontent.com/61633137/104122237-303e1f00-5387-11eb-9872-4be0e0247ff9.gif)

<br>

- Find a median number

```python
def med3(a, b, c):
    if a >= b:
        if b>= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print('Find a median nubmer')
a = int(input('Number a: '))
b = int(input('Number b: '))
c = int(input('Number c: '))

print(f'Median value is {med3(a, b, c)}.')
```

![GIF 10-01-2021 21-11-48](https://user-images.githubusercontent.com/61633137/104122512-b73fc700-5388-11eb-81d4-eb8dd31826ea.gif)

<br>

## Operator & Operand

- __Operator__ : +, - , / , * , etc.
- __Unary Operator__ : 1 operand
- __Binary Operator__ : 2 operand
- __Ternary Operator__ : 3 operand
  (Conditional Operator __if ~ else__ syntax is the only Ternary Operator in Python.)

<br>

- Example

```python
n = int(input('Input Number.'))

if n == 1:
    print('A')
elif n == 2:
    print('B')
elif n == 3:
    print('C')
else:
    pass
```

![GIF 10-01-2021 21-11-48](https://user-images.githubusercontent.com/61633137/104122919-49e16580-538b-11eb-949a-259ffeb610fb.gif)

<br>

## Flowchart

- A picture that illustrates the method to define, analyse and solve the problem.

<br>

- __Data__![Data](https://user-images.githubusercontent.com/61633137/104123350-1b18be80-538e-11eb-8024-3f3a028a2480.png): It refers to the data itself without specifying a memory device.

<br>

- __Activity / Process / Entity / External Interactor__ ![Process](https://user-images.githubusercontent.com/61633137/104123494-db060b80-538e-11eb-8e9e-7f2ab8da93ed.png) : It represents different kinds of processing functions. 

<br>

- __Predefined Process__ ![Process](https://user-images.githubusercontent.com/61633137/104123380-4ac7c680-538e-11eb-8b22-f159da386a87.png) : It represents a process consisting of one or more operations or commands already defined elsewhere, such as a subroutine or module.

<br>

- __Decision__ ![Predefined Process](https://user-images.githubusercontent.com/61633137/104123534-16083f00-538f-11eb-9e83-53b51bb79c6f.png) : it refers to a decision function (switching function) that selects one exit by evaluating the conditions defined in the decision symbol.

<br>

- __Loop Limit__ ![Decision](https://user-images.githubusercontent.com/61633137/104123572-4cde5500-538f-11eb-9544-e424f1df0113.png) : It consists of two parts, indicating the start and end of the loop.

<br>

