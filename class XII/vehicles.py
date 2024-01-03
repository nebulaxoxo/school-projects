import pickle
def showfile(file_path):
    try:
        with open(file_path, 'rb+') as file:
            record_count = 0

            while True:
                try:
                    record = pickle.load(file)
                    vehicletype, no_of_wheels = record

                    print(f"Vehicle Type: {vehicletype}")
                    print(f"No. of Wheels: {no_of_wheels}")
                    print('-' * 30)

                    record_count += 1
                except EOFError:
                    break  # Reached the end of the file

            print(f"Number of Records: {record_count}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return


