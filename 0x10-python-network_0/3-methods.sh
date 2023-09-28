#!/bin/bash
# Script that sends an OPTIONS request to the URL and display all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | grep Allow | cut -d' ' -f 2-
