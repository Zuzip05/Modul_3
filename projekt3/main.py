"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Zuzana Pechova
email: pechovazuzana@seznam.cz
"""

import requests
from bs4 import BeautifulSoup
import csv
import urllib
import sys

# Argument validation
if len(sys.argv) != 3:
    print("Error: You must provide two arguments - URL and output file name.")
    sys.exit(1)

url = sys.argv[1]
csv_filename = sys.argv[2]

# Check if the URL contains "volby.cz", which should be a valid URL
if "volby.cz" not in url:
    print("Error: URL must contain 'volby.cz'.")
    sys.exit(1)

# Send an HTTP request to the main page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#print current status of the script progress
print ("Stahuji data z vybraného URL:",url)

# List for storing results
data = []

# List for storing political party names (CSV header)
party_names = []

# Search all <td> tags with class "number" for municipality codes
for td_nr in soup.find_all('td', class_='cislo'):
    # We extract the community code from the <a> tag
    link = td_nr.find('a')
    if link and 'href' in link.attrs:
        code = link.attrs['href'].split('xobec=')[-1].split('&')[0]
        
        # We find the corresponding municipality name in the <td class="overflow_name"> column
        td_name = td_nr.find_next('td', class_='overflow_name')
        if td_name:
            name = td_name.text.strip()
            
            # We will create a URL for a subpage of a specific municipality
            parsed_url = urllib.parse.urlparse(url)
            query_params = urllib.parse.parse_qs(parsed_url.query)
            county_code = query_params.get('xkraj', [None])[0]
            code_nr = query_params.get('xnumnuts', [None])[0]
            url_suppage = f"https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj={county_code}&xobec={code}&xvyber={code_nr}"
            
            # We will send a request for a subpage.
            response = requests.get(url_suppage)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Number of voters on the register
            registered = soup.find('td', class_='cislo', headers='sa2')
            if registered:
                registered = registered.text.strip()
            else:
                registered = "N/A"

            # Number of envelopes
            envelopes = soup.find('td', class_='cislo', headers='sa3')
            if envelopes:
                envelopes = envelopes.text.strip()
            else:
                envelopes = "N/A"

            # Number of valid
            valid = soup.find('td', class_='cislo', headers='sa6')
            if valid:
                valid = valid.text.strip()
            else:
                valid = "N/A"

            # Get party names and their votes
            parties = soup.find_all('td', class_='overflow_name')
            votes = soup.find_all('td', class_='cislo', headers=["t1sa2 t1sb3", "t2sa2 t2sb3"])

            # Save page names for the CSV header if they are not already added
            if not party_names:
                for party in parties:
                    party_names.append(party.text.strip())

            # Save the vote counts
            votes_list = []
            for vote in votes:
                votes_list.append(vote.text.strip())

            # We will add the municipality data + results to the list
            data.append([code, name, registered, envelopes, valid] + votes_list)

#print current status of the script progress
print ("Ukládám do souboru")

# Open CSV file for writing
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Writing header to CSV
    header = ['code', 'location', 'registered', 'envelopes', 'valid'] + party_names
    writer.writerow(header)
    
    # Writing data to CSV
    for village in data:
        writer.writerow(village)

#print current status of the script progress
print(f"Data was saved to a file {csv_filename}")