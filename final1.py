import csv
dataset1=[]
dataset2=[]

with open ("dataset.csv","r")as f:
    csv_reader= csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)

with open ("dataset1_sorted.csv","r")as f:
    csv_reader= csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)

headers_1= dataset1[0]
planet_data_1= dataset1[1:]
headers_2= dataset2[0]
planet_data_2= dataset2[1:]

headers= headers_1+headers_2
planet_data=[]
for index, datarow in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open ("final.csv", "a+") as f:
    csv_writer= csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)