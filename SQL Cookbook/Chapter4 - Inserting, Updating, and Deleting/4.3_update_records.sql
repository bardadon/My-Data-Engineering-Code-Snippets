select sal
from emp
where empno = 7369;

/*
800
*/

update emp 
set sal = sal * 1.2
where deptno = 20;

select sal
from emp
where empno = 7369;

/*
960
*/

/* Tip:
To prepare for a large/sensitive update, 
we can run a select query to check how the update would look like. 
For example:
*/


select  deptno,
        ename,
        sal as orig_sal,
        sal*.20 as amt_to_add,
        sal*1.20 as new_sal
from emp
where deptno=20
order by new_sal











