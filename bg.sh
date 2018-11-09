#!/bin/bash
username=${1:-$USER}
server='https://electrics.fortheusers.org'
percentage=$(pmset -g batt | grep -Eho '([0-9]*)%' | xargs | sed 's/%//')

discharging=$(pmset -g batt | grep 'discharging')
chargestatus=$([ -z "$discharging" ] && echo 1 || echo 0)

curl --http1.1 --header "Content-Type: application/json" --data "{\"username\":\"$username\",\"percentage\":$percentage,\"charging\":$chargestatus}" $server/percentage
