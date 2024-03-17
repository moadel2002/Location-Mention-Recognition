FROM ubuntu

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-setuptools

RUN pip3 install pandas numpy flair

RUN mkdir -p /home/geoai

WORKDIR /home/geoai

COPY . /home/geoai

CMD ["python3", "predict.py"]
