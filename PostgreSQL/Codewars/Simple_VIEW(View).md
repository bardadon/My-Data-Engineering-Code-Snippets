# SQL Basics: Simple VIEW

## Question

```
For this challenge you need to create a VIEW. This VIEW is used by a sales store to give out vouches to members who have spent over $1000 in departments that have brought in more than $10000 total ordered by the members id. The VIEW must be called members_approved_for_voucher then you must create a SELECT query using the view.
Tables and relationship below:
resultant table schema

    id
    name
    email
    total_spending
```
## Solution

```
-- Create your VIEW statement here

create or replace view members_approved_for_voucher as
select 
  m.id,
  m.name,
  m.email,
  sum(p.price) as total_spending
from sales as s
join members as m on
  s.member_id = m.id
join products as p on
  p.id = s.product_id
where s.department_id in (
  
-- departments that have brough in more than 10K
    select 
      department_id
    from sales as s
    join departments as d on
      s.department_id = d.id
    join products as p on
      s.product_id = p.id
    group by 
      department_id
    having 
      sum(p.price) > 10000
)
group by 
  m.id,
  m.name
having sum(p.price) > 1000
order by m.id;

select *
from members_approved_for_voucher;
```
## Output
```
id	name	email	total_spending
2	Ms. Roxanne Towne	noelia@bins.org	1117.66
5	Beth Wintheiser	raul.hermann@christiansen.org	1275.56
12	Colten Daugherty	maxwell_durgan@denesikharris.io	1753.16
18	Chaim Armstrong	hilbert@torpmedhurst.biz	1048.57
20	Hildegard Will	irma.crooks@strosinhickle.io	1039.16
22	Philip Erdman	darion_crist@pagac.co	1087.45
27	Catalina Goodwin	gina@collierbins.name	1171.97
```
