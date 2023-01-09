select tablename
from pg_tables
where schemaname = 'public';

/*
"tablename"
"emp"
"dept"
"t1"
"t10"
"t100"
"emp_bonus"
"d"
"d2"
"d3"
"dept2"
"emp_commission"
*/

-- In the Shell:
/*

sql_cookbook-# \dt

             List of relations
 Schema |      Name      | Type  |  Owner
--------+----------------+-------+----------
 public | d              | table | postgres
 public | d2             | table | postgres
 public | d3             | table | postgres
 public | dept           | table | postgres
 public | dept2          | table | postgres
 public | emp            | table | postgres
 public | emp_bonus      | table | postgres
 public | emp_commission | table | postgres
 public | t1             | table | postgres
 public | t10            | table | postgres
 public | t100           | table | postgres
(11 rows)
*/






