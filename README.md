# Latvian DBpedia utils
## Tools for generating and processing Latvian DBpedia data

### parse_sameas.py

`parse_sameas.py` processes DBpedia sameAs link file and generates `owl:sameAs` statements for the Latvian DBpedia in the form of `<dbpedia_lv_URI> owl:sameAs <other_language_URI>`.

DBpedia sameAs links can be found here:
* https://databus.dbpedia.org/vehnem/replaced-iris/sameAs/2022.03.01/

A limitation of this approach (using links from the English DBpedia sameAs file listed above) is that this program will not generate links for Latvian DBpedia URIs for which there are no matching English DBpedia resources. That will be the case for Latvian Wikipedia pages that do not have a matching English Wikipedia page.

  These missing LV DBpedia links will have to be generated either from Latvian Wikipedia or Wikidata.
  
