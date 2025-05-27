import argparse
import logging
from typing import Sequence


LOGGER = logging.getLogger(__name__)


def parse_args(
    argv: Sequence[str] | None = None
) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="A simple CLI example using argparse."
    )
    parser.add_argument(
        "--name",
        type=str,
        help="Your name",
        required=True,
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv=argv)
    LOGGER.info("args: %r", args)
    print(f"Hello, {args.name}!")
