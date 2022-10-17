### Load Data
```
drop table if exists activity;
create table activity(player_id int, device_id int,event_date date,games_played int);

start transaction;
insert into activity(player_id , device_id ,event_date ,games_played)
values
(1         , 2         , '2016-03-01' , 5 );

insert into activity(player_id , device_id ,event_date ,games_played)
values
(1         , 2         , '2016-05-02' , 6 );

insert into activity(player_id , device_id ,event_date ,games_played)
values
(2         , 3         , '2017-06-25' , 1   );

insert into activity(player_id , device_id ,event_date ,games_played)
values
(3         , 1         , '2016-03-02' , 0 );

insert into activity(player_id , device_id ,event_date ,games_played)
values
(3         , 4         , '2018-07-03' , 5 );
commit;
```
### Solution
```
select 
	a1.player_id,
    min(a1.event_date) as first_login
from activity as a1
group by a1.player_id;
```
### Output
```
+-----------+-------------+
| player_id | first_login |
+-----------+-------------+
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
+-----------+-------------+
```
