select *
from emp
where coalesce(comm,0) < (select comm
                         from emp 
                         where ename = 'WARD');
                         
/*
"empno"	"ename"	"job"	"mgr"	"hiredate"	"sal"	"comm"	"deptno"
7369	"SMITH"	"CLERK"	7902	"1980-12-17"	800		20
7499	"ALLEN"	"SALESMAN"	7698	"1981-02-20"	1600	300	30
7566	"JONES"	"MANAGER"	7839	"1981-04-02"	2975		20
7698	"BLAKE"	"MANAGER"	7839	"1981-05-01"	2850		30
7782	"CLARK"	"MANAGER"	7839	"1981-06-09"	2450		10
7788	"SCOTT"	"ANALYST"	7566	"1982-12-09"	3000		20
7839	"KING"	"PRESIDENT"		"1981-11-17"	5000		10
7844	"TURNER"	"SALESMAN"	7698	"1981-09-08"	1500	0	30
7876	"ADAMS"	"CLERK"	7788	"1983-01-12"	1100		20
7900	"JAMES"	"CLERK"	7698	"1981-12-03"	950		30
7902	"FORD"	"ANALYST"	7566	"1981-12-03"	3000		20
7934	"MILLER"	"CLERK"	7782	"1982-01-23"	1300		10
*/

/* Discussion:
1. Return all employee that have comm less than the comm of an employee named "WARD".
2. Use coalesce to convert null values into 0, so that they will be included in the result.
*/