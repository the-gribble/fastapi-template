
CREATE TABLE contacts (
	id BIGINT GENERATED ALWAYS AS IDENTITY (START WITH 1), 
	full_name VARCHAR, 
	mobile_no VARCHAR, 
	email VARCHAR, 
	current_address VARCHAR, 
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

