# -*- coding: utf-8 -*-

import click
import logging
import sys

from fair_metadata.generate_metadata import create_dataset_prompt

@click.command(help='Create metadata for a dataset in the terminal prompt')
# @click.argument('first_name')
@click.option(
    '-o', '--output', default='', 
    help='Write RDF to output file')
def create(output):
    create_dataset_prompt(output)


@click.group()
def main(args=None):
    """Generate metadata for your data"""
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)

main.add_command(create)

if __name__ == "__main__":
    sys.exit(main())
