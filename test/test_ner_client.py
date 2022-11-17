import unittest
from ner_client import NameEntityClient
from test_doubles import NerModelTestDouble
 
class TestNerClient(unittest.TestCase):
     
    # { ents: [{}],
    #   html: "<span>..."}
     
    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NameEntityClient(model)
        ents = ner.get_ents('')
        self.assertIsInstance(ents,dict)
        
    def test_get_ents_returns_dictionary_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NameEntityClient(model)
        ents = ner.get_ents('Madison is a city in Wisconsin')
        self.assertIsInstance(ents,dict)


    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Laurent Fressinet', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NameEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Laurent Fressinet', 'label': 'Person'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])
        

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Lithuanian', 'label_': 'NORP'}]
        model.returns_doc_ents(doc_ents)
        ner = NameEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Lithuanian', 'label': 'Group'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])
        

    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'the ocean', 'label_': 'LOC'}]
        model.returns_doc_ents(doc_ents)
        ner = NameEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'the ocean', 'label': 'Location'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])
        