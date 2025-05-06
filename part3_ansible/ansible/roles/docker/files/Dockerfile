FROM ubuntu:22.04

WORKDIR /app

COPY http_requests.py .

RUN chmod +x http_requests.py

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install requests

CMD ["python3", "http_requests.py"]