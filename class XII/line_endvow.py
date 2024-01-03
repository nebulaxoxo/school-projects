def count_lines_ending_with_vowel(file_path):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and line[-1].lower() in vowels:
                    count += 1
        print(f"Number of lines ending with a vowel: {count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
path = r'C:\Users\hp\Desktop\repera\coding\python\school xii\file handling\sample.txt'

count_lines_ending_with_vowel(path) 