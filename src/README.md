## Extract links for Latvian DBpedia 

In order to extract inter-language and Wikidata links use:

`python parse_sameas.py`

It will extract links from `sameAs_lang=en.ttl.bz2` file in the `../data` folder and send RDF ntriples output to standard output.

Example output:
```
<http://lv.dbpedia.org/resource/Sveika,_pasaule> <http://www.w3.org/2002/07/owl#sameAs> <http://es.dbpedia.org/resource/Hola_mundo> .
<http://lv.dbpedia.org/resource/Sveika,_pasaule> <http://www.w3.org/2002/07/owl#sameAs> <http://et.dbpedia.org/resource/Hello_world> .
<http://lv.dbpedia.org/resource/Sveika,_pasaule> <http://www.w3.org/2002/07/owl#sameAs> <http://eu.dbpedia.org/resource/Kaixo_mundua> .
<http://lv.dbpedia.org/resource/Sveika,_pasaule> <http://www.w3.org/2002/07/owl#sameAs> <http://fa.dbpedia.org/resource/برنامه_«سلام،_دنیا!»> .
<http://lv.dbpedia.org/resource/Sveika,_pasaule> <http://www.w3.org/2002/07/owl#sameAs> <http://fi.dbpedia.org/resource/Hei_maailma_-ohjelma> .
```

### Filtering output (to reduce size)

Assumption: the output of `parse_sameas.py` is saved in file `sameAs_lv_output.nt.bz2` in the current directory.

In order to reduce size of the resulting RDF file you may want to leave links just to a few language versions (e.g. links to the English DBpedia and Wikidata). Here is how you can filter the resulting links and save them to another bzip2 archive:

`grep -J -E "http://dbpedia.org|wikidata.org" sameAs_lv_output.nt.bz2 | bzip2 - > sameAs_lv_output_filtered.nt.bz2`

