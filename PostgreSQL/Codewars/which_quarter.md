# Quarter of the year

```
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
```

```
SELECT month, 
       CASE
        WHEN month <= 3  THEN 1
        WHEN month <= 6  THEN 2
        WHEN month <= 9  THEN 3
        WHEN month <= 12 THEN 4
      END AS res
  FROM quarterof
```
