select 
    sal as Salary,
    case
        when sal <= 2000 then 'UNDERPAID'
        when sal >= 4000 then 'OVERPAID'
        else 'OK'
    end as status
from emp;

/*
"salary"	"status"
800	"UNDERPAID"
1600	"UNDERPAID"
1250	"UNDERPAID"
2975	"OK"
1250	"UNDERPAID"
2850	"OK"
2450	"OK"
3000	"OK"
5000	"OVERPAID"
1500	"UNDERPAID"
1100	"UNDERPAID"
950	"UNDERPAID"
3000	"OK"
1300	"UNDERPAID"
*/