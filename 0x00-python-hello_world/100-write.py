#!/usr/bin/python3
import sys

with open('q', 'r') as file:
    text = file.read()
sys.stderr.write(text)
sys.exit(1)
