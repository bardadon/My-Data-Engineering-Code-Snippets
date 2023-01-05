select 
    e1.ename,
    d.loc,
    e2.received
from emp as e1
join dept as d on
    e1.deptno = d.deptno
left join emp_bonus as e2 on
    e1.empno = e2.empno
    
/*
"ename"	"loc"	"received"
"SMITH"	"DALLAS"	"2005-03-14"
"ALLEN"	"CHICAGO"	
"WARD"	"CHICAGO"	
"JONES"	"DALLAS"	
"MARTIN"	"CHICAGO"	
"BLAKE"	"CHICAGO"	
"CLARK"	"NEW YORK"	
"SCOTT"	"DALLAS"	"2005-03-14"
"KING"	"NEW YORK"	
"TURNER"	"CHICAGO"	
"ADAMS"	"DALLAS"	
"JAMES"	"CHICAGO"	"2005-03-14"
"FORD"	"DALLAS"	
"MILLER"	"NEW YORK"	
*/