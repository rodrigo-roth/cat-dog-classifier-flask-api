FROM python:3.6

ADD / /app

WORKDIR /app

RUN pip --no-cache-dir --trusted-host pypi.python.org install -r /app/requirements.txt

EXPOSE 5000

CMD python -u main.py