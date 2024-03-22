#!/bin/bash


/usr/bin/apt update -y
/usr/bin/apt upgrade -y
/usr/bin/apt install jq python3 nginx -y
/usr/bin/python3 -m pip install boto3
