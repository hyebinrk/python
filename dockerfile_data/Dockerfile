# 베이스 이미지
FROM ubuntu:22.04

# 메타데이터 추가
LABEL maintianer="HB hbinndo@naver.com"

RUN apt update -y
RUN apt install -y sudo passwd openssh-server wget
RUN apt install -y nano net-tools
RUN apt install -y iputils-ping openjdk-8-jdk python3-pip

RUN apt clean
RUN rm -rf /var/lib/apt/lists/*

# 계정생성 및 세팅
RUN groupadd pkhb && useradd -m -d /home/pkhb -s /bin/bash -g pkhb -G sudo pkhb && \
       echo "pkhb:1234" | chpasswd && \
       mkdir -p /home/pkhb/.ssh && \
       chown -R pkhb:pkhb /home/pkhb && \
       echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> /home/pkhb/.bashrc && \
       chown pkhb:pkhb /home/pkhb/.bashrc && \
       mkdir -p /var/run/sshd && \
       echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
       echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
       
# 사용자 변경
USER pkhb

# 작업환경 변경
WORKDIR /home/pkhb

# pip 업그레이드 및 주피터랩 설치
RUN pip install --upgrade pip && pip install jupyterlab

# ssh 서버 실행 및 주피터랩 가동(외부접속가능)
CMD ["/bin/bash","-c","service ssh start && python3 -m jupyterlab --ip=0.0.0.0 --prt=8888 --allow-root"]
8888 --allow-root --FileContentsManager.delete_to_trash=False"]