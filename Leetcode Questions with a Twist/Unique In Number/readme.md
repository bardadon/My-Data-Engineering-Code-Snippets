### Question - Unique In Order

https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:
```
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
```
### Bash Solution

```
#!/bin/bash

# Prerequsites
cd /tmp;

> solution.txt;

cat unique_in_order.csv >> solution.txt;

# Solution - For each letter in [A-Z]. delete the all occurances except for the first one
for i in {A..Z}; do

    sed -i "s/$i//2g" solution.txt
done;
```

### WorkFlow

![unique_in_order_workflow](https://user-images.githubusercontent.com/65648983/204299453-0f9bf62d-2b09-45ba-a1b3-c239891f30d2.png)


### Run the Data Pipeline
```
bash run_etl.sh
```

#### Input
```
unique_in_order('AAAABBBCCDAABBB')
```

#### Output
```
The Solution is: 
ABCD
```
