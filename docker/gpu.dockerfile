FROM local0state/base:gpu-conda
LABEL maintainer="Ren Pang <rbp5354@psu.edu>"

RUN cd / && \
    git clone https://github.com/ain-soph/autovul.git && \
    cd /autovul/ && \
    pip install --no-cache-dir -e . && \
    mkdir /autovul/results/
WORKDIR /autovul/