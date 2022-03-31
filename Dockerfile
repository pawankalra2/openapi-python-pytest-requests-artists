FROM python:3.7

WORKDIR /opt/openapi-python-pytest-requests-artists
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /opt/openapi-python-pytest-requests-artists