### Load Data
```
Create table If Not Exists orders (order_number int, customer_number int);
insert into orders (order_number, customer_number) values ('1', '1');
insert into orders (order_number, customer_number) values ('2', '2');
insert into orders (order_number, customer_number) values ('3', '3');
insert into orders (order_number, customer_number) values ('4', '3');
```
### Solution
```
select 
	o.customer_number
from orders as o
group by 
	o.customer_number 
order by count(*) desc
limit 1;
```
### Output
```
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+
```
