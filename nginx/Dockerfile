FROM nginx:1.23-alpine

RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
COPY http.conf /etc/nginx/conf.d/
COPY stream.conf /etc/nginx/conf.d/