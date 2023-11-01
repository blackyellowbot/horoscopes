FROM python
LABEL authors="devs"
WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt
COPY . /src
