#from app.rules import extract_cities, extract_dates
#from app.ner_model import extract_entities

#def hybrid_extract(text, citilist):
#    entities = extract_entities(text)
#    dates = extract_dates(text)
#    cities = extract_cities(text, citilist)

#    result = {
#        "source": entities.get("GPE") or (cities[0] if cities else None),
#        "destination": cities[1] if len(cities) > 1 else None,
#        "departure_date": dates[0] if dates else None,
#        "return_date": dates[1] if len(dates) > 1 else None
#    }
#
#    return result
'''
import re
from app.rules import extract_cities, extract_dates
from app.ner_model import extract_entities

def find_directional_cities(text, cities):
    if len(cities) < 2:
        return cities[0], None if cities else (None, None)
    
    text_lower = text.lower()

    # Common patterns
    patterns = [
        (r'from\s+(\w+)\s+(?:to\s+)?(\w+)', 'from_to'),
        (r'(\w+)\s*[-to]+\s*(\w+)', 'dash_or_to'),  # "X-Y" or "X to Y"
        (r'book me from\s+(\w+)\s+(\w+)', 'book_me_from'),
        (r'share\s+\w+\s+from\s+(\w+)\s+to\s+(\w+)', 'share_from_to')
    ]

    for pattern, _ in patterns:
        match = re.search(pattern, text_lower)
        if match:
            src, dst = match.groups()
            src_match = next((city for city in cities if src.lower() in city.lower()), None)
            dst_match = next((city for city in cities if dst.lower() in city.lower()), None)
            if src_match and dst_match:
                return src_match, dst_match

    # Fallback: use first and second city
    return cities[0], cities[1]

def hybrid_extract(text, citilist):
    entities = extract_entities(text)
    dates = extract_dates(text)
    cities = extract_cities(text, citilist)

    source, destination = find_directional_cities(text, cities)

    # Only use spaCy GPE if regex-based city extraction failed
    result = {
        "source": source or entities.get("GPE"),
        "destination": destination,
        "departure_date": dates[0] if dates else None,
        "return_date": dates[1] if len(dates) > 1 else None
    }

    return result

'''


import re
from app.rules import extract_cities_with_aliases, extract_dates, alias_to_city
from app.ner_model import extract_entities

def find_directional_cities(text, cities):
    if len(cities) < 2:
        return (cities[0], None) if cities else (None, None)

    text_lower = text.lower()

    patterns = [
        (r'from\s+(\w+)\s+(?:to\s+)?(\w+)', 'from_to'),
        (r'(\w+)\s*[-to]+\s*(\w+)', 'dash_or_to'),
        (r'book me from\s+(\w+)\s+(\w+)', 'book_me_from'),
        (r'share\s+\w+\s+from\s+(\w+)\s+to\s+(\w+)', 'share_from_to')
    ]

    for pattern, _ in patterns:
        match = re.search(pattern, text_lower)
        if match:
            src, dst = match.groups()
            src_match = next((city for city in cities if src.lower() in city.lower()), None)
            dst_match = next((city for city in cities if dst.lower() in city.lower()), None)
            if src_match and dst_match:
                return src_match, dst_match

    return cities[0], cities[1]

def hybrid_extract(text):
    entities = extract_entities(text)
    dates = extract_dates(text)
    cities = extract_cities_with_aliases(text, alias_to_city)

    source, destination = find_directional_cities(text, cities)

    result = {
        "source": source or entities.get("GPE"),
        "destination": destination,
        "departure_date": dates[0] if dates else None,
        "return_date": dates[1] if len(dates) > 1 else None
    }

    return result