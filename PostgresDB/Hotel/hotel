CREATE TABLE IF NOT EXISTS rooms
(	
	roomId serial PRIMARY KEY, 
	room_name INT, 
	price INT,
	comfortId INT,
	FOREIGN KEY (comfortId) REFERENCES comfort (comfortId) on DELETE CASCADE,
	FOREIGN KEY (comfortId) REFERENCES comfort (comfortId) on DELETE CASCADE,
	capability INT, 
	hotelID INT,
	FOREIGN KEY (hotelId) REFERENCES hotels (hotelId) on UPDATE CASCADE,
	FOREIGN KEY (hotelId) REFERENCES hotels (hotelId) on DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS users
(	
	userId serial PRIMARY KEY, 
	username varchar(50), 
	email varchar(50) 
);
