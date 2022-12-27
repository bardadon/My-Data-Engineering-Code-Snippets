# Triangular Treasure

```
Triangular numbers are so called because of the equilateral triangular shape that they occupy when laid out as dots. i.e.
1st (1)   2nd (3)    3rd (6)
*          **        ***
           *         **
                     *
You need to return the nth triangular number. You should return 0 for out of range values:

```


```
drop function if exists calculate_n_triangle;
create function calculate_n_triangle(n integer) 
returns integer as $$
begin

  if n <= 0 then
    return 0;
  end if;
  
  if n = 1 then
    return 1;
  end if;
  
  return n * (n + 1) / 2;
  
end;
$$ language plpgsql;


select calculate_n_triangle(n)
from triangular;
```
