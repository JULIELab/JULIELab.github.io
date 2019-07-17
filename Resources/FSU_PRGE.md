---
layout: default
---

# FSU-PRGE

[<< Back to all resources](index.html)

<br>

The **FSU** **PR**otein **GE**ne corpus was developed at the JULIE Lab Jena under supervision of Prof. Udo Hahn.<br/>
The executing scientist was Dr. Joachim Wermter.<br/>
The main annotator was Dr. Rico Pusch who is an expert in biology.<br/>
The corpus was developed in the context of the StemNet project ([http://www.stemnet.de/](http://www.stemnet.de/)).

The goals of the annotation project were
* to construct a consistent and (as far as possible) subdomain-independent/-comprehensive protein-annotated corpus
* to differentiate between protein families and groups, protein complexes, protein molecules, protein variants (e.g. alleles) and elliptic enumerations of proteins.

The corpus has the following annotation levels / entity types:
* protein
* protein_familiy_or_group
* protein_complex
* protein_variant
* protein_enum

For definitions of the annotation levels, please refer to the Proteins-guidelines-final.doc file that should be found in the same archive as this readme.

To achieve a large coverage of biological subdomains, document from multiple other protein / gene corpora were reannotated. For further coverage, new document sets were created. All documents are abstracts from PubMed/MEDLINE. The corpus is made up of the union of all the documents in the different subcorpora. Each subcorpus is stored in its own directory as follows:

All document are delivered as MMAX2 ([http://mmax2.net/](http://mmax2.net/)) annotation projects.

#### Corpus statistics:

| &nbsp;&nbsp;&nbsp;documents | 3309 (3308 since v1.1) |
| &nbsp;&nbsp;&nbsp;sentences | 36223 |
| &nbsp;&nbsp;&nbsp;tokens | 960757 |

#### Changelog:

March 26, 2019, v1.1:
* Fixed a range of MMAX2 projects that were broken in v1.0. Mostly added or removed broken sentence annotations, recreated Basedata for one project.
* Deleted the project Proteins_KIR/mmax/mmax_24742, PMID 7833836, because it did not exhibit any annotations.
* Added the JULIE Lab MMAX2 to IOB/IeXML converter program and a script to convert the whole corpus. Tested with IOB export. The project source can be found at https://github.com/JULIELab/julielab-mmax-to-iob-iexml-converter.

Download the corpus: [v1.0](/downloads/resources/fsu_prge_release_v1_0.tgz) (10MB), [v1.1](/downloads/resources/fsu_prge_release_v1_1.tgz) (19.5MB).
