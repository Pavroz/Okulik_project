import csv

with open('data.csv', newline='') as csv_file:
    file_data = csv.reader(csv_file)

    data = []
    for row in file_data:
        data.append(row)

print(data)


for row in data:
    last_name, name, city = row
    print(f'Name: {name}, laste name: {last_name}, city: {city}')