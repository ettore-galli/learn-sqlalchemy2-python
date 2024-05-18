CREATE USER 'utente' identified by 'password';

GRANT ALL PRIVILEGES ON *.* TO 'utente';

FLUSH PRIVILEGES;