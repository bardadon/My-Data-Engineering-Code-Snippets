#!/bin/bash

rm -r ./solutions/
mkdir ./solutions/

docker cp airflow_worker:/tmp/solution.txt ./solutions/