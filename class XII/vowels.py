def vowelwords(input_file, output_file):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    try:
        with open(input_file, 'r') as file1, open(output_file, 'w') as file2:
            for line in file1:
                words = line.split()
                non_vowel_words = [word for word in words if word[0].upper() not in vowels]
                file2.write(" ".join(non_vowel_words) + '\n')
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
samp_path = r"C:\Users\hp\Desktop\repera\coding\python\school xii\file handling\sample.txt"
vowelwords(samp_path, 'output.txt')  