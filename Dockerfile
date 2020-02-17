FROM lambci/lambda:build-python3.7

WORKDIR /var/task/src

RUN pip install chalice

ADD ./src/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
