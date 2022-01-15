FROM python:alpine

RUN pip install --no-cache-dir boto3 && \
    pip install --no-cache-dir flask

ADD entrypoint.py /

ENTRYPOINT ["python3","-u", "/entrypoint.py"]