import spacy

class NameEntityClient:
    
    def __init__(self, model) -> None:
        self.model = model
    
    def get_ents(self, sentence: str):
        doc = self.model(sentence)
        entities = [{'ent': ent.text, 'label': self.map_label(ent.label_)} for ent in doc.ents]
        return { 'ents':entities, 'html':""}
    
    @staticmethod
    def map_label(label):
        label_map = {
            'PERSON': 'Person',
            'NORP': 'Group',
            'LOC': 'Location',
        }
        return label_map.get(label)