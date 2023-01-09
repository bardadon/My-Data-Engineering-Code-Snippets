CREATE INDEX Employee_name
ON emp (ename);

select a.tablename,a.indexname,b.column_name
from pg_catalog.pg_indexes a, information_schema.columns b
where a.schemaname = 'public' and a.tablename = b.table_name;

/*
"tablename"	"indexname"	"column_name"
"emp_bonus"	"emp_bonus_pkey"	"type"
"emp_bonus"	"emp_bonus_pkey"	"received"
"emp_bonus"	"emp_bonus_pkey"	"empno"
"emp"	"employee_name"	"deptno"
"emp"	"employee_name"	"comm"
"emp"	"employee_name"	"sal"
"emp"	"employee_name"	"hiredate"
"emp"	"employee_name"	"mgr"
"emp"	"employee_name"	"empno"
"emp_commission"	"emp_commission_pkey"	"comm"
"emp_commission"	"emp_commission_pkey"	"empno"
"emp_commission"	"emp_commission_pkey"	"deptno"
"emp"	"employee_name"	"ename"
"emp"	"employee_name"	"job"
"emp_commission"	"emp_commission_pkey"	"ename"
*/