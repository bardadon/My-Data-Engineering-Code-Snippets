#!/bin/bash

cd /tmp;

> solution.txt;

cat unique_in_order.csv >> solution.txt;

for i in {A..Z}; do

    sed -i "s/$i//2g" solution.txt
done;

