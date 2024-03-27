#!/bin/bash
# Script returns response filtering the header with a param
curl -sX GET -H "X-School-User-Id: 98" "$1"
