FROM nginx:1.19.2-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY cache.conf /etc/nginx/conf.d
RUN mkdir -p /tmp/cache/api
