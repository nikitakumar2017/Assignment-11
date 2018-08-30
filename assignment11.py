#Q.1- Write a python code to find a valid email address from a text.
import re
string=input("Enter a string from which you want to extract email ")
s=re.search('[a-zA-Z][a-zA-Z0-9_.]*[@](gmail.com|yahoo.com)',string)
if s!=None:
    print('Match Available ');
    print('First occurence is at: {},End: {},Pattern found: {}'.format(s.start(),s.end(),s.group()))
else:
    print('Match not available')

#Q.2- Write a python program to find a valid Indian phone number from a text.
#(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
import re
string=input("Enter a string from which you want to extract phone no. ")
matcher=re.finditer('\+91-[6-9][0-9]{9}',string)
for m in matcher:
    print("Match is at: {},End:{},Group found: {} ".format(m.start(),m.end(),m.group()))


