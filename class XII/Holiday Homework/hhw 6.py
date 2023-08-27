#Write a Python program to check whether a string starts with specified characters.
#Note: In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. 
#It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed
#number of positions down the alphabet. 
#For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. 
#The method is named after Julius Caesar, who used it in his private correspondence.
def spec_char(s,x):
    if s.lower().startswith(x.lower()) == True:
        return True
    else:
        return False

print(spec_char('Delhi Public School Ghaziabad Meerut Road', 'del'))
print(spec_char('Delhi Public School Ghaziabad Meerut Road', 'Road'))

