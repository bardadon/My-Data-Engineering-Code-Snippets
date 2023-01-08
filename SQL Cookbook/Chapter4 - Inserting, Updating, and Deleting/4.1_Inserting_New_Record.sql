-- 1. Single insert
create table D3 (id integer);
INSERT INTO D3 values(1);

-- 2. Multi insert
INSERT INTO D3 values(1),(2),(3),(4);


-- 3. Insert with default 
create table D1 (id integer default 0);
INSERT INTO D1 values(default);

select *
from D1;
/*
"id"
0
*/


create table D2 (id integer default 0, age integer default 0, name varchar(20));
INSERT INTO D2(id, age, name) values(default, default, 'Bar');

select *
from D2;

/*
"id"	"age"	"name"
0	0	"Bar"
*/

-- 4. Copying Rows from One Table into Another
insert into dept(deptno,dname,loc)
select deptno,dname,loc
from dept
where loc in ( 'NEW YORK','BOSTON' );

    
