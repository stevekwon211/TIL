![sql-illustration](https://user-images.githubusercontent.com/61633137/103292935-3997c500-4a32-11eb-89c1-922f39bc9e14.png)

# Advanced SQL 1

## 1. Using String Patterns, Ranges, and Sets

### 1.1. Retrieving rows - using a String Pattern

- __WHERE__ requires a predicate
- A predicate is and expression that evaluates to True, False, or Unknown
- Use the LIKE predicate with string patterns for the search

<br>

### Example

- __WHERE__ columnname __LIKE__ string pattern

```sql
SELECT firstname FROM Author
	WHERE firstname LIKE R%
```

```sql
SELECT title, pages from Book
	WHERE pages BETWEEN 290 AND 300
```

<br>

### 1.2. Retrieving rows - using a Set of Values

```sql
SELECT firstname, lastname, country from Author
	WHERE country='AU' OR country='BR'
```

```sql
SELECT firstname, lastname, country from Author
	WHERE country IN ('AU', 'BR')
```

<br>

## 2. Sorting Result Sets

### 2.1. ORDER BY clause - Ascending order

```sql
SELECT title from Book
	ORDER BY title
```

- By default the result set is sorted in __ascending order__

<br>

### 2.2.  ORDER BY clause - Descending order

```sql
SELECT title from Book
	ORDER BY title DESC
```

- __Descending order__ with __DESC__ keyword

<br>

### 2.3. Specifying Column Sequence Number

```sql
SELECT title, pages from Book
	ORDER BY 2
```

- __Ascending order__ by __Column 2__ (number of pages)

<br>

## 3. Grouping Result Sets

### 3.1. Eliminating Duplicates - DISTINCT clause

```sql
SELECT DISTINCT(country) from Author
```

<br>

### 3.2. GROUP BY clause

```sql
SELECT country, COUNT(country)
	as Count from Author GROUP BY country
```

<br>

### 3.3. Restricting the Result Set - HAVING clause

```sql
SELECT country, count(country)
as Count from Author
GROUP BY country
having count(country) > 4
```

<br>