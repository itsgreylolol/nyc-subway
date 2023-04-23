import os

import aiohttp
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

from data.loaders.base_loader import BaseLoader


class TurnstileLoader(BaseLoader):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Max-Age": "3600",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    }

    async def load(self) -> None:
        good_years = range(2015, 2023)
        base_url = "http://web.mta.info/developers/"
        main_url = f"{base_url}turnstile.html"
        local_path = "./cache"

        async with aiohttp.ClientSession() as session:
            resp = await session.get(main_url, headers=self.headers)
            soup = BeautifulSoup(await resp.text(), "html.parser")
            links = soup.select(".span-84.last a")
            os.makedirs(local_path, exist_ok=True)

            for year in tqdm(good_years, "iterating years"):
                year_path = os.path.join(local_path, f"turnstile-{year}.pickle")
                if not os.path.exists(year_path) or year == max(good_years):
                    dfs = []
                    good_links = [x for x in links if str(year) in x.text]
                    for link in tqdm(good_links, "iterating links"):
                        dfs.append(pd.read_csv(f"{base_url}{link.get('href')}"))

                    if len(dfs):
                        df = pd.concat(dfs)
                        df.to_pickle(year_path)
