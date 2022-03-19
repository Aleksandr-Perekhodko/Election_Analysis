counties = ["Arapahoe", 'Denver','Jefferson']

if counties[1] == 'Denver':
        print(counties[1])

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")
x = 0
while x<= 5:
    print(x)
    x = x + 1
   
    count = 7
    while count < 1:
        print("Hello World")

for county in counties:
    print(county)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voter in counties_dict.values():
    print(voter)

for county in counties_dict:
    print(counties_dict.get(county))

for county, voter in counties_dict.items():
    print(f"{county} county has {voter:,} registered voters.")

voting_data = [{"county": 'Arapahoe', "registered_voters": 422829},
               {"county": 'Denver', "registered_voters": 463353},
                {"county": 'Jefferson', "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

