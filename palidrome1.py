s = 'malayalam'
s = s.casefold()
rev_s= reversed(s)
if list(s) == list(rev_s):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
