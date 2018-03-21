#!/bin/bash

echo "Running locust chat tests locally..."

locust -f chat.py --host=http://piratebox.lan
