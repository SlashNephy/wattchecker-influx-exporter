FROM python:alpine

RUN apk add --update --no-cache --virtual .build-deps \
        build-base \
        linux-headers \
        curl \
        make \
        musl-dev \
    \
    && apk add --no-cache \
        expect \
    && pip install --no-cache-dir \
        aiohttp \
    # Build
    && cd /tmp \
    && curl -O https://download.atmark-techno.com/misc/howto_armadillo_rex-btwattch1/wattchecker_20170911.tar.gz \
    && tar xzvf wattchecker_20170911.tar.gz \
    && cd wattchecker_20170911 \
    && sed -i -e "s/arm-linux-gnueabihf-//" Makefile \
    && make \
    && install -m 755 wattchecker /usr/local/bin \
    \
    # Clean
    && apk del --purge .build-deps \
    && rm -rf /tmp/wattchecker_20170911 /tmp/wattchecker_20170911.tar.gz

COPY entrypoint.py /

ENV DEVICE=/dev/rfcomm0
ENV LABEL=wattchecker
ENV INFLUX_ADDR=http://influxdb:8086
ENV INFLUX_DB=wattchecker
ENTRYPOINT ["python", "-u", "/entrypoint.py"]
