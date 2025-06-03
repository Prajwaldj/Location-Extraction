
from location_extractor import LocationExtractor

def main():
    extractor = LocationExtractor()
    text = input("Enter your query: ")
    locations = extractor.extract_locations(text)
    print(f"Extracted Locations: {locations}")

if __name__ == "__main__":
     main()
