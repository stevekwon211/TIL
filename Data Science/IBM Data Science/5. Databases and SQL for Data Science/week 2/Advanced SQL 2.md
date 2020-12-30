![sql-illustration](https://user-images.githubusercontent.com/61633137/103292935-3997c500-4a32-11eb-89c1-922f39bc9e14.png)

# Functions, Sub-Queries, Multiple Tables

## 1. Built-in Database Functions

### 1.1. Built-in Functions

- Most databases come with built-in SQL functions
- Built-in functions can be included as part of SQL statements
- Database functions can significantly reduce the amount of data that needs to be retrieved
- Can speed up data processing

### PETRESCUE TABLE

|  ID  |  ANIMAL  | QUANTITY |  COST  | RESCUEDATE |
| :--: | :------: | :------: | :----: | :--------: |
|  1   |   Cat    |    9     | 450.09 | 2018-05-29 |
|  2   |   Dog    |    3     | 666.66 | 2018-06-01 |
|  3   |   Dog    |    1     | 100.00 | 2018-06-04 |
|  4   |  Parrot  |    2     | 50.00  | 2018-06-04 |
|  5   |   Dog    |    1     | 75.75  | 2018-06-10 |
|  6   | Hamster  |    6     | 60.60  | 2018-06-11 |
|  7   |   Cat    |    1     | 44.44  | 2018-06-11 |
|  8   | Goldfish |    24    | 48.48  | 2018-06-14 |
|  9   |   Dog    |    2     | 222.22 | 2018-06-15 |



<br>

### 1.2. Aggregate or Column Functions

- INPUT: Collection of values (e.g. entire column)
- OUTPUT: Single value
- Examples: SUM(), MIN(), MAX(), AVG(), etc.

<br>

### 1.3. SUM

- SUM function: Add up all the values in a column

```sql
select SUM(COST) from PETRESCUE
```

- Result: 
- 1
  1718.24

<br>

### 1.4. Column Alias

- Explicitly name the output column SUM_OF_COST

```sql
select SUM(COST) as SUM_OF_COST
	from PETRESCUE
```

- Result:
- SUM_OF_COST
  1718.24

<br>

### 1.5. MIN, MAX

- MIN: Return the MINIMUM value
- MAX: Return the MAXIMUM value

```sql
select MAX(QUANTITY) from PETRESCUE
```

- Result:
- 1
  24

<br>

- Get the minimum value of ID column for Dogs

```sql
select MIN(ID) from PETRESCUE where ANIMAL = 'Dog'
```

- Result
- 1
  2

<br>

### 1.6. Average

- AVG() return the average value
- Specify the Average value of COST

```sql
select AVG(COST) from PETRESCUE
```

- Result
- 1
  190.91555555

<br>

- Mathematical operations can be performed between columns
- Calculate the average COST per 'Dog'

```sql
select AVG(COST/QUANTITY) from PETRESCUE
where ANIMAL = 'Dog'
```

- Result
- 1
  127.27

<br>

### 1.7. SCALAR and STRING FUNCTIONS

- SCALAR: Perform operations on every input value
- ROUND(), LENGTH(), UCASE, LCASE
- Round UP or DOWN every value in COST

```sql
select
	ROUND(COST)
	from PETRESCUE
```

- Reuslt
- 1
  450.00
  667.00
  100.00
  50.00
  76.00

<br>

- Retrieve the length each value in ANIMAL

```sql
select
	LENGTH(ANIMAL)
	from PETRESCUE
```

- Result
- 1
  3
  3
  3
  6
  3

<br>

### 1.8. UCASE, LCASE

- Retrieve ANIMAL values in UPPERCASE

```sql
select UCASE(ANIMAL) from PETRESCUE
```

- Result
- 1
  CAT
  DOG
  DOG
  PARROT
  DOG

<br>

- Use the function in a WHERE clause

```sql
select * from PETRESCUE
where LCASE(ANIMAL) = 'cat'
```

- Result

- |  ID  | ANIMAL | QUANTITY |  COST  |    DATE    |
  | :--: | :----: | :------: | :----: | :--------: |
  |  1   |  Cat   |    9     | 450.09 | 2018-05-29 |
  |  7   |  Cat   |    1     | 44.44  | 2018-06-11 |

<br>

- Use the DISTINCT() function to get unique values

```sql
select DISTINCT(UCASE(ANIMAL)) from PETRESCUE
```

- Result
- 1
  CAT
  DOG
  GOLDFISH
  HAMSTER
  PARROT

<br>

## 2. Date and Time Built-in Functions

### 2.1. Date, Time Functions

- Most databases contain special data types for dates and times
- DATE: YYYYMMDD
- TIME: HHMMSS
- TIMESTAMP: YYYYXXDDHHMMSSZZZZZZ
- Date/Time functions: YEAR(), MONTH(), DAY(), DAYOFMONTH(), DAYOFWEEK(), DAYOFYEAR(), WEEK(), HOUR(), MINUTE(), SECOND()

<br>

- Extract the DAY portion from a date

```sql
select DAH(RESCUEDATE) from PETRESCUE
where ANIMAL='Cat'
```

- Result
- 29
  11

<br>

- Get the number of rescues during the month of May

```sql
select COUNT(*) from PETRESCUE
where MONTH(RESCUEDATE)='05'
```

- Result
- 1

<br>

### 2.2. Date of Time Arithmetic

- What date is it 3 days after each rescue date?

```sql
select (RESCUDATE + 3 DAYS) from PETRESCUE
```

- Result
- 2018-06-01
  2018-06-04
  2018-06-07
  2018-06-07
  2018-06-13

<br>

- Special Registers:

```sql
CURRENT_DATE, CURRENT_TIME
```

- Find how many days have passed since each RESCUEDATE toll now

```sql
select (CURRENT_DATE - RESCUEDATE) from PETRESCUE
```

- Result
- 10921

<br>

## 3. Sub-Queries and Nested Selects

- Sub-query: A query inside another query

```sql
select COLUMN1 from TABLE
	where COLUMN2 = (select MAX(COLUMN2) from TABLE)
```

- EMPLOYEES

| EMP_ID | F_NAME | L_NAME |  SSN   |   B_DATE   | SEX  |         ADDRESS         | JOB_ID | SALARY | MANAGER_ID | DEP_ID |
| :----: | :----: | :----: | :----: | :--------: | :--: | :---------------------: | :----: | :----: | :--------: | :----: |
| E1001  |  John  | Thomas | 123456 | 1976-01-09 |  M   | 5631 Rice, OakPark, IL  |  100   | 100000 |   30001    |   2    |
| E1002  | Alice  | James  | 123457 | 1972-07-31 |  F   | 980 Berry ln, Elgin, IL |  200   | 80000  |   30002    |   5    |
| E1003  | Steve  | Wells  | 123458 | 1980-08-10 |  M   |  291 Springs, Gary, IL  |  300   | 50000  |   30002    |   5    |

<br>

### 3.1. Why use sub-queries?

- To retrieve the list of employees who earn more than the average salary
- Cannot evaluate Aggregate functions like AVG() in the WHERE clause
- Therefore, use a sub-Select expression

```sql
select EMP_ID, F_NAME, L_NAME, SALARY
	from employees
	where SALARY <
	(select AVG(SALARY) from employees);
```

- Result

| EMP_ID | F_NAME  | L_NAME |  SALARY  |
| :----: | :-----: | :----: | :------: |
| E1003  |  Steve  | Wells  | 50000.00 |
| E1004  | Santosh | Kumar  | 60000.00 |
| E1007  |  Mary   | Thomas | 65000.00 |

<br>

### 3.2. Sub-queries in list of columns

- Substitute column name with a sub-query
- Called Column Expressions

```sql
select EMP_ID, SALARY
	( select AVG(SALARY) from employees
    	AS AVG_SALARY)
    	from employees;
```

- Result

| EMP_ID |  SALARY  |           AVG_SALARY            |
| :----: | :------: | :-----------------------------: |
| E1002  | 80000.00 | 68888.8888888888888888888888888 |
| E1003  | 50000.00 | 68888.8888888888888888888888888 |
| E1004  | 60000.00 | 68888.8888888888888888888888888 |
| E1005  | 70000.00 | 68888.8888888888888888888888888 |
| E1006  | 90000.00 | 68888.8888888888888888888888888 |
| E1007  | 65000.00 | 68888.8888888888888888888888888 |
| E1008  | 65000.00 | 68888.8888888888888888888888888 |
| E1009  | 70000.00 | 68888.8888888888888888888888888 |
| E1010  | 70000.00 | 68888.8888888888888888888888888 |

<br>

### 3.3. Sub-queries in FROM clause

- Substitute the TABLE name with a sub-query
- Called Derived Tables or Table Expressions

```sql
select * from
	( select EMP_ID, F_NAME, L_NAME, DEP_ID
    		from employees) AS EMP4ALL;
```

- Result

| EMP_ID | F_NAME  | L_NAME  | DEP_ID |
| :----: | :-----: | :-----: | :----: |
| E1002  |  Alice  |  James  |   5    |
| E1003  |  Steve  |  Wells  |   5    |
| E1004  | Santosh |  Kumar  |   5    |
| E1005  |  Ahmed  | Hussain |   2    |
| E1006  |  Nancy  |  Allen  |   2    |
| E1007  |  Mary   | Thomas  |   7    |
| E1008  | Bharath |  Gupta  |   7    |
| E1009  | Andrea  |  Jones  |   7    |
| E1010  |   Ann   |  Jacob  |   5    |

<br>

## 4. Working with Multiple Tables

### 4.1. Tables for Examples in this Lesson

- EMPLOYEES

| EMP_ID | F_NAME | L_NAME |  SSN   |   B_DATE   | SEX  |         ADDRESS         | JOB_ID | SALARY | MANAGER_ID | DEP_ID |
| :----: | :----: | :----: | :----: | :--------: | :--: | :---------------------: | :----: | :----: | :--------: | :----: |
| E1001  |  John  | Thomas | 123456 | 1976-01-09 |  M   | 5631 Rice, OakPark, IL  |  100   | 100000 |   30001    |   2    |
| E1002  | Alice  | James  | 123457 | 1972-07-31 |  F   | 980 Berry ln, Elgin, IL |  200   | 80000  |   30002    |   5    |
| E1003  | Steve  | Wells  | 123458 | 1980-08-10 |  M   |  291 Springs, Gary, IL  |  300   | 50000  |   30002    |   5    |

- DEPARTMENTS

| DEPT_ID_DEP |       DEP_NAME       | MANAGER_ID | LOC_ID |
| :---------: | :------------------: | :--------: | :----: |
|      5      | Software Development |   30002    | L0002  |
|      7      |     Design Team      |   30003    | L0003  |

<br>

### 4.2. Accessing Multiple Tables with Sub-queries

- To retrieve only the employee records that correspond to departments in the DEPARTMENTS table

```sql
select * from employees
	where DEP_ID IN
		(select DEPT_ID_DEP from departments);
```

- Result

| EMP_ID | F_NAME | L_NAME |  SSN   |   B_DATE   | SEX  |         ADDRESS         | JOB_ID | SALARY | MANAGER_ID | DEP_ID |
| :----: | :----: | :----: | :----: | :--------: | :--: | :---------------------: | :----: | :----: | :--------: | :----: |
| E1002  | Alice  | James  | 123457 | 1972-07-31 |  F   | 980 Berry ln, Elgin, IL |  200   | 80000  |   30002    |   5    |
| E1003  | Steve  | Wells  | 123458 | 1980-08-10 |  M   |  291 Springs, Gary, IL  |  300   | 50000  |   30002    |   5    |

<br>

### 4.3. Multiple Tables with Sub-queries

- To retrieve only the list of employees from a specific location
- EMPLOYEES table does not contain location information
- Need to get location info from DEPARTMENTS table

```sql
select * from employees
	where DEP_ID IN
	(select DEPT_ID_DEP from departments
    		where LOC_ID = 'L0002');
```

<br>

### 4.4. Accessing multiple tables with Implicit Join

- Specify 2 tables in the FROM clause

``` sql
select * from employees, departments;
```

- The result is a full join (or Cartesian join)
  - Every row in the first table is joined with every row in the second table
  - The result set will have more rows than in both tables

<br>

- Use additional operands to limit the result set

```sql
select * from employees, departments
		where employees.DEP_ID = 
				departments.DEPT_ID_DEP;
```

- Use shorter aliases for tables names

```sql
select * from employees E, departments D
		where E.DEP_ID = D.DEPT_ID_DEP;
```

