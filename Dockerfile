FROM tensorflow/tensorflow:2.0.0rc0-gpu-py3-jupyter

ENV PATH="/.local/bin:${PATH}"

ADD ./requirements.txt .

RUN apt-get update -y && apt-get install git wget -y
RUN pip install -r requirements.txt

EXPOSE 8888 6006
