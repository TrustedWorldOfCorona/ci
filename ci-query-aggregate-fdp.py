"""
Query the different TWOC FAIR Data Points and return the aggregate results.
"""

import requests
import sys, os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "twoc-data-visiting-prototype"))
import fdp

from rdflib import Namespace, Literal
from rdflib.namespace import RDF
from SPARQLWrapper import SPARQLWrapper2

INDEX = "https://twoc-index.fair-dtls.surf-hosted.nl"
ENTRIES_ENDPOINT = INDEX + "/index/entries/all"

DCAT = Namespace("http://www.w3.org/ns/dcat#")

with open("./twoc-data-visiting-prototype/queries/dexamethasone.sparql") as file:
    query = file.read()

client = fdp.Client()
distributionFilter = lambda g: (None, RDF.type, DCAT.Distribution) in g

aggregate_results = {}

for entry in requests.get(ENTRIES_ENDPOINT).json():
    print("Found entry " + entry["clientUrl"])
    try:
        for distribution in client.getResources(entry["clientUrl"], distributionFilter):
            for subject in distribution.subjects(RDF.type, DCAT.Distribution):
                if (subject, DCAT.mediaType, Literal("application/sparql-results+json")) not in distribution:
                    continue

                accessURL = distribution.value(subject, DCAT.accessURL)
                
                sparql = SPARQLWrapper2(accessURL)
                sparql.setQuery(query)

                for binding in sparql.query().bindings:
                    for k, v in binding.items():
                        value = int(v.value)
                        aggregate_results[k] = aggregate_results[k] + value if k in aggregate_results else value
    except:
        print("Failed to query entry")
        continue

for k,v in aggregate_results.items():
    print(f"{k}: {v}")

total_patients = sum(aggregate_results.values())
print("Total patients: ", total_patients)
if total_patients == 0:
    print("Expected a patient total greater than zero")
    sys.exit(1)
