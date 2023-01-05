-- Method 1 - Inner join
select 
    e.empno,
    V.*,
    e.deptno
from V
join emp as e on
    V.ename = e.ename;
    
    
-- Method 2 - Sub query
select *
from emp
where (ename, job, sal) in (
                           select ename, job, sal
                           from V
                            );
                            
/*
"empno"	"ename"	"job"	"mgr"	"hiredate"	"sal"	"comm"	"deptno"
7369	"SMITH"	"CLERK"	7902	"1980-12-17"	800		20
7876	"ADAMS"	"CLERK"	7788	"1983-01-12"	1100		20
7900	"JAMES"	"CLERK"	7698	"1981-12-03"	950		30
7934	"MILLER"	"CLERK"	7782	"1982-01-23"	1300		10
*/