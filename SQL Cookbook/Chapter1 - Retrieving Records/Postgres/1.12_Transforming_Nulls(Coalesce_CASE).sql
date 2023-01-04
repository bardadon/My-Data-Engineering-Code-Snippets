-- Transforming nulls using COALESCE
select 
    coalesce(comm, 0)
from emp
limit 5;

/*
"coalesce"
0
300
500
0
1400
0
0
0
0
0
0
0
0
0
*/

-- Transforming nulls using CASE
select 
    case
        when comm is null then 0
        else comm
    end as comm
from emp;


/* Discussion

- Coalesce replaces null values with an argument. In this case, with 0.
*/

