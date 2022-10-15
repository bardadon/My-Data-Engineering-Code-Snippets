### Solution
```
DELIMITER //
drop function if exists getNthHighestSalary //

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT deterministic
BEGIN
    SET N = N - 1;
  RETURN (
      SELECT DISTINCT(salary)
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N
      
  );
END
//
DELIMITER ;
```

```
select getNthHighestSalary(2);
```

### Output
```
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
```

