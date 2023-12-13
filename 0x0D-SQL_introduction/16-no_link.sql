-- This script lists all records with names from 'second_table'
SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;
