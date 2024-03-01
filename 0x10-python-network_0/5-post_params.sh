#!/bin/bash
# Takes a url that sends a post requests with variables
curl -X POST -data-urlencode email=test@gmail.com subject="I will always be here for PLD" "$1"
