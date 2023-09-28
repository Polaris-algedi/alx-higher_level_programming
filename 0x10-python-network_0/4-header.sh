#!/bin/bash
# Script that sends a GET request to the URL with a header variable and display the body of the response

url=$1
curl -s -H "X-School-User-Id: 98" "$url"
