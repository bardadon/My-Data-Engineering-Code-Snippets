select 
    e.ename,
    d.loc
from emp as e
join dept as d on
    e.deptno = d.deptno 
where 
    e.deptno = 10;

/*
"ename"	"loc"
"CLARK"	"NEW YORK"
"KING"	"NEW YORK"
"MILLER"	"NEW YORK"
*/

    
/* Discussion
1. This is an example of an inner join.
2. Conceptually, the result set from a join is produced by first creating a catesian product of both tables, and then filtering for e.deptno = d.deptno.

Lets check and example:
*/

-- First, the catesian product:
select ename, loc
from emp as e
cross join dept  as d
where e.deptno = 10;

-- Second, filtering e.deptno = d.deptno
select ename, loc
from emp as e
cross join dept  as d
where 
    e.deptno = 10 and
    e.deptno = d.deptno

/*
"ename"	"loc"
"CLARK"	"NEW YORK"
"KING"	"NEW YORK"
"MILLER"	"NEW YORK"
*/



