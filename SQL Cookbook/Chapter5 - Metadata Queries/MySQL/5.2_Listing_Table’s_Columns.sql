select column_name, data_type, ordinal_position
from information_schema.columns
where table_schema = 'playground' and table_name = 'emp';

/*
COMM	int	7
DEPTNO	int	8
EMPNO	int	1
ENAME	varchar	2
HIREDATE	date	5
JOB	varchar	3
MGR	int	4
SAL	int	6
*/