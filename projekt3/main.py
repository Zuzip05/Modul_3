"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Zuzana Pechova
email: pechovazuzana@seznam.cz
"""

#import libraries
import requests
from bs4 import BeautifulSoup
import csv
import urllib
import sys
from typing import List, Tuple

# Argument validation
def validate_arguments() -> Tuple[str, str]:
    """Validates the command-line arguments."""
    if len(sys.argv) != 3:
        print("Error: You must provide two arguments - URL and output file name.")
        sys.exit(1)

    # Two required arguments
    url = sys.argv[1]
    csv_filename = sys.argv[2]

    # Check if the URL contains "volby.cz", which should be a valid URL
    if "volby.cz" not in url:
        print("Error: URL must contain 'volby.cz'.")
        sys.exit(1)

    return url, csv_filename

# Send an HTTP request to the main page
def fetch_soup(url: str) -> BeautifulSoup:
    """Fetches the HTML content of the URL and returns a BeautifulSoup object."""
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def get_municipality_data(url: str, soup: BeautifulSoup) -> List[List[str]]:
    """Extracts municipality data from the page and returns it as a list of lists."""

    # List for storing results
    data = []

    # List for storing political party names (CSV header)
    party_names = []

    # Search all <td> tags with class "cislo" for municipality codes
    for td_nr in soup.find_all('td', class_='cislo'):
        link = td_nr.find('a')
        if link and 'href' in link.attrs:
            code = link.attrs['href'].split('xobec=')[-1].split('&')[0]

            # We find the corresponding municipality name in the <td class="overflow_name"> column
            td_name = td_nr.find_next('td', class_='overflow_name')
            if td_name:
                name = td_name.text.strip()

                # Create a URL for a subpage of a specific municipality
                parsed_url = urllib.parse.urlparse(url)
                query_params = urllib.parse.parse_qs(parsed_url.query)
                county_code = query_params.get('xkraj', [None])[0]
                code_nr = query_params.get('xnumnuts', [None])[0]
                if county_code and code_nr:
                    url_suppage = f"https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj={county_code}&xobec={code}&xvyber={code_nr}"

                    # Send a request for the subpage
                    response = requests.get(url_suppage)
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Extract results
                    registered = soup.find('td', class_='cislo', headers='sa2')
                    registered = registered.text.strip() if registered else "N/A"

                    envelopes = soup.find('td', class_='cislo', headers='sa3')
                    envelopes = envelopes.text.strip() if envelopes else "N/A"

                    valid = soup.find('td', class_='cislo', headers='sa6')
                    valid = valid.text.strip() if valid else "N/A"

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

                    # Add the municipality data + results to the list
                    data.append([code, name, registered, envelopes, valid] + votes_list)

    return data, party_names

# Writing data to csv
def save_to_csv(filename: str, header: List[str], data: List[List[str]]) -> None:
    """Saves the extracted data to a CSV file."""
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for row in data:
                writer.writerow(row)
    except Exception as e:
        print(f"Error saving to CSV: {e}")
        sys.exit(1)

# Main function
def main() -> None:
    """Main function that coordinates the data extraction and saving process."""
    # Step 1: Validate arguments
    url, csv_filename = validate_arguments()

    # Step 2: Fetch and parse the main page
    print(f"Stahuji data z vybraného URL: {url}")
    soup = fetch_soup(url)

    # Step 3: Extract data
    print("Získávám data z vybraných obcí...")
    data, party_names = get_municipality_data(url, soup)

    # Step 4: Save data to CSV
    print("Ukládám do souboru...")
    header = ['code', 'location', 'registered', 'envelopes', 'valid'] + party_names
    save_to_csv(csv_filename, header, data)

    # Step 5: Notify the user
    print(f"Data byla uložena do souboru {csv_filename}")


if __name__ == "__main__":
    main()