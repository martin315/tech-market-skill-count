from email import header
import json
import csv
import os
#from collections import OrderedDict

data_path = "./data"
sample_data_01 = "./sample_data/SampleData_01.json"
sample_data_02 = "./data/Barcalona.json"
tech_path = "./tech.txt"

def main():
    # Collect a list of headers from tech.txt
    tech_file = open(tech_path, "r")
    headers =  tech_file.read().split()
    headers.insert(0, "City")

    # Create tech dictionary
    tech_dict = create_tech_dictionary(headers)

    dir_list = os.listdir(data_path)


    # DictWriter
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()

        for city_name in dir_list:
            tech_dict["City"] = city_name

            f = open(data_path + "/" + city_name, "r", encoding='utf-8')
            data = json.load(f)

            for post in data:
                for k in range(1,len(tech_dict)):

                    if (" " + headers[k].lower()) in post["description"].lower():
                        tech_dict[headers[k]] += 1

            writer.writerow(tech_dict)
            #reset tech dictionary
            tech_dict = create_tech_dictionary(headers)

    f.close()
    tech_file.close()
    return

# function to create and reset the tech_dict
def create_tech_dictionary(headers):
    tech_dict = {headers[0]: ""}
    tech_dict.update({skill: 0 for skill in headers[1:]}) 
    return tech_dict

if __name__ == "__main__":
    main()