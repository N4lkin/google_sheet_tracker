import json
from decimal import Decimal

import aiohttp
import redis

from config import Settings
from main.constants import BASE_DIR


redis_connection = redis.Redis(host="0.0.0.0", port=6379, db=0)


def path_to_file(file_path):
    return "%s/%s" % (BASE_DIR, file_path)


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
