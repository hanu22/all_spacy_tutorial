
import spacy
nlp = spacy.load("en_core_web_lg")

ex = "There are four cars."

# Creating the doc object of example
ex_doc = nlp(ex)

ex_doc[0].shape
ex_doc[0].suffix
