#Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters.
#Sample String: PythonProgramminG
#Expected Output: Original String: Python Programming No. of Uppercase characters: 3
#No. of Lowercase characters: 14

def counter(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["upper"])
    print ("No. of Lower case Characters : ", d["lower"])

counter('PythonProgramminG')