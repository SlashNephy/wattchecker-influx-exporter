import asyncio
import os
import re
from subprocess import Popen, PIPE

from aiohttp import ClientSession

device = os.getenv("DEVICE")
label = os.getenv("LABEL")
influx_addr = os.getenv("INFLUX_ADDR")
influx_db = os.getenv("INFLUX_DB")

line_pattern = r"^voltage = (\d+\.\d+)V , current = (\d+\.\d+)mA , power = (\d+\.\d+)W$"

async def main():
    while True:
        await do_loop()
        await asyncio.sleep(10)

async def do_loop():
    with Popen(["unbuffer", "wattchecker", device], stdout=PIPE, bufsize=-1) as p:
        with open(p.stdout.fileno(), closefd=False) as stream:
            for line in stream:
                m = re.match(line_pattern, line)
                if not m:
                    continue

                voltage, current, power = [float(x) for x in m.groups()]
                await write(label, {"voltage": voltage, "current": current, "power": power})

        p.wait()

async def write(measurement, data):
    async with ClientSession(raise_for_status=True) as session:
        line = f"{measurement} " + ",".join([f"{k}={v}" for k, v in data.items()])

        async with session.post(f"{influx_addr}/write?db={influx_db}&precision=s", data=line):
            print(f"Write: {line}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
