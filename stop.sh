#!/bin/bash

#if [ -f finished ]; then
#    echo "can't stop job that's already finished"
#    exit 1
#fi

#ENV="IUHPC"
if [ $ENV == "VM" ]; then
    pid=`cat pid`
    echo "running kill"
    kill $pid
fi


jobid=`cat jobid`
echo "running qdel $jobid"
qdel $jobid
