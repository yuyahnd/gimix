from argparse import ArgumentParser
from gimix.cmd import load

def test_parser():
    parser = ArgumentParser(description='mix commands')
    subparsers = parser.add_subparsers()

    parser = load.parser(subparsers)
    assert hasattr(parser, 'add_help')
