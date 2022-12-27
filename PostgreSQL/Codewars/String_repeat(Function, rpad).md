# String repeat
```
Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
Examples (input -> output)

6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"

```


```
--# write your SQL statement here: you are given a table 'repeatstr' with columns 'n' and 's', return a table with all columns and your result in a column named 'res'


create or replace function multiplyString(n integer, s varchar(30)) 
returns varchar(30) as $$
begin

  if length(s) = n then
    return s;
  else
    return rpad(s, n*length(s), s);
  end if;
  
end;
$$ language plpgsql;


select r.s,
        r.n,
       multiplyString(n, s) as res
from repeatstr as r;
```


