drop view if exists V;
create view V
as
select concat(ename, ' ', deptno) as data
from emp;

select * from V;

/*
"data"
"SMITH 20"
"ALLEN 30"
"WARD 30"
"JONES 20"
"MARTIN 30"
"BLAKE 30"
"CLARK 10"
"SCOTT 20"
"KING 10"
"TURNER 30"
"ADAMS 20"
"JAMES 30"
"FORD 20"
"MILLER 10"
*/

-- Sorting by name
select 
    V.*,
    substring(V.data, 0, length(V.data) - 3) as name,
    substring(V.data, length(V.data) - 2, length(V.data)) as department
from V
order by name
limit 5;

/*
"data"	"name"	"department"
"ADAMS 20"	"ADAM"	" 20"
"ALLEN 30"	"ALLE"	" 30"
"BLAKE 30"	"BLAK"	" 30"
"CLARK 10"	"CLAR"	" 10"
"FORD 20"	"FOR"	" 20"
*/


-- Sorting by department
select 
    V.*,
    substring(V.data, 0, length(V.data) - 3) as name,
    substring(V.data, length(V.data) - 2, length(V.data)) as department
from V
order by name
limit 5;

/*
"data"	"name"	"department"
"ADAMS 20"	"ADAM"	" 20"
"ALLEN 30"	"ALLE"	" 30"
"BLAKE 30"	"BLAK"	" 30"
"CLARK 10"	"CLAR"	" 10"
"FORD 20"	"FOR"	" 20"
*/





