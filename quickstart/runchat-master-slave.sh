#!/bin/bash

echo "Starting locust master..."

locust -f chat.py --master --host=http://piratebox.lan &

echo "Starting locust using mutiple processes..."

locust -f chat.py --slave --host=http://piratebox.lan &
locust -f chat.py --slave --host=http://piratebox.lan &
locust -f chat.py --slave --host=http://piratebox.lan &

echo "Remember to stop slave locusts."

