#!/bin/bash

for i in `cat ./services.txt`
do
  echo $i
  python3 one_srv_oncall.py $i
done