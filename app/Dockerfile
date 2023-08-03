# pull official base image
FROM python:3.9

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install  -y gcc python3-dev 

RUN apt-get install -y  virtualenv 
RUN apt-get install -y postgresql-client

# install dependencies
RUN virtualenv --python=/usr/bin/python3 --system-site-packages /virtenv
RUN exit
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
COPY ./worker-entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN sed -i 's/\r$//g' /usr/src/app/worker-entrypoint.sh
# copy project
COPY . .
RUN chmod 777 /usr/src/app/entrypoint.sh
RUN chmod 777 /usr/src/app/worker-entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]