FROM python:3.8-slim-buster
COPY . /usr/app
EXPOSE 1000
WORKDIR /usr/app/
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools
RUN  pip install -r requirements.txt
CMD python3 main.py