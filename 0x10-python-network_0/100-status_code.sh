#!/bin/bash
# sends a request to a URL passed as an argument, retunr the status code of the response
curl -so /dev/null --write-out "%{http_code}" "$1"
