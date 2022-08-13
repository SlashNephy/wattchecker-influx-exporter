# wattchecker-influx-exporter

🔌 A tiny tool to export wattchecker metrics

`docker-compose.yml`

```yaml
version: '3.8'

services:
  influxdb:
    container_name: InfluxDB
    image: influxdb
    restart: always
    volumes:
      - influxdb:/var/lib/influxdb

  wattchecker-influx-exporter:
    container_name: wattchecker-influx-exporter
    image: ghcr.io/slashnephy/wattchecker-influx-exporter:master
    restart: always
    devices:
      - /dev/rfcomm0
    environment:
      # rfcomm デバイス
      DEVICE: /dev/rfcomm0
      # ラベル (空白不可)
      LABEL: wattchecker
      # InfluxDB アドレス
      INFLUX_ADDR: http://influxdb:8086
      # InfluxDB データベース名
      INFLUX_DB: wattchecker

volumes:
  influxdb:
```

## Acknowledgements

Original C programs came from https://armadillo.atmark-techno.com/howto/armadillo_rex-btwattch1. Thanks for the C implementations.

`wattchecker.c`

```
/*
 * This file is provided under a Simplified BSD License.
 *
 * Copyright (C) 2017 Atmark Techno, Inc. All Rights Reserved.
 *
 * Permission to use, copy, modify, and/or distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
 * SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION
 * OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
 * CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */
```

`crc8.c`, `crc8.h`

```
/*
 * This file is provided under a Simplified BSD License.
 *
 * Based on linux/lib/crc8.c
 *
 * Copyright (c) 2011 Broadcom Corporation
 * Copyright (C) 2017 Atmark Techno, Inc. All Rights Reserved.
 *
 * Permission to use, copy, modify, and/or distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
 * SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION
 * OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
 * CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */
```
