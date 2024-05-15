FROM tensorflow/tensorflow:2.0.0rc0-gpu-py3-jupyter

ENV PATH="/.local/bin:${PATH}"

ADD ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install packaging
RUN apt-get update -y && apt-get install git wget -y
RUN pip install -r requirements.txt
EXPOSE 8888 6006

## XXXXX VS-Code mapping data folders and configuring DVC

FROM tensorflow/tensorflow:2.10.0-gpu-jupyter

ARG MY-RPOJECT-NAME
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC
ADD ./requirements.txt .
RUN apt-get update && apt-get install -y git
RUN apt-get install -y openssh-client
RUN pip3 -q install pip --upgrade
RUN pip install --upgrade pip

RUN pip install -r requirements.txt
RUN pip install dvc

RUN nbdev_install_quarto
## Matching the cuda version for this container and T5 server Feb 2023
RUN pip install --upgrade torch==1.12.1 --extra-index-url https://download.pytorch.org/whl/cu113 

#TODO: How to change the project name dynamicaly
RUN git config --global --add safe.directory /workspaces/${MY-PROJECT-NAME}
