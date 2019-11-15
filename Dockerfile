FROM python:3.7.3-slim
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV FLASK_APP=adapis
ENV FLASK_DEBUG=1
CMD flask run --host=0.0.0.0
