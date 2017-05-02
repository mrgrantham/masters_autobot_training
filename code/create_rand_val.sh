#!/bin/bash

#randomly select 1/6 of the training data for testing


NUMFILES=$(ls -1q * | wc -l)
# 1/6 of photos for test set
echo Total $NUMFILES
NUMFILES=$(($NUMFILES/6))
echo Train $NUMFILES
i=1

while [ "$i" -le "$NUMFILES" ]; do
    RANFILE=$(shuf -n1 -e ./train/*)
    echo $RANFILE
    mv $RANFILE ./test/
    i=$((i+1))
done
shuf -n1 -e ./train/*