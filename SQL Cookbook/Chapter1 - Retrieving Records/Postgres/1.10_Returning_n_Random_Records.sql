select *
from emp
order by Random()
limit 5;

/*
"empno"	"ename"	"job"	"mgr"	"hiredate"	"sal"	"comm"	"deptno"
7839	"KING"	"PRESIDENT"		"1981-11-17"	5000		10
7566	"JONES"	"MANAGER"	7839	"1981-04-02"	2975		20
7788	"SCOTT"	"ANALYST"	7566	"1982-12-09"	3000		20
7900	"JAMES"	"CLERK"	7698	"1981-12-03"	950		30
7902	"FORD"	"ANALYST"	7566	"1981-12-03"	3000		20
*/