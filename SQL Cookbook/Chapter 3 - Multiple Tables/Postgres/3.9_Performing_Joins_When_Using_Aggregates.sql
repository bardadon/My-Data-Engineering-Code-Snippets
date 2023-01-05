select 
    deptno,
    sum(bonus)
from
    (
    select 
        e1.empno,
        e1.ename,
        e1.sal,
        e1.deptno,
        case
            when e2.type = 1 then 0.1*e1.sal
            when e2.type = 2 then 0.2*e1.sal
            when e2.type = 3 then 0.3*e1.sal
        end as bonus
    from emp as e1
    join emp_bonus as e2 on
        e1. empno = e2.empno
    ) as aaa
group by 
    deptno;
    
/*
"deptno"	"sum"
30	190.0
20	980.0
*/

    
    

