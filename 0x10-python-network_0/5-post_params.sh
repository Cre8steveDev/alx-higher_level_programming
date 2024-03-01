#!/bin/bash
# Takes a url that sends a post requests with variables
curl -X POST -d"email=test@gmail.com" -d "I will always be here for PLD" "$1"
