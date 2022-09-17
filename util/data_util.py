import glob
import logging
import os
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_turnstile_data() -> pd.DataFrame:
    pattern = re.compile(r"\sAV$")
    if not os.path.exists("./cache/turnstile-all.ftr"):
        logging.info("getting turnstile data")
        os.makedirs("./cache")
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        }
        base_url = "http://web.mta.info/developers/"
        url = f"{base_url}turnstile.html"
        req = requests.get(url, headers)

        dfs = []
        soup = BeautifulSoup(req.content, "html.parser")
        links = soup.select(".span-84.last a")
        good_years = ["2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015"]

        for year in good_years:
            for link in links:
                if year in link.text:
                    dfs.append(pd.read_csv(f"{base_url}{link.get('href')}"))

            df = pd.concat(dfs)
            df.to_feather(df, f"./cache/turnstile-{year}.ftr")
            dfs = []

        df = pd.concat(
            map(pd.read_feather, glob.glob(os.path.join("", "./cache/*.ftr")))
        )
        df = df[df["DESC"] == "REGULAR"]
        files = glob.glob(os.path.join("", "./cache/*.ftr"))
        for f in files:
            os.remove(f)

        logging.info("writing turnstile data to local cache")
        df.to_feather("./cache/turnstile-all.ftr")

        return df
    else:
        logging.info("reading turnstile data")
        return pd.read_feather("./cache/turnstile-all.ftr")
