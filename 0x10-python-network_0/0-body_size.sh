#!/bin/bash
# Get body size from outgoing requesr ro url introduced as argument

curl -sI "$1" | grep 'Content-Length:' | cut -c 17-
