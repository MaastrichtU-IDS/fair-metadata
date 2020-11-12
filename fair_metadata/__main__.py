# -*- coding: utf-8 -*-

import click
import logging
import sys

from fair_metadata.generate_metadata import create_dataset_prompt, generate_hcls_from_sparql

@click.command(help='Create metadata for a dataset in the terminal prompt')
# @click.argument('first_name')
@click.option(
    '-o', '--output', default='', 
    help='Write RDF to output file')
def create(output):
    create_dataset_prompt(output)


@click.command(help='Generate descriptive metadata (about types and relations) for a SPARQL endpoint')
@click.argument('sparql_endpoint')
@click.option(
    '-u', '--dataset-uri', default='https://w3id.org/d2s/distribution/default', 
    help='URI of the dataset distribution')
@click.option(
    '-o', '--output', default='', 
    help='Write RDF to output file')
def analyze(sparql_endpoint, dataset_uri, output):
    g = generate_hcls_from_sparql(sparql_endpoint, dataset_uri)
    if output:
        g.serialize(destination=output, format='turtle')
        print("Metadata stored to " + output + ' 📝')
    else:
        print(g.serialize(format='turtle'))



@click.group()
def main(args=None):
    """Generate metadata for your data"""
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)

main.add_command(create)
main.add_command(analyze)

if __name__ == "__main__":
    sys.exit(main())
