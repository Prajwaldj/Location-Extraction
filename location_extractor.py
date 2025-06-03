import spacy

class LocationExtractor:
    def __init__(self, model="en_core_web_sm"):
        self.nlp = spacy.load(model)

    def extract_locations(self, text):
        doc = self.nlp(text)
        locations = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC"]]
        return locations if locations else ["No location found"]

if __name__ == "__main__":
    extractor = LocationExtractor()
    sample_text = "List properties in Baner and Wakad."
    print(extractor.extract_locations(sample_text))