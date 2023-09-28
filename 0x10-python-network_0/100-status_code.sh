#!/bin/bash
# Script that sends a request to the URL and display only the status code of the response

url=$1
curl -s -o /dev/null -w "%{http_code}" "$url"