#!/bin/sh

## linux based
# start the cashman application
# start bootstrap in another terminal
#./bootstrap.sh &


hdr_json="Content-Type: application/json"
URL="http://localhost:5000"

echo "## get expenses"
curl -X GET ${URL}/expenses


echo "# add new expense"
curl -X POST -H "${hdr_json}" -d '{
    "amount": 20,
    "description": "lottery ticket"
}' ${URL}/expenses

echo "## check expenses after addition"
curl -X GET $URL/expenses



echo "###### get incomes"
curl -X GET $URL/incomes


echo "# add new income"
curl -X POST -H "${hdr_json}" -d '{
  "description": "loan payment",
  "amount": 300.0
}' $URL/incomes


echo "# check incomes after new income was added"
curl $URL/incomes

# kill pocesses matching flask --debug run
#kill -9 $(ps -aef | grep -e "flask --debug run" | awk '{print $2}')