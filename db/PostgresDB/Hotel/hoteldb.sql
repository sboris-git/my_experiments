--DROP DATABASE "Hotel"
--CREATE DATABASE "Hotel_1";

CREATE TABLE IF NOT EXISTS hotels(
	hotel_Id serial PRIMARY KEY, 
	hotel_name VARCHAR(255), 
	foundation_year DATE,
	address VARCHAR(255), 
	is_active BOOLEAN);


CREATE TABLE IF NOT EXISTS rooms
(	
	room_Id serial PRIMARY KEY, 
	room_name INT, 
	price INT,
	comfort_Id INT,
	FOREIGN KEY (comfort_Id) REFERENCES comfort (comfort_Id) on DELETE CASCADE,
	FOREIGN KEY (comfort_Id) REFERENCES comfort (comfort_Id) on UPDATE CASCADE,
	capability INT, 
	hotel_Id INT,
	FOREIGN KEY (hotel_Id) REFERENCES hotels (hotel_Id) on UPDATE CASCADE,
	FOREIGN KEY (hotel_Id) REFERENCES hotels (hotel_Id) on DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS users
(	
	user_Id serial PRIMARY KEY, 
	username varchar(50), 
	email varchar(50) 
);

CREATE TABLE IF NOT EXISTS reservation
(	
	reservation_Id serial PRIMARY KEY, 
	date_of_reservation DATE, 
	user_Id INT,
	room_Id INT,
	FOREIGN KEY (user_Id) REFERENCES users (user_Id) on DELETE CASCADE,
	FOREIGN KEY (user_Id) REFERENCES users (user_Id) on UPDATE CASCADE,
	start_date_reservation DATE, 
	end_date_reservation DATE,
	FOREIGN KEY (room_Id) REFERENCES rooms (room_Id) on UPDATE CASCADE,
	FOREIGN KEY (room_Id) REFERENCES rooms (room_Id) on DELETE CASCADE 
);

--3
--https://www.postgresql.org/docs/9.4/functions-datetime.html
UPDATE hotels
SET foundation_year = (make_date(1937, date_part('MONTH', hotels.foundation_year)::INT, 
						date_part('DAY', hotels.foundation_year)::INT))
WHERE hotel_Id = ( 
SELECT h.hotel_Id
FROM hotels h
WHERE date_part('YEAR', h.foundation_year) = (SELECT MIN(date_part('YEAR', hotels.foundation_year)) FROM hotels));

--4
DELETE FROM hotels WHERE hotel_Id=3;

--6
SELECT * FROM users WHERE username LIKE 'A%';

--7
--INSERT INTO rooms(room_name, price, comfort_Id, capability, hotel_Id) 
--VALUES(1202,450.00,4,5,2),(1204,290.00,2,3,2),(1205,500.00,1,5,2);
 

INSERT INTO rooms(room_name, price, comfort_Id, capability, hotel_Id)
VALUES
	('101', '50',
	 (SELECT comfort_Id FROM rooms WHERE comfort_Id=2),
	 '3', 
	 (SELECT hotel_Id FROM hotels WHERE hotel_Id=1)),
	('301', '50',
	 (SELECT comfort_Id FROM rooms WHERE comfort_Id=2),
	 '3', 
	 (SELECT hotel_Id FROM hotels WHERE hotel_Id=1)),
	('103', '50', 
	 (SELECT comfort_Id FROM rooms WHERE comfort_Id=2),
	 '3', 
	 (SELECT hotel_Id FROM hotels WHERE hotel_Id=1)),
	('103', '50',
	 (SELECT comfort_Id FROM rooms WHERE comfort_Id=2),
	 '3', 
	 (SELECT hotel_Id FROM hotels WHERE hotel_Id=1)),
	('104', '50',
	 (SELECT comfort_Id FROM rooms WHERE comfort_Id=2),
	 '3', 
	 (SELECT hotel_Id FROM hotels WHERE hotel_Id=1)),
	('105', '50',
	 (SELECT comfort_Id FROM rooms WHERE comfort_Id=2),
	 '3', 
	 (SELECT hotel_Id FROM hotels WHERE hotel_Id=1)),
	('106', '50',
	 (SELECT comfort_Id FROM rooms WHERE comfort_Id=2),
	 '3', 
	 (SELECT hotel_Id FROM hotels WHERE hotel_Id=1)),
	
	('101', '50', 
	 (SELECT comfort_Id FROM rooms WHERE comfort_Id=3),
	 '3', 
	 (SELECT hotel_Id FROM hotels WHERE hotel_Id=3)),
	('103', '50', 
	 (SELECT comfort_Id FROM rooms WHERE comfort_Id=1),
	 '3', 
	 (SELECT hotel_Id FROM hotels WHERE hotel_Id=1)),
	('103', '50', 
	 (SELECT comfort_Id FROM rooms WHERE comfort_Id=3),
	 '3', 
	 (SELECT hotel_Id FROM hotels WHERE hotel_Id=2))
;

--8
SELECT * FROM rooms ORDER BY price;

--9
SELECT 
	room_name, price
FROM
	hotels
NATURAL JOIN rooms	
WHERE hotel_name = 'Edelweiss'
ORDER BY price;

--10
SELECT 
	room_name, price, comfort_level
FROM
	(hotels NATURAL JOIN rooms)
NATURAL JOIN comfort
WHERE comfort_level = 3
ORDER BY price;

--11
SELECT 
	hotel_name, room_name, comfort_level
FROM
	(hotels NATURAL JOIN rooms)
NATURAL JOIN comfort
WHERE comfort_level = 1
ORDER BY price;

--12
SELECT 
	hotel_name, COUNT(*)
FROM
	hotels NATURAL JOIN rooms
GROUP BY hotel_name
;

--13
INSERT INTO reservation (date_of_reservation, user_Id, room_id, start_date_reservation, end_date_reservation)
VALUES
('11-11-2011', 1, 11, '02-02-2002', '04-02-2002'),
('05-06-2007', 2, 12, '01-02-2003', '02-02-2003'),
('04-05-2006', 3, 13, '15-09-2006', '18-09-2006'),
('07-08-2009', 4, 14, '27-08-2009', '02-09-2009'),
('10-11-2012', 5, 15, '12-11-2012', '13-11-2012'),
('23-12-2015', 6, 16, '25-12-2015', '26-12-2015'),
('26-07-2019', 7, 17, '26-07-2019', '27-07-2019'),
('18-03-2018', 8, 16, '20-03-2018', '21-03-2018'),
('13-02-2015', 9, 15, '20-02-2015', '25-02-2015'),
('09-09-2009', 10, 14, '10-09-2009', '11-09-2009')
;

--14
--Select Username, room number, reservation period.
SELECT username, room_name, end_date_reservation-start_date_reservation AS reservation_duration
FROM rooms
NATURAL JOIN reservation
NATURAL JOIN users
;

