import pytest

from fair_metadata.generate_metadata import create_dataset

def test_create_dataset_metadata():
    test_metadata = {
        'dataset_id': 'testdataset',
        'name': 'Test Dataset',
        'description': 'Test dataset description',
        'publisher_name': 'Institute of Data Science at Maastricht University',
        'publisher_url': 'https://maastrichtuniversity.nl/ids',
        'license': 'http://creativecommons.org/licenses/by-nc/4.0/legalcode',
        'format': 'application/xml',
        'homepage': 'http://d2s.semanticscience.org/',
        'accessURL': 'https://www.drugbank.ca/releases/latest',
        'references': 'https://www.ncbi.nlm.nih.gov/pubmed/29126136',
        'keyword': 'drug',
        'downloadURL': 'https://www.drugbank.ca/releases/5-1-1/downloads/all-full-database',
        'sparqlEndpoint': 'https://graphdb.dumontierlab.com/repositories/test-vincent'
    }
    g = create_dataset(test_metadata)
    print(len(g))
    assert len(g) > 3
