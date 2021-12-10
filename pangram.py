import string
alphabet = set(string.ascii_lowercase)
def ispangram(string):
    return set(string.lower()) >= alphabet
string = 'The quickfox jumps over the lazy dog brown '
if(ispangram(string)==True):
   print("The string is a pangram.")
else:
   print("The string is not a pangram.")
