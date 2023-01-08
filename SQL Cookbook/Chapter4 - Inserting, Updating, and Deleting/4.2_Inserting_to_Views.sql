-- 1. Inserting to views
create view restricted_info_emp as
select ename, job
from emp;

select *
from restricted_info_emp
limit 5;

/*
"ename"	"job"
"SMITH"	"CLERK"
"ALLEN"	"SALESMAN"
"WARD"	"SALESMAN"
"JONES"	"MANAGER"
"MARTIN"	"SALESMAN"
*/

-- 2. Inserting into the original table updates the view automatically
insert into emp
values (50, 'Bar', 'DE');

select *
from restricted_info_emp
where ename = 'Bar';


-- 3. Inserting into the view violates Postgres not-null constraint
insert into restricted_info_emp
values ('Yuval', 'SE');

select *
from emp
where ename = 'Yuval';


/* Discussion:
A good use case for views is to give restricted access to a table.
When we insert the original table, the view is updated automatically.
However, the other way around is not recommended.
*/

