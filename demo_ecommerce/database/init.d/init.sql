CREATE USER 'utente' identified by 'password';
GRANT ALL PRIVILEGES ON * . * TO 'utente';
FLUSH PRIVILEGES;

-- CREATE TABLE COSI(
--     id int NOT NULL AUTO_INCREMENT,
--     name varchar(255),
--     primary key (id)
