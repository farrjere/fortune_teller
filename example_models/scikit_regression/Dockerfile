FROM python:3-onbuild
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /code
WORKDIR /code
CMD [ "python", "predict.py" ]