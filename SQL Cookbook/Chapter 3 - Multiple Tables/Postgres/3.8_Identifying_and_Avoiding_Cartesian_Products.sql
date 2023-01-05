select e.ename, d.loc
from emp e
join dept d on
 d.deptno = e.deptno
where e.deptno = 10

/*
"ename"	"loc"
"CLARK"	"NEW YORK"
"KING"	"NEW YORK"
"MILLER"	"NEW YORK"
*/
