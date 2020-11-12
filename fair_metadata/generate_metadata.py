import os
import click
import urllib.parse
from datetime import date
import pkg_resources
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import RDFS, XSD, DC, DCTERMS, VOID
from SPARQLWrapper import SPARQLWrapper, TURTLE, POST, JSON

DATASET_NAMESPACE = 'https://w3id.org/d2s/dataset/'

RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
SCHEMA = Namespace("http://schema.org/")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
PROV = Namespace("http://www.w3.org/ns/prov#")
DC = Namespace("http://purl.org/dc/elements/1.1/")
DCTYPES = Namespace("http://purl.org/dc/dcmitype/")
PAV = Namespace("http://purl.org/pav/")
IDOT = Namespace("http://identifiers.org/idot/")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")


def create_dataset_prompt(output_file):
    """Create a new dataset from questions asked in the prompt"""
    metadataArray = []
    metadataArray.append({'id': 'dataset_id', 'description': 'Enter the identifier of your datasets, e.g. drugbank (lowercase, no space or weird characters)'})
    metadataArray.append({'id': 'name', 'description': 'Enter a human-readable name for your datasets, e.g. DrugBank'})
    metadataArray.append({'id': 'description', 'description': 'Enter a description for this dataset'})
    metadataArray.append({'id': 'publisher_name', 'default': 'Institute of Data Science at Maastricht University', 'description': 'Enter complete name for the institutions publishing the data and its affiliation, e.g. Institute of Data Science at Maastricht University'})
    metadataArray.append({'id': 'publisher_url', 'default': 'https://maastrichtuniversity.nl/ids', 'description': 'Enter a valid URL for the publisher homepage. Default'})
    metadataArray.append({'id': 'license', 'default': 'http://creativecommons.org/licenses/by-nc/4.0/legalcode', 'description': 'Enter a valid URL to the license informations about the original dataset'})
    metadataArray.append({'id': 'format', 'default': 'application/xml', 'description': 'Enter the format of the source file to transform'})
    metadataArray.append({'id': 'homepage', 'default': 'http://d2s.semanticscience.org/', 'description': 'Enter the URL of the dataset homepage'})
    metadataArray.append({'id': 'accessURL', 'default': 'https://www.drugbank.ca/releases/latest', 'description': 'Specify URL of the directory containing the file(s) of interest (not the direct file URL)'})
    metadataArray.append({'id': 'references', 'default': 'https://www.ncbi.nlm.nih.gov/pubmed/29126136', 'description': 'Enter the URL of a publication supporting the dataset'})
    metadataArray.append({'id': 'keyword', 'default': 'drug', 'description': 'Enter a keyword to describe the dataset'})
    metadataArray.append({'id': 'downloadURL', 'default': 'https://www.drugbank.ca/releases/5-1-1/downloads/all-full-database', 'description': 'Enter the URL to download the source file to be transformed'})
    metadataArray.append({'id': 'sparqlEndpoint', 'description': 'Enter the URL of the final SPARQL endpoint to access the integrated dataset',
        'default': 'https://graphdb.dumontierlab.com/repositories/test-vincent'})
    # metadataArray.append({'id': 'theme', 'default': 'http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C54708', 'description': 'Enter the URL to an ontology concept describing the dataset theme'})

    metadata_answers = {}
    for metadataObject in metadataArray:
        if 'default' in metadataObject:
            metadata_answers[metadataObject['id']] = click.prompt(click.style('[?]', bold=True) 
            + ' ' + metadataObject['description'] + '. Default',
            default=metadataObject['default'])
        else:
            metadata_answers[metadataObject['id']] = click.prompt(click.style('[?]', bold=True) 
            + ' ' + metadataObject['description'])

    g = create_dataset(metadata_answers)

    if output_file:
        g.serialize(destination=output_file, format='turtle')
        print("Metadata stored to " + output_file + ' 📝')
    else:
        print(g.serialize(format='turtle'))



def create_dataset(metadata):
    """Create a new dataset from provided JSON"""
    g = Graph()
    g.bind("foaf", FOAF)
    g.bind("rdf", RDF)
    g.bind("rdfs", RDFS)
    g.bind("skos", SKOS)
    g.bind("schema", SCHEMA)
    g.bind("dcat", DCAT)
    g.bind("prov", PROV)
    g.bind("dc", DC)
    g.bind("dctypes", DCTYPES)
    g.bind("dcterms", DCTERMS)
    g.bind("pav", PAV)
    g.bind("idot", IDOT)
    # g.bind("owl", OWL)

    # Summary
    summary_uri = URIRef(DATASET_NAMESPACE + metadata['dataset_id'])
    g.add((summary_uri, RDF.type, DCTYPES['Dataset']))
    g.add((summary_uri, DC.identifier, Literal(metadata['dataset_id'])))
    g.add((summary_uri, DC.description, Literal(metadata['description'])))
    g.add((summary_uri, DCTERMS.title, Literal(metadata['name'])))
    g.add((summary_uri, IDOT['preferredPrefix'], Literal(metadata['dataset_id'])))
    g.add((summary_uri, DCTERMS.license, URIRef(metadata['license'])))
    g.add((summary_uri, FOAF['page'], URIRef(metadata['homepage'])))
    g.add((summary_uri, DCAT['accessURL'], URIRef(metadata['accessURL'])))
    g.add((summary_uri, DCAT['accessURL'], URIRef(metadata['accessURL'])))
    g.add((summary_uri, DCTERMS.references, URIRef(metadata['references'])))
    g.add((summary_uri, DCAT['keyword'], Literal(metadata['keyword'])))
    g.add((summary_uri, VOID.sparqlEndpoint, URIRef(metadata['sparqlEndpoint'])))

    # Publisher
    publisher_uri = URIRef(DATASET_NAMESPACE + urllib.parse.quote(metadata['publisher_name']))
    g.add((publisher_uri, RDF.type, DCTERMS.Agent))
    g.add((publisher_uri, FOAF['name'], Literal(metadata['publisher_name'])))
    g.add((publisher_uri, FOAF['page'], Literal(metadata['publisher_url'])))
    g.add((summary_uri, DCTERMS.publisher, publisher_uri))

    # Version
    version = '1'
    version_uri = URIRef(DATASET_NAMESPACE + metadata['dataset_id'] + '/version/' + version)
    g.add((version_uri, RDF.type, DCTYPES['Dataset']))
    g.add((version_uri, DCTERMS.isVersionOf, summary_uri))
    g.add((version_uri, PAV['version'], Literal(version)))
    g.add((version_uri, DCTERMS.issued, Literal(date.today())))

    # Source distribution
    source_uri = URIRef(DATASET_NAMESPACE + metadata['dataset_id'] + '/version/' + version + '/distribution/source')
    g.add((source_uri, RDF.type, DCAT['Distribution']))
    g.add((source_uri, DCTERMS['format'], Literal(metadata['format'])))
    g.add((source_uri, DCAT['downloadURL'], Literal(metadata['downloadURL'])))

    # RDF Distribution description
    rdf_uri_string = DATASET_NAMESPACE + metadata['dataset_id'] + '/version/' + version + '/distribution/source'
    rdf_uri = URIRef(rdf_uri_string)
    g.add((rdf_uri, RDF.type, DCAT['Distribution']))
    g.add((rdf_uri, RDF.type, VOID.Dataset))
    g.add((rdf_uri, DCTERMS.source, source_uri))

    g.add((version_uri, DCAT['distribution'], source_uri))
    g.add((version_uri, DCAT['distribution'], rdf_uri))

    print(g.serialize(format='turtle'))

    if metadata['sparqlEndpoint']:
        g.add((rdf_uri, DCAT['accessURL'], Literal(metadata['sparqlEndpoint'])))
        g = generate_hcls_from_sparql(metadata['sparqlEndpoint'], rdf_uri_string, g)
    
    return g


def generate_hcls_from_sparql(sparql_endpoint, rdf_distribution_uri, g=Graph()):
    """Query the provided SPARQL endpoint to compute HCLS metadata"""
    sparql = SPARQLWrapper(sparql_endpoint)

    for filename in os.listdir(pkg_resources.resource_filename('fair_metadata', 'queries')):
        with open(pkg_resources.resource_filename('fair_metadata', 'queries/' + filename), 'r') as f:
            sparql_query = f.read().replace('?_input', rdf_distribution_uri)
            print(sparql_query)
            sparql.setQuery(sparql_query)

            sparql.setReturnFormat(TURTLE)
            results = sparql.query().convert()
            g.parse(data=results, format="turtle")
            # hcls_graph = Graph()
            # hcls_graph.parse(data=results, format="turtle")
            # g.add(hcls_graph)
            # print(results.serialize(format='ttl'))
    return g
