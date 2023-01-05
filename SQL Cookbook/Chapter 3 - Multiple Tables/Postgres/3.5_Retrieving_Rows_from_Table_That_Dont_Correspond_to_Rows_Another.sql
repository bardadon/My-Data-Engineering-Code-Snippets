select *
from dept as d
left join emp as e on
    d.deptno = e.deptno
where e.deptno is null;

/*
"deptno"	"dname"	"loc"	"empno"	"ename"	"job"	"mgr"	"hiredate"	"sal"	"comm"	"deptno-2"
40	"OPERATIONS"	"BOSTON"								
*/