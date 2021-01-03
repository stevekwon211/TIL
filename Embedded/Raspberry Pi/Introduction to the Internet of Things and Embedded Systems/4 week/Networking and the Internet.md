![](https://cdn.pixabay.com/photo/2018/12/10/10/21/earth-3866609_960_720.jpg)

# 1. Networking Basics

## 1.1. Why is Networking Needed?

- To enhance many devices
  - Cars communicating to reduce traffic
  - On-line game play
  - Access media libraries
- To access data or computational power outside of the device

<br>

## 1.2. Client-Server Transactions

![Untitled Diagram](https://user-images.githubusercontent.com/61633137/103472878-02306c00-4dd6-11eb-93af-7bbcf4c2d184.png)

- Single server, one or more clients
- Server provides a service for clients
- Server manages a resource
- Server responds to requests from the client

<br>

## 1.3. Computer Networks

### 1.3.1. LAN

- Hierarchical system of computer-based devices which communicate
  - __Local Area Network (LAN)__ 
    spans a building or campus (Ethernet is most common)

<br>

### 1.3.2. WAN

- __Wide Area Network (WAN)__
  Internet is best example

<br>

### 1.3.3. MANET

- __Mobile Ad Hoc Network (MANET)__
  continually changing network built from wireless, mobile devices
  - Typically short-range
  - Most common for IoT devices

<br>

## 1.2. WAN Structure

### 1.2.1. Small LAN

![Untitled Diagram (1)](https://user-images.githubusercontent.com/61633137/103472970-d8c41000-4dd6-11eb-91ef-f38dd58971cb.png)

- Ethernet is a common LAN protocol
- Ethernet switch sends messages to the right input or output

### 1.2.2. Large LAN

![Untitled Diagram (2)](https://user-images.githubusercontent.com/61633137/103473007-3b1d1080-4dd7-11eb-8a35-a4fad7548326.png)

- Spans a building or campus
- Smaller LANs connected by __bridges__ which speak both LAN protocols

<br>

### 1.2.3. Wide Area Network

![Untitled Diagram (3)](https://user-images.githubusercontent.com/61633137/103473050-a830a600-4dd7-11eb-9cff-4db1e6949b74.png)

- Multiple LANs connected by routers

<br>

# 2. Internet Protocol

## 2.1. Internet Structure

- Ad hoc interconnection of networks
  - Unpredictable structure
  - Can be changed by anyone at any time
- Messages travel from source to destination by hopping through networks

<br>

## 2.2. How is it possible to send bits across incompatible networks?

### 2.2.1. Internet Protocol Solution

- Protocol software running on each host and router
- Common communication rules for all networks

<br>

### 2.2.2. Solution

- Implement protocol (set of rules)
  - governs how hosts and routers should cooperate when they transfer data from network to network
  - __TCP/IP__ is the protocol for the global IP Internet

<br>

## 2.3. Protocols

### 2.3.1. What Does an Internet Protocol Do?

- Provides a naming scheme
  - An Internet protocol defines a uniform format for host addresses
  - Each host (and router) is assigned at least one of these unique Internet addresses

<br>

### 2.3.2. Protocol Model

- Rules that determine how computers will communicate
- Rules enable efficient communication

<br>

### 2.3.3. Network Protocols

- Many networking tasks to transmit and receive data
  - Routing, flow control, arbitration
- OSI divides these tasks between network abstraction layers
- Each layer has its own responsibilities
- Each layer uses different data
  - Routing requires network topology
  - Arbitration may use message priorities

<br>

## 2.4. Protocol Stack

### 2.4.1. OSI Layer Concept

![Untitled Diagram (4)](https://user-images.githubusercontent.com/61633137/103473206-66086400-4dd9-11eb-9ad1-d8b8bb5d076b.png) 

- Message is received at each layer and decisions are made
- Assume layer __R__ performs routing, transmission
  - Message __M__ is received by layer __R__
  - Layer __R__ identifies a route for message __M__
  - Layer __R__ adds routing information, creating __M`__
  - Layer __R__ passes message __M`__ to the next lower layer

<br>

### 2.4.2. Encapsulation

- Communication tasks are confined to one protocol layer
- __Protocol stack__ is the implementation (usually software) of each protocol layer
- __Transmission__
  - Messages start at top layer and go down
  - Message decisions are made at each layer
  - Relevant information is added to the message at each layer (header or footer)
- __Reception__
  - Messages start at bottom later and go up
  - Relevant information is stripped information is stripped at each layer
  - New decisions are made, if necessary

<br>

# 3. Network Layers and MANETS

## 3.1. TCP/IP Application Layer

- __TCP/IP__

  ![Untitled Diagram (5)](https://user-images.githubusercontent.com/61633137/103473454-327b0900-4ddc-11eb-9564-2a2f48d62ae3.png) 

  - Transmission Control Protocol (TCP), Internet Protocol (IP)
  - Protocol stack used in the Internet

- TCP/UDP used at Transport layer: App to App

- IP used at network layer: Host to Host

- 4 layers total, unlike OSI's 7

<br>

## 3.2. Application Layer

- Protocols that directly support applications
- Information is application-specific
  - __Simple Mail Transfer Protocol (SMTP)__ : email
  - __Hypertext Transfer Protocol (HTTP)__ : web
  - __Line Printer Daemon (LPD)__ : printing

<br>

## 3.3. MANETs

![Untitled Diagram (6)](https://user-images.githubusercontent.com/61633137/103473577-a5d14a80-4ddd-11eb-8081-765bc5e170c3.png) 

- Self-configuring network of mobile hosts/routers
- Connected by wireless links
- Often connected to a wired LAN via an __Access Point__
- Common for IoT devices

<br>

### 3.3.1. Power Budget

- Mobile devices are power constrained
- Standard LAN protocols must be modified
- Battery is often the heaviest component

<br>

### 3.3.2. Data Rate and Security

- Data Rate
  - Wireless bandwidth is lower than wired
  - Bandwidth costs power
- Security
  - Power is not available for complex security
  - No encryption, anti-virus, etc

<br>

