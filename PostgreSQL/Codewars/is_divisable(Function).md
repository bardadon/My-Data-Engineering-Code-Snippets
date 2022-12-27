# Is n divisible by x and y?
```
Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero numbers.
```

```
CREATE OR REPLACE FUNCTION is_divisible(n INTEGER, x INTEGER, y INTEGER)
RETURNS BOOLEAN AS $$
BEGIN
    IF n % x = 0 AND n % y = 0 THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END;
$$ LANGUAGE plpgsql;

SELECT id, is_divisible(n, x, y) as res
FROM kata;
```

```
id	res
1	false
2	true
3	true
4	false
5	false
6	false
7	true
8	false
9	true
10	false
```
