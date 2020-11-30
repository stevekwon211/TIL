# JavaScript Object Notation (JSON)

- __JSON__ is an open standard file format and data interchange format.

```python
import json
data = '''{
	"name" : "Chuck",
	"phone" : {
		"type" : "intl"
		"number" : "+1 123 456 7890"
	},
	"email" : {
		"hide" : "yes"
	}
}'''

info = json.loads(data)
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])
```

- JSON represents data as nested __lists__ and __dictionaries__

```python
import json
input = '''[ 			# list starts here
	{					# first dictionary start here
		"id" : "001",
		"x" : "2",
		"name" : "Chuck"
	},					# first dictionary ends here
	{					# second dictionary starts here
		"id" : "009",
		"x" : "7",
		"name" : "Kwon"
	}					# second dictionary ends here
]'''					# list ends here

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
```

<br>

# REST (Representative State Transfer)

## Overview

- REST refers to an interface that defines how data is transmitted and processed on the web. All data structures and processing methods are defined through URLs in REST, so they are very intuitive to understand. It is also an element that makes it easier to approach when providing services to the public.

<br>

## REST Concept

- This means specifying a resource (Resource) through the HTTP Uniform Resource Identifier (URI) and applying CRUD Operation to that resource through the HTTP Method (POST, GET, PUT, DELETE).
  REST refers to an architecture that has a resource at the center of a resource-oriented architecture design and is designed to handle the resource through HTTP methods. Give HTTP URI, a unique ID, to all resources such as images, text, and DB content of a website.

<br>

## CRUD action

- Create: Data generation (POST)
- Read: Data inquiry (GET)
- Update: Modify Data (PUT)
- Delete: Delete data (DELETE)
- HEAD: Query header information of data on a network (HEAD)

<br>

## REST Configuration

- Resources - URI
- Behaviour (Verb) - HTTP Method
- Expression (Representations)

<br>

## Features of REST

- Uniform
  - If only by the HTTP standard, it means an architecture style that can be used on any platform, whether it is an Android/IOS platform, without being dependent on a particular language or technology, and can be manipulated for resources designated by URI.
- Stateless
    - REST has a stateless character. In other words, it does not store and manage status information for work separately. Because session information or cookie information is not stored and managed separately, the API server simply processes incoming requests. This increases the freedom of service and simplifies implementation by not managing unnecessary information on the server.
- Cache-able
	- One of the biggest features of REST is that it uses the existing web standard called HTTP, so it can take advantage of the existing infrastructure it uses on the web. Therefore, the caching function of HTTP can be applied. Last-Modified tags or E-Tag, which are used in HTTP protocol standards, enable caching.

- Self-description (self-expression structure)
  - Another big feature of REST is that it has a self-expression structure that makes it easy to understand only by viewing REST API messages.

- Client-Server Structure
  - Because REST servers provide APIs and clients manage user authentication or context (session, login information) directly, each role is divided, what needs to be developed by clients and servers becomes less dependent on each other.

- Hierarchical structure
  - REST servers can consist of multiple tiers and add security, load balancing, and encryption layers to provide structural flexibility and enable network-based intermediaries such as PROXY and gateway to use.

<br>

## The Advantages and Disadvantages of REST

- Advantages
  - There is no need to rescue separate infrastructure for using the REST API because the infrastructure of the HTTP protocol is still used.
  - It makes most of the HTTP protocol's standards, allowing you to take many additional benefits together.
  - It is available on any platform that complies with the HTTP standard protocol.
  - Ensure universality while faithfully following the basics of Hypermedia API.
  - The REST API message indicates what it is intended, so it is easy to understand what it is intended.
  - Minimise possible problems in various service designs.
  - Clear separation of server and client roles.

- Disadvantages
  - The standard itself does not exist, so a definition is needed.
  - There are only four methods available.
  - HTTP method form is limited.
  - If a service has a lot of work to be tested through a browser, expertise is required because it has to deal with the value of header information rather than the URL that can be easily fixed.
  - Many actions cannot be supported by older browsers because they are not compatible. (Explore)

<br>

## URI Design Rules in RESTful API #
- Use lowercase letters (minimum case-sensitive)
- A hyphen (-, hyphen): Remove spaces
- Avoid using extension: Put a value in the header.
- CRUD should not be used in URI.

<br>

## HTTP method

- POST: Create a resource (Document) one step below the current resource (Collection)
- GET: Look up current resource (collection, document)
- PUT: Modification of information on current resources (complete modification of those resources)
- DELETE: Delete the current resource (Document)
- PATCH: Modifying the current resource (part of that resource)

## REST Header

- Reactive Web: Provides screen regardless of user-Agent -> Web Client

  <br>

## Response Code

- 200: Normal execution of client requests (including messages for responses)
- 201: Normal processing of requests for resource creation
- 202: Used when resource creation requests are processed asynchronously
- 204: Normal execution of client requests (not including messages for responses, used for delete requests, etc.)
- 400: Used when client requests are inappropriate (inappropriate reasons should be included in response body)
- 401: Used when clients request protected resources without authentication
- 403: Used when clients request resources that they do not want to respond to regardless of their authentication status (recommended to use 400)
- 404: Used when the requested resource does not exist by the client
- 405: When the client uses an impossible method

<br>

# Service Oriented Approach

- Most non-trivial web applications use services
- They use services from other applications
- Services publish the __rules__ applications must follow to make use of the service (__API__)

<br>

## Multiple Systems

- Initially - two systems cooperate and split the problem
- As the data/service becomes useful - multiple applications want to use the information / application

<br>

# Using Application Programming Interfaces

## Application Program Interface

- Application Programming Interface (API) is an interface that allows you to control the functions provided by the operating system or programming language for use in applications. It mainly provides interfaces for file control, window control, video processing, character control, etc.

<br>

## API Security and Rate Limiting

- The compute resources to run these APIs are not __free__
- The data provided by these APIs is usually valuable
- The data providers might limit the number of requests per day, demand an API __key__, or even charge for usage 