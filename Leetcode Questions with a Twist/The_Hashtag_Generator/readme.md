### Question - The Hashtag Generator
https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

```
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.
    
    

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
```

### Workflow
1. Setting up a PostgreSQL database and exporting a CSV file filled with input data
![image](https://user-images.githubusercontent.com/65648983/204628461-4beea3a4-297c-4196-9d97-53a619f46649.png)

2. Move CSV file from airflow_worker and into Local.

3. Read CSV and solve question using Python.

### Run the ETL

The ETL stages are set up in file __run_etl.sh__:

``` 
#!/bin/bash

# Run Airflow Dags
docker exec -it airflow_scheduler airflow dags unpause hashtag_generator
docker exec -it airflow_scheduler airflow dags trigger hashtag_generator

# Export the CSV file from airflow_worker to local
docker cp airflow_worker:tmp/input_data.csv input_data.csv

# Solve Problem
python solve_problem.py
```

To run the ETL, use this command:

```
bash run_etl.sh
```

### Solution

```
                                     Input                          Solution
0                                   test1                            #Test1
1                                   test2                            #Test2
2                                   Hello                            #Hello
3   Hello there thanks for trying my Kata  #HelloThereThanksForTryingMyKata
4                      Hello     World                          #HelloWorld
```
