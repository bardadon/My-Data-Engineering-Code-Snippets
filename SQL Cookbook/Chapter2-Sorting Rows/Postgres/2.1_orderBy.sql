select 
    ename,
    job,
    sal
from emp
where 
    deptno = 10
order by sal;

/*
"ename"	"job"	"sal"
"MILLER"	"CLERK"	1300
"CLARK"	"MANAGER"	2450
"KING"	"PRESIDENT"	5000
*/

-- Other options:

--- Sorting in Descending
select 
    ename,
    job,
    sal
from emp
where 
    deptno = 10
order by sal desc;

--- Sorting by the location of the column in the select clause
select 
    ename,
    job,
    sal
from emp
where 
    deptno = 10
order by 3 desc;

--- Sorting by the multiple columns
select 
    ename,
    job,
    sal
from emp
where 
    deptno = 10
order by sal desc, job desc;