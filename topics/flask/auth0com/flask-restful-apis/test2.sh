#!/bin/sh

## linux based
# start the cashman application
# start bootstrap in another terminal
# expect the app runing in docker container started with docker-compose up  -d
echo "starting docker container cashman in detached mode"
docker run --name cashman -d -p 5000:5000 cashman

sleep 3

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

echo "stopping cashman docker container. This can take some seconds"
docker stop cashman
docker container rm cashman