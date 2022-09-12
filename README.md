# all_spacy_tutorial

# What does Sapcy use as word embeddings
https://stackoverflow.com/questions/44492430/how-does-spacy-use-word-embeddings-for-named-entity-recognition-ner
spaCy does use word embeddings for its NER model, which is a multilayer CNN. 
There's a quite a nice video that Matthew Honnibal, the creator of spaCy made, about how its NER works here.
All three English models use GloVe vectors trained on Common Crawl,
 but the smaller models "prune" the number of vectors by having similar words mapped to the same vector link.

It's quite doable to add custom vectors. 
There's an overview of the process in the spaCy docs, plus some example code on Github.
