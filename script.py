from email import header
import json
import csv
#from collections import OrderedDict

data_path = "./data"
sample_data_01 = "./sample_data/SampleData_01.json"
sample_data_02 = "./data/Berlin.json"
tech_path = "./tech.txt"

def main():
    # Collect a list of headers from tech.txt
    tech_file = open(tech_path, "r")
    headers =  tech_file.read().split()
    headers.insert(0, "City")

    tech_dict = {headers[0]: ""}
    tech_dict.update({skill: 0 for skill in headers[1:]}) 


    print(headers)
    print(tech_dict)

    # DictWriter Example
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        writer.writeheader()

        tech_dict["City"] = "Madrid"
        # Open data file with json library
        # Note: this is for only one file, we gotta loop
        f = open(sample_data_02, "r", encoding='utf-8')
        data = json.load(f)

        for post in data:
            for k in range(1,len(tech_dict)):

                if headers[k].lower() in post["description"].lower():
                    tech_dict[headers[k]] += 1

            #print(i["description"])
            #print("software" in i["description"])
        writer.writerow(tech_dict)
        # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    f.close()
    tech_file.close()

if __name__ == "__main__":
    main()