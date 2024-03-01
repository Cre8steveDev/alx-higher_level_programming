#!/bin/bash
# Making a Request to a server using Curl and printing 
curl -s -I "$1" | grep "Content-Length" | cut -d" " -f2