#!/bin/bash
# Get body size from outgoing request to url introduced as argument
curl -sI "$1" | grep 'Content-Length' | cut -c 17-
