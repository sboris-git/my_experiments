=============dvdrental===================
http://www.postgresqltutorial.com/postgresql-select-distinct/

#  Select and contecate first_name, last_name
#  Sort...
SELECT 
   first_name || ' ' || last_name
FROM 
   customer
ORDER BY 
	first_name,
	last_name DESC;  -- ASC used as default/ DESC


# The same with condition
SELECT 
   first_name || ' ' || last_name
FROM 
   customer
WHERE
   (first_name = 'Jamie' OR
   last_name = 'Rodriguez' OR
   first_name IN ('Ann','Anne','Annie') OR
   first_name LIKE 'Do%'OR
   first_name LIKE 'A%') AND
   LENGTH(first_name) BETWEEN 3 AND 4
ORDER BY 
	first_name,
	last_name DESC;  -- ASC used as default/ DESC

# Select 5 first rows with offset of 5 rows
SELECT
    film_id,
    title
FROM
    film
ORDER BY
    title 
OFFSET 5 ROWS 
FETCH FIRST 5 ROW ONLY; 


# Select Set of the pairs. All combination is considered. Result - two cols table.
SELECT
   DISTINCT bcolor,
   fcolor
FROM
   t1
ORDER BY
   bcolor,
   fcolor;


# Remove duplicates in pairs eg.: red-blue/blue-red
SELECT
   DISTINCT ON
   (bcolor) bcolor,
   fcolor
FROM
   t1
ORDER BY
   bcolor,
   fcolor;



value IN (value1,value2,...)
value IN (SELECT value FROM tbl_name);

SELECT
   customer_id,
   rental_id,
   return_date
FROM
   rental
WHERE
   customer_id NOT IN (1, 2);

#  The following query returns a list of customer id of customers that has rental’s return date on 2005-05-27:

SELECT
   customer_id
FROM
   rental
WHERE
   CAST (return_date AS DATE) = '2005-05-27';



#  Subquery
http://www.postgresqltutorial.com/postgresql-subquery/

SELECT
   film_id,
   title,
   rental_rate
FROM
   film
WHERE
   rental_rate > (	SELECT
   						AVG (rental_rate) -- This is 2.9. Subquery should be in parenteless.
					FROM
   						film)
ORDER by rental_rate DESC,
	title;


<<<<<<< HEAD
SELECT * 
FROM 
	actor 
WHERE first_name like '%e'
OFFSET 4
FETCH FIRST 2 ROWS ONLY;



# Group by

The GROUP BY clause must appear right after the FROM or WHERE clause. Followed by the GROUP BY clause is one column or a list of comma-separated columns. Beside the table column, you can also use an expression with the GROUP BY clause.
=======
# Syntax of USING:
# https://www.w3resource.com/PostgreSQL/postgresql-inner-join.php

SELECT [* | column_list]
FROM table1
INNER JOIN table2
ON table1.column_name=table2.column.name; 

# OR
# Syntax:
SELECT [* | column_list]
FROM table1
INNER JOIN table2
USING (column.name);

# OR
SELECT [* | column_list]
FROM table1,table2
WHERE table.column

# INNER JOIN play
SELECT
	*
FROM ((
	film_category
	INNER JOIN film
		USING(film_id)
	)
	INNER JOIN category 
		USING(category_id)
	)
WHERE name in ('SCi-Fi', 'Action')
ORDER by name
;


SELECT
	title,
	name,
	description,
	rental_duration,
	special_features,
	fulltext
	
FROM ((
	film_category
	INNER JOIN film
		USING(film_id)
	)
	INNER JOIN category 
		USING(category_id)
	)
WHERE (name in ('SCi-Fi','Action')) AND (rental_rate > 2.9)
ORDER by rental_duration DESC
OFFSET 20
FETCH FIRST 10 ROW ONLY
;
	

# Serial Join of four tables to get actor_name, film_title, rental_duration in one table 
SELECT
	title,
	first_name || '  ' || last_name,
	name,
	description,
	rental_duration,
	special_features,
	fulltext
	
FROM ((((
	film_category
	INNER JOIN film
		USING(film_id)
	)
	INNER JOIN category 
		USING(category_id)
	)
	INNER JOIN film_actor 
	  	USING(film_id)
	)
	INNER JOIN actor 
	  	USING(actor_id)  
	)
WHERE (name in ('SCi-Fi','Action')) AND (rental_rate > 2.9)
ORDER by rental_duration DESC
OFFSET 10
FETCH FIRST 10 ROW ONLY
;

=========================================
# cur = conn.cursor()
# cur.execute('''CREATE TABLE COMPANY
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       ADDRESS        CHAR(50),
#       SALARY         REAL);''')
# print("Table created successfully")

# cur = conn.cursor()
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )")
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
# conn.commit()

cur = conn.cursor()
sql = '''
SELECT * FROM COMPANY;
'''
cur.execute(sql)
rows = cur.fetchall()
print('Database contains {} records'.format(len(rows)))
for row in rows:
    print(row)
print("Records created successfully")
