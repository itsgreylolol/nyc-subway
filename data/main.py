import asyncio
import logging
import sys

from .loaders import TurnstileLoader


async def main():
    turnstile_loader = TurnstileLoader()
    await turnstile_loader.load()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("./logs/log.txt"),
        ],
    )
    asyncio.run(main())
