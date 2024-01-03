import csv

def AddRecord():
    model_no = input("Enter Model Number: ")
    mobile_name = input("Enter Mobile Name: ")
    manufacturer = input("Enter Manufacturer: ")
    price = input("Enter Price: ")

    record = [model_no, mobile_name, manufacturer, price]

    try:
        with open('Mobile_Phones.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(record)
        print("Record added successfully.")
    except Exception as e:
        print("Error:", e)

def Find():
    manufacturer_to_find = input("Enter the manufacturer to search (e.g., Apple): ")

    try:
        with open('Mobile_Phones.csv', 'r') as file:
            reader = csv.reader(file)
            found_records = [record for record in reader if record[2].lower() == manufacturer_to_find.lower()]

        if found_records:
            print("Found Records:")
            for record in found_records:
                print(record)
        else:
            print("No records found for manufacturer:", manufacturer_to_find)

    except Exception as e:
        print("Error:", e)

AddRecord()
Find()
