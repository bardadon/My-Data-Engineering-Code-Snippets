-- Nulls last
select *
from emp
order by
    comm asc;

-- Nulls first
select *
from emp
order by
    comm desc;