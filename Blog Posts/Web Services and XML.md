# Data on the Web

- With the HTTP Request/Response well understood and well supported, there was a natural move toward exchanging data between programs using these protocols
- We needed to come up with an agreed way to represent data going between applications and across networks
- There are two commonly used formats: XML and JSON

<br>

# Sending Data across the "Net"

## Agreeing on a "Wire Format"

### XML Example

__Python Dictionary__   
=> Serialize    

```XML
<person>
  <name>  
    Chuck  
  </name>  
  <phone>  
    303 4456  
  </phone>  
</person>  
```
=> De-Serialize  
__Java HashMap__

<br>

### JSON Example

__Python Dictionary__   
=> Serialize    

```JSON
{
  "name":  
    "Chuck",  
  "phone":  
    "303 4456"  
}   
```

=> De-Serialize  
__Java HashMap__

<br>

# XML "Elements" (or Nodes)

```XML 
<people>  
  <person>  
    <name>Chuck</people>
    <phone>303 4456</phone>
  </person>
  <person>
    <name>Noah</name>
    <phone>622 7421</phone>
  </person>
</people>
```

- Simple Element

  ```XML
  <name>Chuck</people>
  <phone>303 4456</phone>
  ```


- Complex Element

  ```xml
  <person>
    <name>Noah</name>
    <phone>622 7421</phone>
  </person>
  ```

<br>

# eXtensible Markup Language

- Primary purpose is to help information systems __share structured data__
- It started as a simplified subset of the Standard Generalised Markup Language (SGML), and is designed to be relatively human-legible

<br>

# XML Basics

- Start Tag

  ```xml
  <phone>
  ```
  
- End Tag

  ```xml
  </phone>
  ```

- Text Content

  ```xml
  <phone> 111 1111 </phone>
  ```

- Attribute

  ```xml
  <phone type="intl">
  ```

- Self Closing Tag

  ```xml
  <phone hide="yes" />
  ```

<br>

# XML Terminology

- __Tags__ indicate the beginning and ending of elements
- __Attributes__ - Keyword/value pairs on the opening tag of XML
- Serialize / De-Serialize - Convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner

<br>

# XML Schema

- Description of the __legal format__ of an XML document
- Expressed in terms of constraints on the structure and content of documents
- Often used to specify a __"contract"__ between systems - "My system will only accept XML that conforms to this particular Schema."
- If a particular piece of XML meets the specification of the Schema - it is said to __"validate"__   
  
  
- XML Document

```xml
<person>
 <lastname>Serverance</lastname>
 <age>17</age>
 <dateborn>2001-04-17</dateborn>
</person>
```

  

- XML Schema Contract

```xml
<xs:complexType name="person">
 <xs:sequnce>
   <xs:element name="lastname" type="xs:string"/>
   <xs:element name="age" type="xs:integer"/>
   <xs:element name="dateborn" type="xs:date"/>
 </xs:sequnce>
</xs:complexType>
```

<br>

# Many XML Schema Languages

- Document Type Definition (DTD)
- Standard Generalised Markup Language (ISO 8879:1986 SGML)
- XML Schema from W3C - (XSD)

<br>

# XSD XML Schema (W3C spec)

- It is often called "W3C Schema" because "Schema" is considered generic
- More commonly it is called XSD because the file names end in .xsd

<br>

# XSD Structure

- xs:element

```xml
<xs:element name="age" type="xs:integer"/>
```

- xs:sequence

```xml
<xs:sequence>
</xs:sequence>
```

- xs:complexType

```xml
<xs:complexType name="person">
</xs:complexType>
```

<br>

# Parsing XML

```python
import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
```

