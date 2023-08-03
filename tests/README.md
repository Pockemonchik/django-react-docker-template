Тесты
_________________
Генерация тестов по сваггеру :

docker pull openapitools/openapi-generator-cli

docker run --rm -v /pathtoswagger/:/local/ openapitools/openapi-generator-cli generate \
    -i /local/spec.json \
    -g k6 \
    -o /local/k6-test/ 

_________________
Запуск тестов:

sudo docker run --rm -i grafana/k6 run - <script.js

sudo docker run --rm -i grafana/k6 run --vus 3 --iterations 3 - <script.js