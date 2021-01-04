![](https://cdn.pixabay.com/photo/2014/04/02/10/17/disk-303333_960_720.png)

# 1. How to Access Databases Using Python

## 1.1. Benefits of python for database programming

- Python ecosystem: Numpy, pandas, matplotlib, SciPy
- Ease of use
- Portable
- Python supports relational database systems
- Python Database API (DB-API)
- Detailed documentation

<br>

## 1.2. What are Jupyter Notebooks?

- Language of choice
  - Python
  - R
  - Julia
  - Scala
  - and more..
- Share notebooks
  - Email
  - Dropbox
  - Github
  - Jupyter notebook viewer
- Interactive output
  - HTML
  - Images
  - videos
  - LaTex
  - and more..
- Big data integration
  - Apache Spark from Python, R, Scala

<br>

## 1.3. Accessing databases using Python

<img src="https://user-images.githubusercontent.com/61633137/103435354-46463400-4c51-11eb-8702-b109d4b0890d.png" alt="Untitled Diagram" style="zoom:150%;" /> 

<br>

## 1.4. What is a SQL API?

![Untitled Diagram (1)](https://user-images.githubusercontent.com/61633137/103435380-af2dac00-4c51-11eb-985d-ce6fb0bd48a3.png) 

<br>

## 1.5. APIs used by popular SQL-based DBMS systems

| Application or Database                  | SQL API     |
| :--------------------------------------- | :---------- |
| MySQL                                    | MySQL C API |
| PostgreSQL                               | psycopg2    |
| IBM DB2                                  | ibm_db      |
| SQL Server                               | dblib API   |
| Database access for Microsoft Windows OS | ODBC        |
| Oracle                                   | OCI         |
| Java                                     | JDBC        |

<br>

# 2. Writing code using DB-API

## 2.1. Benefits of using DB-API

- Easy to implement and understand
- Encourages similarity between the Python modules used to access databases
- Achieves consistency
- Portable across databases
- Broad reach of database connectivity from Python

<br>

## 2.2. Examples of libraries used by database systems to connect to Python applications

| Database               | DB API                 |
| ---------------------- | ---------------------- |
| IBM DB2                | ibm_db                 |
| Compose for MySQL      | MySQL Connector/Python |
| Compose for PostgreSQL | psycopg2               |
| Compose for MongoDB    | PyMongo                |

<br>

## 2.3. Concepts of the Python DB API

- Connection Objects
  - Database connections
  - Manage transactions
- Cursor Objects
  - Database Queries
  - Scroll through result set
  - Retrieve results

<br>

### 2.3.1. Connection methods

- .cursor(): returns a new cursor object using the connection 
- .commit(): is used to commit any pending transaction to the database
- .rollback(): which causes the database to roll back to the start of any pending transaction
- .close(): is used to close a database connection

<br>

### 2.3.2. Cursor methods

- .callproc()
- .execute()
- .executemany()
- .fetchone()
- .fetchmany()
- .fetchall()
- .nextset()
- .arraysize()
- .close()

<br>

## 2.4. What is a database cursor?

![Untitled Diagram (2)](https://user-images.githubusercontent.com/61633137/103435546-74c50e80-4c53-11eb-90da-822edbe20809.png) 

- A database cursor is a control structure that enables a database to pass through records. 

  Works like a file name or file handle in a programming language. 

  Just as a program opens a file to access the file, the cursor opens to access the query results. 

  Similarly, the program closes the file to terminate access and closes the cursor to terminate access to query results. 

  Another similarity is that the cursor keeps track of the program's current location within the query results, just as the file handle tracks the program's current location within an open file.

<br>

## 2.5. Writing code using DB-API

```python
from dbmodule import connect
# Create connection object
Connection = conncec('databasename', 'username', ' pswd')

# Create a cursor object
Cursor = connection.cursor()

# Run Queries
Cursor.execute('select * from mytable')
Results = cursor.fetchall()

# Free resources
Cursor.close()
Connection.close()
```

<br>

# 3. Connecting to a database using ibm_db API

## 3.1. What is ibm_db?

- The ibm_db API provides a variety of useful Python functions for accessing and manipulating data in an IBM data server Database
- ibm_db API uses the IBM Data Server Driver for ODBC and CLI APIs to connect to IBM DB2 and Informix

<br>

## 3.2. Identify database connection credentials

```python
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"
dsn_hostname = "YourDb2Hostname"
dsn_port = "50000"
dsn_protocol = "TCPIP"
dsn_uid = "abc12345"
dsn_pwd = "7asdvbsd779af@#@!"
```

<br>

## 3.3. Create & Close a database connection

```python
# Create database connection
dsn = (
    "DRIVER={{IBM DB2 ODBC DRIVER}};"
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "PROTOCOL=TCPIP;"
    "UID={3};"
    "PWD={4};").format(dsn_database, dsn_hostname, dsn_port, dsn_uid, dsn_pwd)

try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected!")
   
except:
    print("Unable to conncet to database")
```

```python
# Close the database conncetion
ibm_db.close(conn)
```

<br>

# 4. Creating tables, loading data, querying data

- Example Tables "Trucks"

| Serial No | Model         | Manufacturer           | Engine Size    | Class                      |
| --------- | ------------- | ---------------------- | -------------- | -------------------------- |
| A1234     | Lonestar      | International Trucks   | Cummins ISX15  | Class 8                    |
| B5432     | Volvo VN      | Volvo Trucks           | Volvo D11      | Heavy Duty Tractor Class 8 |
| C5674     | Kenworth W900 | Kenworth Truck Company | Caterpillar C9 | Class 8                    |

<br>

## 4.1. ibm_db.exec_immediate()

- The parameters for the function are
  - Conncetion
  - Statement
  - Options

<br>

### 4.1.1. Python code to create a table

```python
stmt = ibm_db.exec_immediate(conn,
"CREATE TABLE Trucks(serial_no varchar(20) PRIMARY KEY NOT NULL, model VARCHAR(20) NOT NULL, manufacturer VARCHAR(20) NOT NULL, Engine_size VARCHAR(20) NOT NULL, Truck_Class VARCHAR(20) NOT NULL)"
)
```

<br>

### 4.1.2. Python code to insert data into the table

```python
stmt = ibm_db.exec_immediate(conn,
"INSERT INTO Trucks(serial_no, model, manufacturer, Engine_size, Truck_Class) VALUES('A1234', 'Lonestar', 'International Trucks', 'Cummins ISX15', 'Class 8');"
)
```

<br>

### 4.1.3. Python code to query data

```python
ibm_db.fetch_both(stmt)
```

<br>