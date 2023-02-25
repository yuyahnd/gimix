from typing import Any
from argparse import (
    ArgumentParser,
    Namespace,
    _SubParsersAction as SubParsersAction,
)
from pathlib import Path
from gimix import files
import sys


def parser(subparser: SubParsersAction) -> ArgumentParser:
    parser  = subparser.add_parser("load", help="see `load -h`")
    parser.add_argument("-i", "--input",
                        type=str,
                        help="file path")
    parser.add_argument("-m", "--mode",
                        type=str,
                        choices=["r", "rb"],
                        default="r",
                        help="file open mode")
    parser.add_argument("-e", "--encoding",
                        type=str,
                        default="utf-8",
                        help="file encoding")
    parser.set_defaults(handler=load_command)

    return parser


def load_command(args: Namespace) -> None:
    input = args.input
    mode = args.mode
    encoding = args.encoding

    if sys.stdin.isatty():
        contents = files.load(input, mode, encoding)
        echo(contents)
    else:
        paths = []
        for input in sys.stdin:
            path = Path(input.rstrip())
            if path.is_file():
                paths.append(str(path))

        for input in paths:
            contents = files.load(input, mode, encoding)
            echo(contents)

def echo(contents: Any) -> None:
    if isinstance(contents, list):
        sys.stdout.write("".join(contents))
