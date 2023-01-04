select 
    e.ename,
    e.sal,
    e.job,
    e.comm
from emp as e
order by 
        case
            when e.job = 'SALESMAN' then e.comm
            else e.sal
        end
limit 5;

/*
"ename"	"sal"	"job"	"comm"
"TURNER"	1500	"SALESMAN"	0
"ALLEN"	1600	"SALESMAN"	300
"WARD"	1250	"SALESMAN"	500
"SMITH"	800	"CLERK"	
"JAMES"	950	"CLERK"	
*/