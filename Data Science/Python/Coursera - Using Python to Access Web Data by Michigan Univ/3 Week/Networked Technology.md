# Transport Control Protocol (TCP)

- Built on top of IP (Internet Protocol)
- Assumes IP might lose some data - stores and retransmits data if it seems to be lost
- Handles "flow control" using a transmit window
- Provides a nice reliable pipe

![](/home/stevekwon/Documents/TIL/Data Science/Python/Coursera - Using Python to Access Web Data by Michigan Univ/src/IP_stack_connections.png)



Source: https://en.wikipedia.org/wiki/Internet_protocol_suite

<br>

# TCP Connections / Sockets

- In computer networking, an Internet __socket__ or network __socket__ is an endpoint of a bidirectional __inter-process__ communication flow across an __Internet__ Protocol-based computer network, such as the __Internet__

<br>

# TCP Port Numbers

- A port is an __application-specific__ or process-specific software communications endpoint
- It allows multiple networked applications to coexist on the same server
- There is a list of well-known TCP port numbers

<br>

# Common TCP Ports

- Telnet (23) - Login
- SSH (22) - Secure Login
- HTTP (80)
- HTTPS (443) - Secure
- SMTP (25) - Mail
- IMAP (143/220/993) - Mail Retrieval
- POP (109/110) - Mail Retrieval
- DNS (53) - Domain Name
- FTP (21) - File Transfer

<br>

# Sockets in Python

Python has built-in support for TCP Sockets

```python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80)) #'Host', Port
```

