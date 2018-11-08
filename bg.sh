#!/bin/bash

server='https://electrics.fortheusers.org'
username='Username'
percentage=$(pmset -g batt | grep -Eho '(...)%' | xargs | sed 's/%//')

curl --http1.1 --header "Content-Type: application/json" --data "{\"username\":\"$username\",\"percentage\":$percentage}" $server/percentage
