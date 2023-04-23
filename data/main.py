import asyncio
import logging
import sys

from data.loaders.turnstile_loader import TurnstileLoader


async def main():
    turnstile_loader = TurnstileLoader()
    await turnstile_loader.load()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    asyncio.run(main())
