-- This script establishes the MySQL server user user_0d_1.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Refreshes privileges after creating a user or assigning permissions.
FLUSH PRIVILEGES;

-- Grants user_0d_1 full permissions across all databases and tables.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Refreshes privileges after granting permissions.
FLUSH PRIVILEGES;
