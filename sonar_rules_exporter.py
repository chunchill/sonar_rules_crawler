import requests
from bs4 import BeautifulSoup
import pandas as pd


def export_rules(language):
    # Construct the URL with the specified language
    url = f'https://rules.sonarsource.com/{language}/'

    # Send a request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all rule names
    rule_names = [h3.get_text().strip() for h3 in soup.select('ol li a h3')]

    # Create a DataFrame
    df = pd.DataFrame(rule_names, columns=['Rule Name'])

    # Add a column for Rule Number at the beginning of the DataFrame
    df.insert(0, 'Rule Number', range(1, len(df) + 1))

    # Construct the path for the Excel file
    excel_path = f'./output/SonarQube_{language.capitalize()}_Rules.xlsx'
    df.to_excel(excel_path, index=False)

    return excel_path

def export_multiple_languages(languages):
    for language in languages:
        export_rules(language)
        print(f'Exported rules for {language}')


