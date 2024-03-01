#!/bin/bash
# Making a Request to a server using Curl and printing 
# just the size of the body in the Content-Length

GIVEN_URL=$1
curl -s -I "$GIVEN_URL" | grep "Content-Length" | cut -d" " -f2