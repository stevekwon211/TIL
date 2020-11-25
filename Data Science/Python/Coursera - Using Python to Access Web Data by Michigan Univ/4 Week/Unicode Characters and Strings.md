# ASCII

American Standard Code for Information Interchange

![](TIL/Data Science/Python/Coursera - Using Python to Access Web Data by Michigan Univ/src/asciifull.png)

<br>

## Representing Simple Strings

- Each character is represented by a number between 0 and 256 stored in 8 bits of memory
- We refer to "8 bits of memory as a __"byte"__ of memory - (i.e. my disk drive contains 3 Tera__bytes__ of memory)
- The __ord()__ function tells us the numeric value of a simple ASCII character

```python
>>> print(ord('H'))
72
>>> print(ord('e'))
101
>>> print(ord('\n'))
10
```

<br>

## Multi-Byte Characters

- To represent the wide range of characters computers must handle we represent characters with more than one byte

  - UTF-16 - Fixed length - Two bytes

  - UTF-32 - Fixed Length - Four bytes

  - __UTF-8__ - 1~4 bytes

    - Upwards compatible with ASCII
    - Automatic detection between ASCII and UTF-8
    - UTF-8 is recommended practice for encoding data to be exchanged between systems

<br>

## Two Kinds of Strings in Python

### Python 2 Versus Python 3

```python
# Python 2.7.10
>>> x = '권혁일'
>>> type(x)
<type 'str'>
>>> x = u'권혁일'
>>> type(x)
<type 'unicode'>
```

```python
# Python 3.5.1
>>> x = '권혁일'
>>> type(x)
<class 'str'>
>>> x = u'권혁일'
>>> type(x)
<class 'str'>
```

__=> In Python 3, all strings are Unicode__

<br>

```python
# Python 2.7.10
>>> x = b'abc'
>>> type(x)
<type 'str'>
>>> x = '권혁일'
>>> type(x)
<type 'str'>
>>> x = u'권혁일'
>>> type(x)
<type 'unicode'>
```
__=> In Python 2, byte string and regular string are the same,__  
__and the Unicode string are different__
```python
# Python 3.5.1
>>> x = b'abc'
>>> type(x)
<class 'bytes'>
>>> x = '권혁일'
>>> type(x)
<class 'str'>
>>> x = u'권혁일'
>>> type(x)
<class 'str'>
```
__=> In Python 3, Unicode string and regular string are the same,__  
__and the byte string are different__  

<br>

## Python 3 and Unicode

In Python 3, all strings internally are UNICODE  
Working with string variables in Python programs and reading data from files usually "just works"  
When we talk to a network resource using sockets or talk to a database we have to encode and decode data (usually to UTF-8)

<br>

## Python Strings to Bytes

- When we talk to an external resource like a network socket we sends bytes, so we need to encode Python 3 strings into a given character encoding
- When we read data from an external resource, we must decode it based on the character set so it is properly represented in Python 3 as a string

```python
while True:
    data = mysock.recv(512) # data -> bytes
    if (len(data)<1):
        break
    mystring = data.decode() # mystring -> Unicode
    print(mystring)
```

<br>

## An HTTP Request in Python

```python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pre4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() # Bytes
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode()) # Unicode
mysock.close()
```

