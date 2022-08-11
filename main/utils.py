import json
from decimal import Decimal

import aiohttp
import redis

from config import Settings


redis_connection = redis.Redis(host=Settings.REDIS_HOST, port=Settings.REDIS_PORT, db=0)


def path_to_file(file_path):
    return "%s/%s" % (Settings.ROOT_DIR, file_path)


async def parse_usd():
    url = Settings.CBRF_DAILY

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = json.loads(await response.text())
            usd = content["Valute"]["USD"]["Value"]

            redis_connection.set("usd", usd, 86400)

            return usd


async def usd_in_rub(summ):
    usd = redis_connection.get("usd")
    if not usd:
        usd = await parse_usd()
    if isinstance(usd, bytes):
        usd = json.loads(usd)

    usd = Decimal(usd)
    summ = Decimal(summ)

    result = usd * summ

    return float("%.2f" % result)
