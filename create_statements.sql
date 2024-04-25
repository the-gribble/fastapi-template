
CREATE TABLE contacts (
	id BIGINT GENERATED ALWAYS AS IDENTITY (START WITH 1), 
	name VARCHAR, 
	mobile VARCHAR, 
	email VARCHAR, 
	address VARCHAR, 
	PRIMARY KEY (id)
)



CREATE TABLE users (
	id BIGINT GENERATED ALWAYS AS IDENTITY (START WITH 1), 
	username VARCHAR, 
	email VARCHAR, 
	password VARCHAR, 
	first_name VARCHAR, 
	last_name VARCHAR, 
	PRIMARY KEY (id)
)

