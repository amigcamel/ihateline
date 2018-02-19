FROM alpine:3.6

RUN apk update
RUN apk upgrade
RUN apk add ca-certificates && update-ca-certificates
# Change TimeZone
RUN apk add --update tzdata
ENV TZ=Asia/Taipei
# Clean APK cache
RUN rm -rf /var/cache/apk/*

COPY crontabs /etc/crontabs/root
CMD ["crond", "-f", "-d", "8"]
