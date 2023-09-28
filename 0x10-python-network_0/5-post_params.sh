#!/bin/bash
# Script that sends a POST request to the URL with variables and display the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
