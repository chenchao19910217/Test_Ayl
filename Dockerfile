FROM python:3.7
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
RUN apt-get install cron -yq
ADD . /code
CMD ["python","manage.py","runserver","0.0.0.0:8080"]
