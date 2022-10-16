### Load Data
```
create table scores(id int, score decimal);

insert into scores(id, score) values (1, 3.5);
insert into scores(id, score) values (2, 3.65);
insert into scores(id, score) values (3, 4);
insert into scores(id, score) values (4, 3.85);
insert into scores(id, score) values (5, 4);
insert into scores(id, score) values (6, 3.65);
```
### Solution
```
select 
	s1.score, 
    count(*) as "rank"
from scores as s1, (select distinct score from scores) as s2
where s1.score <= s2.score
group by s1.id
order by s1.score desc;
```

### Output
```
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
 ```
