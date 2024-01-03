def words_startwith(file_path):
    count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if word and word[0].lower() == 'a':
                        count += 1
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return

    print(f"Number of words starting with 'A' or 'a': {count}")

path = r'C:\Users\hp\Desktop\repera\coding\python\school xii\file handling\sample.txt'
words_startwith(path)  