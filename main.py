from asyncio import run as aiorun
from datetime import datetime
from logging import INFO, StreamHandler, basicConfig
from random import seed
from sys import stdout
from typing import Optional

from typer import Argument, run

from tasks.sim import Simulation


async def _main(start: datetime, end: datetime):
    sim = Simulation(start, end)
    await sim.run()


def main(
    start_date: Optional[str] = Argument(None, help="start date for the simulation"),
    end_date: Optional[str] = Argument(None, help="end date for the simulation"),
    date_format: str = Argument("%m/%d/%Y", help="date format of passed in datetimes"),
    random_seed: Optional[int] = Argument(None, help="global random seed"),
) -> None:
    seed(random_seed)
    start = (
        datetime.strptime(start_date, date_format)
        if start_date
        else datetime(datetime.now().year, 1, 1)
    )
    end = datetime.strptime(end_date, date_format) if end_date else datetime.now()
    aiorun(_main(start, end))


if __name__ == "__main__":
    basicConfig(
        level=INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[StreamHandler(stdout)],
    )
    run(main)
