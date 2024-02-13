#!/bin/bash


date

if [[$? -eq 0]]
then
	echo "Success"
	exit 0
else 
	echo "Failure"
	exit 1;
fi
