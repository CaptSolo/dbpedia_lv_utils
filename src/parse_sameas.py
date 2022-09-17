#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Parses DBpedia sameAs_lang=en.ttl.bz2 file and generates corresponding links
for Latvian DBpedia:
 - links to other language DBpedias
 - links to Wikidata, etc.
"""

from itertools import islice
import bz2
import re


# limitation:
#  - if we use the English DBpedia sameAs file, we will not have sameAs links
#    for Latvian Wikipedia pages that do not have a version in English DBpedia.

FNAME = "sameAs_lang=en.ttl.bz2"


def read_bzip2_file(filename):

    with bz2.open(filename, "rt", encoding="utf8") as inf:
        for line in inf:
            yield line.strip()


def get_triples(data):

    re_triples = re.compile(r"^<([^>]+)> <([^>]+)> <([^>]+)> .$")

    for record in data:
        res = re_triples.match(record) 
        
        if res and res.group(2) == "http://www.w3.org/2002/07/owl#sameAs":
            # print(f"Match OK: {record}")
            yield res.group(1, 2, 3)

        else:
            print(f"Error processing line: {record}")


def make_clusters(triples):

    buf = []
    cur_subject = None    

    # assuming that all the triples here are owl:sameAs triples

    for triple in triples:

        if triple[0] == cur_subject:

            buf.append(triple)

        else:

            yield(buf)

            buf = []
            cur_subject = triple[0]
            
            buf.append(triple)

    # yield the last cluster
    yield(buf)


def filter_lv_clusters(clusters):

    for cluster in clusters:

        lv_dbpedia = (item[2].startswith("http://lv.dbpedia.org/")
            for item 
            in cluster)

        # cluster contains a URI from Latvian DBpedia
        if any(lv_dbpedia):

            yield(cluster)


def transform_to_lv_clusters(clusters):

    for cluster in clusters:

        en_URI = cluster[0][0]

        # assuming that there is exactly one LV DBpedia URI in the cluster
        lv_URI = [item[2]
            for item 
            in cluster
            if item[2].startswith("http://lv.dbpedia.org/")][0]

        other_URIs = [item[2]
            for item 
            in cluster
            if not item[2].startswith("http://lv.dbpedia.org/")]

        other_URIs.append(en_URI)

        res = (lv_URI, other_URIs)

        yield res


def construct_nt_output(lv_clusters):

    # cluster = a tuple (LV_URI, list_of_other_URIs)

    for lv_URI, other_URIs in lv_clusters:

        for URI in other_URIs:

            yield f"<{lv_URI}> <http://www.w3.org/2002/07/owl#sameAs> <{URI}> ."

            
def main():

    data = read_bzip2_file(FNAME)

    triples = get_triples(data)

    clusters = make_clusters(triples)
    clusters_lv = filter_lv_clusters(clusters)

    # clusters_lv = islice(clusters_lv, 100)

    clusters_lv_transformed = transform_to_lv_clusters(clusters_lv)

    output_ntriples = construct_nt_output(clusters_lv_transformed)

    for line in output_ntriples:
        print(line)


# ------------------------------------------------------------ 

if __name__ == "__main__":
    main()
