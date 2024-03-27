#!/bin/bash
# Script that return the HTTP methods allowed on a server
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
