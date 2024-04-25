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
    name VARCHAR(100),
    mobile VARCHAR(20),
    email VARCHAR(100),
    address VARCHAR(200)
);
-- Comment on the "contacts" table
COMMENT ON TABLE contacts IS 'Table containing Agent-level contact data. Each agent has their own contacts list. Contacts can be duplicated between agents.';
-- Comment on the "name" column
COMMENT ON COLUMN contacts.name IS 'Contact''s full name';
-- Comment on the "mobile" column
COMMENT ON COLUMN contacts.mobile IS 'Contact''s personal mobile number';
-- Comment on the "email" column
COMMENT ON COLUMN contacts.email IS 'Contact''s personal email address';
-- Comment on the "address" column
COMMENT ON COLUMN contacts.address IS 'Contact''s current home address';
