# -*- coding: utf-8 -*-

import click
import logging
import sys

from my_package.application import App

@click.command()
@click.argument('first_name')
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
def hello_world(first_name, verbose):
    app = App()
    if verbose:
        print("Performing hello world.")
    print(app.get_hello_world(first_name))


@click.group()
def main(args=None):
    """Command line utility"""
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)


main.add_command(hello_world)


if __name__ == "__main__":
    sys.exit(main())
