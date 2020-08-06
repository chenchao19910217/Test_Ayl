FROM python:3.7
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
ADD sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install cron -yq
COPY google-chrome-stable_current_amd64.deb /opt
RUN apt-get install /opt/google-chrome* -yq
ADD . /code
CMD ["python","manage.py","runserver","0.0.0.0:8080"]

#
#

#FROM ubuntu:16.04
#EXPOSE 9100
#
#COPY google-chrome-stable_current_amd64.deb /opt
#
#RUN apt-get update \
#    && apt-get install python -y \
#    && apt-get install python3 -y \
#    && apt-get install python3-pip -y \
#    && pip3 install requests \
#    && pip3 install selenium==2.48.0 \
#    && apt-get install wget -y \
#    && wget -P /opt http://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip \
#    && apt-get install unzip -y \
#    && unzip /opt/chrome* -d /usr/bin/ \
#    && wget -P /opt https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
#    && tar -xvf /opt/phantomjs* -C /opt \
#    && mv /opt/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin \
#    && apt-get install xfonts-wqy -y \
#    && pip3 install openpyxl \
#    && pip3 install pillow \
#    && apt-get install git -y
#
#WORKDIR /opt
#RUN dpkg -i google-chrome* >>/tmp/google_error_log.txt || echo 1\
#    && apt-get install -f -y \
#    && dpkg -i google-chrome* \
#    && apt-get install sudo -y \
#    && pip3 install django==1.8 \
#    && pip3 install pymysql \
#    && echo /code/tts >>/usr/lib/python3/dist-packages/MyModule.pth