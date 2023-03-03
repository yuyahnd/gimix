from argparse import ArgumentParser
from gimix.cmd import load


def main() -> None:
    """gimix main."""
    parser = ArgumentParser(description='mix commands')
    subparsers = parser.add_subparsers()

    # sub commands
    load.parser(subparsers)

    # handle command
    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
