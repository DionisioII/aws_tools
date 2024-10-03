FROM amazonlinux:2022
MAINTAINER Giampiero Cimini <g.cimini@emojlab.com>

WORKDIR /project

COPY . .



RUN  yum install -y openssl-devel \
	&& yum -y install binutils-devel.x86_64 \
     && yum install -y libXext libSM libXrender \
     && yum install -y libsndfile \
     && yum install -y tar \
     && yum install -y xz \
     && yum install -y python39 \
     && curl -O https://bootstrap.pypa.io/get-pip.py \
     && python3 get-pip.py \
     && python3 -m pip install scikit-learn==1.1.2 \
     && python3 -m pip install numpy==1.21.0 \
     && python3 -m pip install opencv-contrib-python-headless==4.5.1.48 \
     && python3 -m pip install numba==0.55.1 \
     && python3 -m pip install loguru==0.6.0 \
     && python3 -m pip install pandas==1.3.5 \
     && python3 -m pip install librosa==0.9.1 \
     && python3 -m pip install onnxruntime==1.10.0 \
     && python3 -m pip install tflite-runtime==2.7.0 \
     && python3 -m pip install boto3 \
     && python3 -m pip install pyinstaller \
     && yum install -y libsndfile zip unzip \
     && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
     && unzip awscliv2.zip \
     && ./aws/install

ENTRYPOINT ["python3", "main.py"]
#CMD /bin/bash
