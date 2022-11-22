from datetime import datetime
from glob import glob
from logging import info
from os import makedirs, remove
from os.path import exists, join
from pathlib import Path

from bs4 import BeautifulSoup
from pandas import DataFrame, concat, read_csv, read_feather, to_datetime
from requests import get


class DataLoader:
    def get_turnstile_data(self) -> DataFrame:
        if not exists("./cache/turnstile-all.ftr"):
            info("getting turnstile data")
            df = self._download()
        else:
            info("reading turnstile data")
            df = read_feather(Path("./cache/turnstile-all.ftr"))

        return self._transform(df)

    @staticmethod
    def _download() -> DataFrame:
        makedirs("./cache", exist_ok=True)
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        }
        base_url = "http://web.mta.info/developers/"
        url = f"{base_url}turnstile.html"
        req = get(url, headers)

        dfs = []
        soup = BeautifulSoup(req.content, "html.parser")
        links = soup.select(".span-84.last a")
        good_years = range(2015, datetime.now().year + 1)

        for year in good_years:
            for link in links:
                if str(year) in link.text:
                    dfs.append(read_csv(f"{base_url}{link.get('href')}"))

            df = concat(dfs).reset_index()
            df.to_feather(Path(f"./cache/turnstile-{year}.ftr"))
            dfs = []

        df = concat(list(map(read_feather, glob(join("", "./cache/*.ftr")))))
        df = df[df["DESC"] == "REGULAR"]
        files = glob(join("", "./cache/*.ftr"))
        for f in files:
            remove(f)

        info("writing turnstile data to local cache")
        df.reset_index(drop=True).to_feather(Path("./cache/turnstile-all.ftr"))

        return df

    @staticmethod
    def _transform(df: DataFrame) -> DataFrame:
        df.columns = df.columns.str.strip()

        df["DATETIME_STR"] = df.apply(lambda x: f"{x['DATE']} {x['TIME']}", axis=1)
        df["DATETIME"] = to_datetime(df["DATETIME_STR"], format="%m/%d/%Y %H:%M:%S")

        # column errors?
        df = (
            df.sort_values("DATETIME")
            .groupby(["STATION", "SCP"])
            .agg({"ENTRIES": "diff", "EXITS": "diff"})
        )

        return df
