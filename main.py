import asyncio
import logging
import sys

from tasks.sim import Simulation


async def main():
    sim = Simulation()
    await sim.run()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    asyncio.run(main())
