#!/usr/bin/bash
# Script return the header: content-header from the server response
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
