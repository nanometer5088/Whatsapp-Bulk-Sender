#!/bin/bash

# check if Python is installed
if command -v python &> /dev/null
then
    # run the Python script
    python main.py
else
    # print an error message
    echo "Python is not installed on this system."
fi