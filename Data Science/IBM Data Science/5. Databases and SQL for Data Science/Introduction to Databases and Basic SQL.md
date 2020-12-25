![27856393600_f0c6542b04_z](https://user-images.githubusercontent.com/61633137/103135391-5f079480-46fb-11eb-8e0b-505fca1ae79b.jpg)

# 0. Before Start.. Why SQL for Data Science?

- Job
  - Median based salary: $110,000
  - Job satisfaction score: 4.4/5
  - Top spot on Glassdoor's best jobs in America
  - Top three skills for a Data Scientist
- Needs for somewhere with data
  - Big data
  - Table with a few rows
  - Small start up
  - Big database
  - Mobile phone
- Advantages
  - Boost your professional profile
  - Give you a good understanding of relational databases

<br>

# 1. Introduction to Databases

## 1.1. What is SQL?

- __S__ tructured __Q__ uery __L__ anguage
- A language used for relational databases
- Query data

<br>

## 1.2. What is Data?

- Facts (words, numbers)
- Pictures
- One of the most critical assets of any business
- Needs to be secure

<br>

## 1.3. What is a database?

- A repository of data
- Provides the functionality for adding, modifying and querying that data
- Different kinds of databases store data in different forms

<br>

## 1.4. Relational Database

- Data stored in tabular form - columns and rows
- Columns contain item properties e.g. Last Name, First Name, etc
- Table is collection of related things e.g Employees, Authors, etc.
- Relationships can exist between tables (hence: "relational")

<br>

## 1.5. DBMS

- Database: repository of data
- DBMS: Database Management System - software to manage databases
- Database, Database Server, Database System, Data Server, DBMS - often used interchangeably

<br>

## 1.6. What is RDBMS?

- RDBMS = Relational database management system
- A set of software tools that controls the data
  - access, organization, and storage
-  Examples are: MySQL, Orcale Database, IBM Db2, etc

<br>

## 1.7. Basic SQL Commands

- Create a table
- Insert
- Select
- Update
- Delete

<br>

# 2. How to create Database Instance on Cloud

## 2.1. Cloud databases

- Ease of Use and Access
  - API
  - Web Interface
  - Cloud or Remote Applications
- Scalability & Economics
  - Expand/Shrink Storage & Compute Resources
  - Pay per use
- Disaster Recovery
  - Cloud Backups and Geographical Distribution

<br>

## 2.2. Examples of Cloud databases

- IBM Db2
- Databases for PostgreSQL
- Orcale Database Cloud Service
- Microsoft Azure SQL Database
- Amazon Relational Database Services (RDS)



- Available as
  - VMs or Managed Service
  - Single or Multi-tenant

<br>

## 2.3. Database service instances

- DBaaS provides users with access to Database resources in cloud without setting up hardware and installing software
- Database service instance holds data in data objects/tables
- Once data is loaded, it can be queried using web interfaces and application

<br>

## 2.4. Creating a database instance on IBM Db2 on Cloud

1. Login IBM Cloud 
2. Select Catalog, and Databases
3. Select Db2

![Screenshot from 2020-12-25 20-09-53](https://user-images.githubusercontent.com/61633137/103133835-126a8c00-46f0-11eb-83f9-b3236c90a000.png)

<br>

# 3. Relational Database Concepts

## 3.1. Relational Model

- Most used data model
- Allows for data independence
- Data is stored in a tables

<br>

## 3.2. Entity-Relationship Model

- Used as a tool to design relational databases

<br>

## 3.3. Mapping Entity Diagrams to Tables

- Entities become tables
- Attributes get translated into columns

<br>

## 3.4. Primary Keys and Foreign Keys

- Primary Key
  - A Primary Key uniquely identifies a specific row in a table
- Foreign Key
  - Tables can also contain foreign keys which are primary keys defined in other tables, creating a link between the tables

<br>

# 4. Basic SQL


## 4.1. CREATE Table Statement

SQL Statement types: __DDL__ and __DML__

### 4.1.1. Types of SQL Statements - DDL

- __DDL__ (Data Definition Language) statements
  - Define, change, or drop data
- __Common DDL__
  - CREATE
  - ALTER
  - TRUNCATE
  - DROP

<br>

### 4.1.2. Types of SQL Statements - DML

- __DML__ (Data Manipulation Language) statements
  - Read and modify data
  - __CRUD__ operations (Create, Read, Update, Delete rows)
- __Common DML__
  - INSERT
  - SELECT
  - UPDATE
  - DELETE

<br>

### 4.1.3. CREATE table

- Syntax

```SQL
CREATE TABLE table_name
	(
	column_name_1 datatype optional_parameters,
	column_name_2 datatype,
	...
	column_name_n datatype
	)
```

<br>

- Example - Create a table for Canadian provinces

```sql
CREATE TABLE provinces(
	id char(2) PRIMARY KEY NOT NULL,
    name varchar(24)
	)
```

<br>

### 4.1.4. CREATE TABLE Statement

- To create the Author table, use the following columns and datatypes
  - Example - AUTHOR
    - Author_ID : char
    - Lastname : varchar
    - Firstname : varchar
    - Email : varchar
    - City : varchar
    - Country : char

```sql
CREATE TABLE author(
	author_id CHAR(2) PRIMARY KEY NOT NULL,
    lastname VARCHAR(15) NOT NULL,
    firstname VARCHAR(15) NOT NULL,
    email VARCHAR(40),
    city VARCHAR(15),
    country CHAR(2)
	)
```

- NOT NULL : The field cannot contain a NULL value

<br>

## 4.2. SELECT Statement

### 4.2.1. Retrieving rows from a table

- After creating a table and inserting data into the table, we want to see the data
- SELECT statement
  - A Data Manipulation Language (DML) statement used to read and modify data

<br>

### 4.2.2. Retrieving a subset of the columns

- You can retrieve just the columns you want
- The order of the columns displayed always matches the order in the SELECT statement

```sql
SELECT book_id, title FROM Book
```

<br>

### 4.2.3. Restricting the Result Set: WHERE Clause

- Restricts the result set
- Always requires a Predicate
  - Evaluates to
    - True
    - False
    - Unknown
  - Used in the search condition of the Where clause

```sql
SELECT book_id, title FROM Book WHERE book_id='B1'
```

- WHERE Clause Comparison Operators

|        Operators         |      |
| :----------------------: | :--: |
|         Equal to         |  =   |
|       Greater than       |  >   |
|        Less than         |  <   |
| Greater than or equal to |  >=  |
|  Less than or equal to   |  <=  |
|       Not equal to       |  <>  |

<br>

## 4.3. COUNT, DISTINCT, LIMIT

### 4.3.1. COUNT

- COUNT() : a built-in function that retrieves the number of rows matching the query criteria

- Number of rows in a table

  ```sql
  SELECT COUNT(*) FROM tablename
  ```

  <br>

- Example - Rows in the MEDALS table where Country is Canada

  ```sql
  SELECT COUNT(COUNTRY) FROM MEDALS WHERE COUNTRY='CANADA'
  ```

<br>

### 4.3.2. DISTINCT

- DISTINCT : use to remove duplicate values from a result set

- Retrieve unique values in a column

  ```sql
  SELECT DISTINCT columnname FROM tablename
  ```

- Example - List of unique countries that received GOLD medals

  ```sql
  SELECT DISTINCT COUNTRY FROM Medals WHERE MEDALTYPE = 'GOLD'
  ```

<br>

### 4.3.3. LIMIT

- LIMIT : use for restricting the number of rows retrieved from the database

- Retrieve just the first 10 rows in a table

  ```sql
  select * from tablename LIMIT 10
  ```

- Example - Retrieve 5 rows in the MEDALS table for a particular year

  ```sql
  select * from MEDALS where YEAR = 2018 LIMIT 5
  ```

  <br>

## 4.4. INSERT Statement

### 4.4.1. Adding rows to a table

- Create the table (CREATE TABLE statement)
- Populate table with data
  - INSERT statement
    - a Data Manipulation Language (DML) statement used to read and modify data

<br>

### 4.4.2. Using the INSERT Statement

```sql
INSERT INTO tablename <(columnname)> VALUES (values)
```

```sql
INSERT INTO AUTHOR
	(AUTHOR_ID, LASTNAME, FIRSTNAME, EMAIL, CITY, COUNTRY)
VALUES('A1', 'Kwon', 'Hyukil', 'stevekwon211@gmail.com', 'Seongnam-si Bundang-gu', 'South Korea')
```

<br>

## 4.5. UPDATE & DELETE Statements

### 4.5.1. Altering rows of a table - UPDATE statement

- After creating a table and inserting data into the table, we can alter the data
  - UPDATE statement
    - A Data Manipulation Language (DML) statement used to read and modify data

<br>

### 4.5.2. Using the UPDATE Statement

```sql
UPDATE tablename SET columnname=value WHERE condition
```

```sql
UPDATE AUTHOR
SET LASTNAME = 'Kwon'
	FIRSTNAME = 'Steve'
	WHERE AUTHOR_ID = 'A1'
```

<br>

### 4.5.3. Deleting rows from a table

- Remove 1 or more rows from the table
  - DELETE statement
    - A DML statement used to read and modify data

```sql
DELETE FROM tablename WHERE condition
```

<br>

### 4.5.4. Using the DELETE Statement

```sql
DELETE FROM AUTHOR
	WHERE AUTHOR_ID IN ('A1')
```

