FROM python:3.6.3
ENV APPDIR /ihateline
WORKDIR $APPDIR
ADD . $APPDIR
ADD src/SourceHanSansTC-Medium.otf /tmp/font.otf
RUN pip install -r requirements.txt
