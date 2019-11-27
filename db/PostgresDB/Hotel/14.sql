--Select Username, room number, reservation period.
SELECT username, r.room_name, re.start_date_reservation, re.end_date_reservation 
FROM 
	(SELECT 
		* 
	 FROM 
		rooms r
	 NATURAL JOIN reservation re)
NATURAL JOIN users
;