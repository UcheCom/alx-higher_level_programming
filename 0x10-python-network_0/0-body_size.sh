#!/bin/bash
# sends a URL request and displays the size of the body response
curl -s "$1" | wc -c
