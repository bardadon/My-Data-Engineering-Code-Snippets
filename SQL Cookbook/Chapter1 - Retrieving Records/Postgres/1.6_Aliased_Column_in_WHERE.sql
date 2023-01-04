-- Wrong
select 
    ename as Employee_Name,
    deptno as Deptartment_NUmber,
    sal as Salary
from emp
where Deptartment_NUmber = 20;

-- Correct
select *
from
(
    select 
        ename as Employee_Name,
        deptno as Deptartment_NUmber,
        sal as Salary
    from emp
) as aaa
where Deptartment_NUmber = 20;

/* Discussion
1. The WHERE clause is evaluated before the SELECT. 
That is why Postgres does not know that "Deptartment_NUmber" is an alias for deptno in the first query.

2. However, FROM is evaluated before WHERE.
That is why Postgres is able to detect the inner query before "where Deptartment_NUmber = 20;"
*/




