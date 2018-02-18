FROM python:3.6.3
ENV APPDIR /ihateline
WORKDIR $APPDIR
ADD . $APPDIR
RUN pip install -r requirements.txt
