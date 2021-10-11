FROM local0state/base:cpu-conda
LABEL maintainer="Ren Pang <rbp5354@psu.edu>"

RUN pip install --no-cache-dir autovul && \
    cd / && \
    git clone https://github.com/ain-soph/autovul.git
WORKDIR /autovul/