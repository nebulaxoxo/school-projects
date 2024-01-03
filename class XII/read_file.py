def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
path = r'C:\Users\hp\Desktop\repera\coding\python\school xii\file handling\sample.txt'
read_file(path)  