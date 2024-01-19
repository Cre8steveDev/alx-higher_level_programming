-- Creating a New User on the MySQL Server
-- syntax: CREATE USER '<username>'@'<localhost or ip address>' IDENTIFIED BY '<password>';

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';