#!/bin/sh
. ./.env

while true; do
  git pull
  python3 main.py
  sleep 60
done
