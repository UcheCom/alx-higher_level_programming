#!/bin/bash
# Sends a POST request with the content of a JSON file and displays the body response
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
