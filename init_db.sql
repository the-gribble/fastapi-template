-- Just run the create table code

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id bigserial PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
);

-- Comment on the "users" table
COMMENT ON TABLE users IS 'Table containing system user data across functional areas of the system. Roles are used to control access to the funcitonal areas.';
-- Comment on the "username" column
COMMENT ON COLUMN users.username IS 'Globally unique system user identifier (and agent can change email address frequently).';
-- Comment on the "username" column
COMMENT ON COLUMN users.email IS 'Personal email address that can be changed frequently (e.g. when agents often change brokerages).';

DROP TABLE IF EXISTS contacts;
CREATE TABLE contacts (
    id bigserial PRIMARY KEY,
    full_name VARCHAR(100),
    mobile_no VARCHAR(20),
    email VARCHAR(100),
    current_address VARCHAR(200)
);
-- Comment on the "contacts" table
COMMENT ON TABLE contacts IS 'Table containing Agent-level contact data. Each agent has their own contacts list. Contacts can be duplicated between agents.';
-- Comment on the "name" column
COMMENT ON COLUMN contacts.full_name IS 'Contact''s full name';
-- Comment on the "mobile" column
COMMENT ON COLUMN contacts.mobile_no IS 'Contact''s personal mobile number';
-- Comment on the "email" column
COMMENT ON COLUMN contacts.email IS 'Contact''s personal email address';
-- Comment on the "address" column
COMMENT ON COLUMN contacts.current_address IS 'Contact''s current home address';


--------------------------
-- Create a new user with a password and the LOGIN privilege
CREATE ROLE sa_ahs_db WITH LOGIN PASSWORD 'Password123#';
GRANT CONNECT ON DATABASE mydatabase TO sa_ahs_db;
-- Grant all privileges to the new user on a specific database
-- GRANT ALL PRIVILEGES ON DATABASE mydatabase TO sa_ahs_db; -- this doesn't do anything
-- Change the owner of the database to the new user
ALTER DATABASE mydatabase OWNER TO sa_ahs_db; -- db restart required
-- Grant specific roles to existing objects (this works)
GRANT ALL ON SEQUENCE public.contacts_id_seq TO sa_ahs_db;
GRANT ALL ON SEQUENCE public.users_id_seq TO sa_ahs_db;
GRANT ALL ON TABLE public.contacts TO sa_ahs_db;
GRANT ALL ON TABLE public.users TO sa_ahs_db;

-- list users
SELECT usename AS role_name,
  CASE 
     WHEN usesuper AND usecreatedb THEN 
	   CAST('superuser, create database' AS pg_catalog.text)
     WHEN usesuper THEN 
	    CAST('superuser' AS pg_catalog.text)
     WHEN usecreatedb THEN 
	    CAST('create database' AS pg_catalog.text)
     ELSE 
	    CAST('' AS pg_catalog.text)
  END role_attributes
FROM pg_catalog.pg_user
ORDER BY role_name desc;

SELECT usename, usesuper FROM pg_user WHERE usename = current_user;

-- Check permissions
SELECT table_catalog, table_schema, table_name, privilege_type
FROM   information_schema.table_privileges 
WHERE  grantee = 'sa_ahs_db'
and table_name in ('users', 'contacts')

SELECT users.id AS users_id, users.username AS users_username, users.email AS users_email, users.password AS users_password, users.first_name AS users_first_name, users.last_name AS users_last_name 
FROM users 
WHERE users.username = 'sam'
