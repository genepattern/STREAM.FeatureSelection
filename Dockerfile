FROM pinellolab/stream:0.3.8

RUN mkdir /stream
COPY featureselection_command_line.py /stream/featureselection_command_line.py

ENTRYPOINT []
