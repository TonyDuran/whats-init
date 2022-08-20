FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install -y python3 python3-pip
RUN apt-get install -y libgconf2-4 libxss1 libnss3 libnspr4
RUN apt-get install -y fonts-liberation libappindicator3-1 xdg-utils

RUN apt-get install -y curl unzip wget
RUN apt-get install -y xvfb
RUN apt-get install -y software-properties-common


RUN GECKODRIVER_VERSION=`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'` && \
    wget https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz && \
    tar -zxf geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver

RUN add-apt-repository -y ppa:ubuntu-mozilla-daily/ppa
RUN apt-get update -y
RUN apt-get install -y firefox

# install chromedriver and google-chrome

RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/bin
RUN chmod +x /usr/bin/chromedriver

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome*.deb
RUN apt-get install -y -f

RUN pip3 install --upgrade --ignore-installed urllib3
RUN pip3 install -r requirements.txt/worker.txt

#TODO: COPY wkdir and install -r requirements.txt
