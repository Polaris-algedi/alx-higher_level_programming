#!/bin/bash
# Script that send a DELETE request to the URL and display the body of the response

url=$1
curl -X DELETE "$url"
