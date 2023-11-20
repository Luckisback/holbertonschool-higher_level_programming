-- a script that converts hbtn_0c_0 database to UTF8

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; 

USE hbtn_0c_0;
-- modifying the character set and collation of the entire first_table

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- modify the character set and collation of the name in the field in the first_table
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
