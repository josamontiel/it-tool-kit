#!/bin/bash

line="---------------------------"

echo "starting at $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; df -h; echo $line

echo "WHO"; who; echo $line

echo "Finishing at $(date)"
