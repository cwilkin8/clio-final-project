from bs4 import BeautifulSoup
import requests
import pandas as pd

# create dataframes
immigration_df = {'family_record_num': [],
                  'arrivalDate': [],
                  'familyName': [],
                  'destination': [],
                  'departureCity': [],
                  'origin': [],
                  'people': [],
                  'departureDate': [],
                  'vessel': []}

family_df = {'family_record_num': [],
             'name': [],
             'age': [],
             'sex': [],
             'occupation': []}

print('DataFrames created. Beginning scraping............')
# loop through pages to add info to tables
for i in range(1, 83073):

    url = 'http://ghf.destinationnext.com/immigration/SearchDetails.aspx?ID=' + str(i)

    response = requests.get(url)

    soup = BeautifulSoup(response.text,'html.parser')

    immigration_df['family_record_num'].append(i)

    arrivalDate = soup.find('span', {'id': 'lblArrivalDate'})
    immigration_df['arrivalDate'].append(arrivalDate.text.strip())

    familyName = soup.find('span', {'id': 'lblFamilyName'})
    immigration_df['familyName'].append(familyName.text.strip())

    destination = soup.find('span', {'id': 'lblDestination'})
    immigration_df['destination'].append(destination.text.strip())

    departure = soup.find('span', {'id': 'lblDeparture'})
    immigration_df['departureCity'].append(departure.text.strip())

    origin = soup.find('span', {'id': 'lblOrigin'})
    immigration_df['origin'].append(origin.text.strip())

    people = soup.find('span', {'id': 'lblPeople'})
    immigration_df['people'].append(people.text.strip())

    departureDate = soup.find('span', {'id': 'lblDepatureDate'})
    immigration_df['departureDate'].append(departureDate.text.strip())

    ship = soup.find('span', {'id': 'lblShip'})
    immigration_df['vessel'].append(ship.text.strip())

    family = soup.find('table', {'id': 'table1'})
    members = family.find_all('div')
    for member in members:
        vals = member.find_all('span')
        family_df['family_record_num'].append(i)
        family_df['name'].append(vals[0].text.strip())
        family_df['age'].append(vals[1].text.strip())
        family_df['sex'].append(vals[2].text.strip())
        family_df['occupation'].append(vals[3].text.strip()) 
        
    if i % 831 == 0:
        print('{}% done!'.format(i // 831))

immigration_df = pd.DataFrame.from_dict(immigration_df)
family_df = pd.DataFrame.from_dict(family_df)

immigration_df.to_csv('immigration.csv')
family_df.to_csv('immigrant_families.csv')
print('Scraping finished. DataFrames converted to CSVs and .csv files added to current directory.')
