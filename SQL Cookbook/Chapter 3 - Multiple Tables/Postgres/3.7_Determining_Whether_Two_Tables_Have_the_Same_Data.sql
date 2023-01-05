drop function if exists is_bigger;

create function is_bigger() 
returns table(
    empno emp.empno%type, 
    ename emp.ename%type,
    job emp.job%type, 
    mgr emp.mgr%type, 
    hiredate emp.hiredate%type, 
    sal emp.sal%type, 
    comm emp.comm%type, 
    deptno emp.deptno%type
) as $$
declare
    rows_counter1 integer;
    rows_counter2 integer;
begin
    
    -- Count the numer of rows in each tables
    SELECT COUNT(*) FROM V into rows_counter1;
    SELECT COUNT(*) FROM emp into rows_counter2;
    
    -- return the difference between the tables
    if rows_counter1 > rows_counter2 then
        return query 
        select * from V
        except
        select * from emp;
    else
        return query 
        select * from emp
        except
        select * from V;
    end if;
    
end $$
language plpgsql;


select *
from is_bigger();


/*
7934	"MILLER"	"CLERK"	7782	"1982-01-23"	1300		10
7839	"KING"	"PRESIDENT"		"1981-11-17"	5000		10
7782	"CLARK"	"MANAGER"	7839	"1981-06-09"	2450		10
*/
