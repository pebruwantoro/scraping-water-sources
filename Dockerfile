FROM python:3.10-slim

COPY . /app

WORKDIR /app

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        build-essential git libssl-dev libpq-dev libmariadb-dev && \
    pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "/main.py"]
