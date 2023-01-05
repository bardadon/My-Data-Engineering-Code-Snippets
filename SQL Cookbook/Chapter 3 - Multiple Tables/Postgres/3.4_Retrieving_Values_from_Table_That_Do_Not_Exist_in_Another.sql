-- Method #1 - subquery
select *
from dept
where deptno not in (select deptno from emp);

-- Method #1 - Set Theory(except)
select deptno
from dept

except

select deptno 
from emp;

/*
"deptno"
40
*/