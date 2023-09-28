#!/bin/bash
# Script that sends an OPTIONS request to the URL and display all HTTP methods the server will accept

url=$1
curl -sI -X OPTIONS "$url" | grep Allow | cut -d' ' -f 2-
