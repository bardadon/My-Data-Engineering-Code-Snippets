-- Generating SQL queries with SQL

-- 1. count the number of rows in your
select 'select count(*) from ' || tablename || ';' as sql_queries
from pg_tables
where schemaname = 'public'
limit 5;

/*
"select count(*) from emp;"
"select count(*) from dept;"
"select count(*) from t1;"
"select count(*) from t10;"
"select count(*) from t100;"
*/


-- 2. tables, disable foreign key constraints defined on your tables, and 

select 'alter table ' || table_name || ' disable constraint ' || constraint_name || ';' as sql_queries
from information_schema.key_column_usage
where 
    constraint_catalog = 'sql_cookbook' and 
    constraint_schema = 'public';
 
/*
"alter table emp_bonus disable constraint emp_bonus_pkey;"
"alter table emp_commission disable constraint emp_commission_pkey;"
*/
    
    
-- 3. generate insert scripts from the data in your tables.
select 'insert into emp(empno,ename,hiredate) '||chr(10)||
'values( '||empno||','||''''||ename
||''',to_date('||''''||hiredate||''') );' as insert_queries
from emp
where deptno = 10;

/*
"insert into emp(empno,ename,hiredate) 
values( 7782,'CLARK',to_date('1981-06-09') );"
"insert into emp(empno,ename,hiredate) 
values( 7839,'KING',to_date('1981-11-17') );"
"insert into emp(empno,ename,hiredate) 
values( 7934,'MILLER',to_date('1982-01-23') );"
*/

