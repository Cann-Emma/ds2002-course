#!/bin/bash


logfile="./logging.log"

NOW=`date`
STATUS="Warning"
MSG="This is a warning message"


echo $NOW - $STATUS - $MSG >> logging.log
