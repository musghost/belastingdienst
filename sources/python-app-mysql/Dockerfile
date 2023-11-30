FROM registry.access.redhat.com/ubi8/python-39
USER root
RUN wget https://dev.mysql.com/get/mysql80-community-release-el8-9.noarch.rpm &&\
    yum install mysql80-community-release-el8-9.noarch.rpm -y &&\
    rm mysql80-community-release-el8-9.noarch.rpm &&\
    yum install yum-utils -y &&\
    yum-config-manager --enable mysql80-community &&\
    yum install mysql-community-devel.x86_64 -y &&\
    yum install python3-devel -y

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
USER default
EXPOSE 5000
CMD [ "python", "app.py" ]
