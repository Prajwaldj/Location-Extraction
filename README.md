# Location Extraction
## A Python-based NLP application using SpaCy that takes a natural language prompt and identifies locations mentioned in the input.

# Used Technologies

## Language
  1. Python
  2. ScaPy models/library

## IDE & Tools
  1. Visual Studio (Python Tools Installed)

## Installation and execution
1. https://www.python.org/downloads/     *for python installation
2. pip install spacy                     *for spacy library installation
3. Install dependencies
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
4. python main.py  * for execution 
  
* Visual Studio is Used to Edit the Code and To Test the project files.

## It Contains 5 Portals :
  1. main.py  ## Entry point script
  2. location_extractor.py  ## NLP model logic
  3. test_location_extractor.py  ## Test cases for location extraction
  4. requirements.txt  ## Dependencies
  5. README.md   ## Documentation

## Sample input/output :
 1. input:
    Enter your query: "List properties in Baner and Wakad."

 2. Output:
    Extracted Locations:["Baner","Wakad"]

    if no location detected:
    Extracted Locations:["No location found"]


## How to run tests
 python test_locatoin_exetractor.py
  
