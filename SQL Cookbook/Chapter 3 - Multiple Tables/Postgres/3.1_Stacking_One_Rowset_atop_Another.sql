select ename, deptno
from emp
where deptno = 10

union

select dname, deptno
from dept
order by deptno;

/*
"ename"	"deptno"
"KING"	10
"MILLER"	10
"ACCOUNTING"	10
"CLARK"	10
"RESEARCH"	20
"SALES"	30
"OPERATIONS"	40
*/

-- Organizing the results

select ename as ename_and_dname, deptno
from emp
where deptno = 10

union all

select '----------', null
from t1

union all

select dname, deptno
from dept

/* Discussion
1. UNION combines two rows tables WITHOUT duplicates.
2. To keep the duplicates, use UNION ALL
3. To use UNION, you need that the columns of both tables have the same order, type
*/




