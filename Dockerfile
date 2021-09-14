FROM python:3.8.11-alpine3.13
WORKDIR /usr/src/app

# setting up timezone data
RUN apk update
RUN apk add tzdata
RUN cp /usr/share/zoneinfo/Asia/Kolkata /etc/localtime
RUN echo "Asia/Kolkata" >  /etc/timezone

# installing chromium
RUN apk add chromium chromium-chromedriver

# copying and installing requirements
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./config.ini .
COPY ./webscp/ ./src
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "-m", "src" ]
