#!/bin/bash
# Script that sends a JSON POST request to the URL with the contents of the file in the body of the request and display the body of the response

url=$1
file=$2
curl -s -X POST -H "Content-Type: application/json" -d @"$file" "$url"
