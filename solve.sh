#! /bin/sh

folder="day$1"
solution=$(python compute.py $folder)

echo "Computing solution for $folder"
echo "Solution: $solution"
