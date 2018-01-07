FROM centos:7
RUN yum install -y epel-release
RUN yum update -y
RUN yum install -y python-pip \
                   python-devel \
                   make \
                   gcc
RUN pip install ansible==2.2.0.0
ADD hosts /app/
WORKDIR /app
