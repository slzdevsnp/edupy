#!/bin/sh

## linux based
# start the cashman application
# start bootstrap in another terminal
#./bootstrap.sh &

echo "get incomes"
curl -X GET http://localhost:5000/incomes

hdr_json="Content-Type: application/json"

echo "add new income"
curl -X POST -H "${hdr_json}" -d '{
  "description": "lottery",
  "amount": 1000.0
}' http://localhost:5000/incomes

echo "check new income was added"
curl localhost:5000/incomes

# kill pocesses matching flask --debug run
#kill -9 $(ps -aef | grep -e "flask --debug run" | awk '{print $2}')