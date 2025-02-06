FROM ubuntu:latest

RUN apt-get update
RUN apt install -y openjdk-11-jre-headless
RUN apt install -y wget
RUN apt install -y nginx
RUN apt install -y python3 pip3


WORKDIR /automation_runner
COPY .pdrunner-creds /automation_runner/
COPY alerter.py /automation_runner/

RUN wget https://runbook-actions.pagerduty.com/pd-runner.jar


CMD ["bash"]
