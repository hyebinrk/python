# 베이스 이미지
FROM ubuntu:22.04

# 메타데이터 추가
LABEL maintianer="HB hbinndo@naver.com"

# 시스템 업데이트
RUN apt update -y && \
    apt install -y sudo passwd openssh-server wget \
    apt install -y nano net-tools \
    apt install -y iputils-ping openjdk-8-jdk python3-pip && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# 계정생성 및 세팅
RUN groupadd pkdata && useradd -m -d /home/pkdata -s /bin/bash -g pkdata -G sudo pkdata && \
       echo "pkdata:1234" | chpasswd && \
       mkdir -p /home/pkdata/.ssh && \
       chown -R pkdata:pkdata /home/pkdata && \
       echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> /home/pkdata/.bashrc && \
       exho "export PATH=$PATH:/home/pkhb/.local/bin" >> /home/pkdata/.bashrc && \
       chown pkdata:pkdata /home/pkdata/.bashrc && \
       mkdir -p /var/run/sshd && \
       echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
       echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
       
# 사용자 변경
USER pkdata

# 작업환경 변경
WORKDIR /home/pkdata

# pip 업그레이드 및 주피터랩 설치
RUN pip install --upgrade pip && pip install jupyterlab && \
       echo "export PATH=\$home\.local/bin:\$PATH" >> ~/.bashrc 

# ssh 서버 실행 및 주피터랩 가동(외부접속가능)
CMD ["/bin/bash","-c","service ssh start && python3 -m jupyterlab --ip=0.0.0.0 --port=8888 --allow-root --FileContetsManager.delete_to_trash=False"]