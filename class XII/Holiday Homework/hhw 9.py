#Write a Python program to count and display the vowels of a given text.	
def vowel_check(s):
    vowels = 'aeiou'
    count = 0
    v = []
    for i in s:
        if i.lower() in vowels:
            count += 1
            v.append(i)

    print('Number of vowels in ', s, ' = ', count, '\nThe vowels involved are: ', v)

vowel_check('Nandita Krishnan')