select *
from pg_tables
where tablename = 'emp'

-- OR 

select column_name, data_type, ordinal_position
from information_schema.columns
where table_schema = 'public' and table_name = 'emp';

/*
"empno"	"integer"	1
"ename"	"character varying"	2
"job"	"character varying"	3
"mgr"	"integer"	4
"hiredate"	"date"	5
"sal"	"integer"	6
"comm"	"integer"	7
"deptno"	"integer"	8
*/





-- Shell

/*

sql_cookbook-# \d emp
                        Table "public.emp"
  Column  |         Type          | Collation | Nullable | Default
----------+-----------------------+-----------+----------+---------
 empno    | integer               |           | not null |
 ename    | character varying(10) |           |          |
 job      | character varying(9)  |           |          |
 mgr      | integer               |           |          |
 hiredate | date                  |           |          |
 sal      | integer               |           |          |
 comm     | integer               |           |          |
 deptno   | integer               |           |          |
 
 */