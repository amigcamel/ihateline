FROM python:3.6.4-alpine3.7
WORKDIR /home/root
RUN apk update
RUN apk upgrade
RUN apk add ca-certificates && update-ca-certificates
# Change TimeZone
RUN apk add --update tzdata
ENV TZ=Asia/Taipei
# Clean APK cache
RUN rm -rf /var/cache/apk/*
COPY client.py /home/root
CMD ["crond", "-f", "-d", "8"]
