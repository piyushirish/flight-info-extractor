import re

def extract_dates(text):
    return re.findall(r'\d{1,2}(?:st|nd|rd|th)?\s?\w{3,}', text)

#def extract_cities(text, citilist):
#   text_lower = text.lower()
 #   return [city.title() for city in citilist if city.lower() in text_lower]

'''def extract_cities_with_aliases(text, alias_to_city):
    text_lower = text.lower()
    found = []

    for alias, city in alias_to_city.items():
        index = text_lower.find(alias)
        if index != -1:
            found.append((index, city))

    # Sort by position in text
    found.sort()
    
    # Remove duplicates while preserving order
    seen = set()
    ordered_unique = []
    for _, city in found:
        if city not in seen:
            seen.add(city)
            ordered_unique.append(city)

    return ordered_unique
'''

import re

def extract_dates(text):
    return re.findall(r'\d{1,2}(?:st|nd|rd|th)?\s?\w{3,}', text)

alias_groups = {
    'Agartala': ['Agartala'],
    'Agra': ['Agra'],
    'Ahmedabad': ['Ahmedabad', 'AMD'],
    'Aizawl': ['Aizawl', 'Aizwal'],
    'Amritsar': ['Amritsar', 'ATQ'],
    'Aurangabad': ['Aurangabad'],
    'Bagdogra': ['Bagdogra'],
    'Bengaluru': ['Bengaluru', 'Bangalore', 'BLR'],
    'Bhopal': ['Bhopal', 'BHO'],
    'Bhubaneswar': ['Bhubaneswar', 'BBI'],
    'Bhutan': ['Bhutan'],
    'Chandigarh': ['Chandigarh', 'IXC'],
    'Chennai': ['Chennai', 'MAA'],
    'Coimbatore': ['Coimbatore'],
    'Dehradun': ['Dehradun'],
    'Delhi': ['Delhi', 'delhi', 'DEL'],
    'Dibrugarh': ['Dibrugarh'],
    'Dimapur': ['Dimapur'],
    'Durgapur': ['Durgapur'],
    'Gaya': ['Gaya'],
    'Goa': ['Goa', 'GOI', 'GOX'],
    'Gorakhpur': ['Gorakhpur'],
    'Guwahati': ['Guwahati', 'GAU'],
    'Gwalior': ['Gwalior'],
    'Hyderabad': ['Hyderabad', 'HYD'],
    'Imphal': ['Imphal'],
    'Indore': ['Indore', 'IDR'],
    'Jabalpur': ['Jabalpur'],
    'Jaipur': ['Jaipur', 'JAI'],
    'Jammu': ['Jammu'],
    'Jodhpur': ['Jodhpur'],
    'Jorhat': ['Jorhat'],
    'Kannur': ['Kannur'],
    'Kanpur': ['Kanpur'],
    'Kochi': ['Kochi', 'COK'],
    'Kolkata': ['Kolkata', 'Calcutta', 'KOLKATTA', 'CCU'],
    'Kozhikode': ['Kozhikode'],
    'Lucknow': ['Lucknow', 'LKO'],
    'Madurai': ['Madurai'],
    'Mangaluru': ['Mangaluru'],
    'Mumbai': ['Mumbai', 'BOM'],
    'Nagpur': ['Nagpur', 'NAG'],
    'Patna': ['Patna', 'PAT'],
    'Port Blair': ['Port Blair'],
    'Prayagraj': ['Prayagraj'],
    'Pune': ['Pune', 'PNQ'],
    'Raipur': ['Raipur', 'RPR'],
    'Rajkot': ['Rajkot'],
    'Ranchi': ['Ranchi', 'IXR'],
    'Shillong': ['Shillong'],
    'Siliguri': ['Siliguri'],
    'Srinagar': ['Srinagar', 'SXR'],
    'Surat': ['Surat'],
    'Thiruvananthapuram': ['Thiruvananthapuram', 'TRV'],
    'Tiruchirappalli': ['Tiruchirappalli'],
    'Tirupati': ['Tirupati'],
    'Udaipur': ['Udaipur'],
    'Varanasi': ['Varanasi', 'VNS'],
    'Vijayawada': ['Vijayawada'],
    'Visakhapatnam': ['Visakhapatnam']
}

alias_to_city = {}
for city, aliases in alias_groups.items():
    for alias in aliases:
        alias_to_city[alias.lower()] = city

def extract_cities_with_aliases(text, alias_to_city):
    text_lower = text.lower()
    found = []

    for alias, city in alias_to_city.items():
        index = text_lower.find(alias)
        if index != -1:
            found.append((index, city))

    found.sort()
    seen = set()
    ordered_unique = []
    for _, city in found:
        if city not in seen:
            seen.add(city)
            ordered_unique.append(city)

    return ordered_unique
