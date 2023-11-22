#!/bin/bash

for i in *.py
do
    echo "#!/usr/bin/python3" > $i
done
