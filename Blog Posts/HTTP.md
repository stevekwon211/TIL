# Application Protocol

- Since TCP (and Python) gives us a reliable __socket__, what do we want to do with the __socket__? What problem do we want to solve?

- Application Protocols

  - Mail

  - World Wide Web (WWW)
    <br>

# HTTP - Hypertext Transfer Protocol

- The dominant Application Layer Protocol on the Internet
- Invented for the Web - to Retrieve HTML, Images, Documents, etc
- Extended to be data in addition to documents - RSS, Web Services, etc.
- Basic Concept
  - 1. Make a Connection
  - 2. Request a document
  - 3. Retrieve the Document
  - 4. Close the Connection
       <br>

# HTTP

The __HyperText Transfer Protocol__ is the set of rules to allow browsers to retrieve web documents from servers over the Internet

<br>

# What is a Protocol?

- A set of rules that all parties follow so we can predict each other's behaviour
- And not bump into each other
  - On two-way roads in USA, drive on the right-hand side of the road
  - On two-way roads in the UK, drive on the left-hand side of the road

`http://stevekwon211.github.io/blog`

=> `http://` : protocol

=> `stevekwon211.github.io` : host

=> `/blog` : document

<br>

#  Getting Data From The Server

- Each the user clicks on  an anchor tag with an __href=__ value to switch to a new page,
  the browser makes a connection to the web server and issues a __"GET"__ request - to GET the content of the page at the specified URL.
- The server returns the __HTML document__ to the Browser which formats and displays the document to the user.

<br>

# Internet Standards

- The standards for all of the Internet protocols (inner workings) are developed by an organisation
- Internet Engineering Task Force (IETF)
- Standards are called __"RFCs" - "Request for Comments"__

<br>

# Making an HTTP request

Connect to the server like __https://stevekwon211.github.io__  
Request a document (or the default document)  

- GET `http://stevekwon211.github.io/blog`
- GET `https://stevekwon211.github.io/about`

<br>

# An HTTP Request in Python

```python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pre4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
```

