num = int(input("Enter a two digit number: "))

ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}


if num not in range(10,100):
    print("invalid input")
else:
    if num <= 19:
        print(num, '--> ', ones[num])
    if 20<=num<=99:
        a = []
        
        for i in str(num):
            a.append(int(i))
        prefix = int(a[0])
        suffix = int(a[1])
        out = tens[prefix] + " " + ones[suffix]
        print(out)
