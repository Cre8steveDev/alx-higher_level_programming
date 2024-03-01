#!/bin/bash
# Displays all HTTP methods the server will accept
curl -sI HEAD "$1" | grep "Allow:" | cut -d" " -f2-4

