import os

var1 = os.system('''uname -r | cut -d '-' -f1 | cut -d '.' -f1''')
var2 = os.system('''uname -r | cut -d '-' -f1 | cut -d '.' -f2''')
var3 = os.system('''uname -r | cut -d '-' -f1 | cut -d '.' -f3''')

if var1 == 5 & var2 == 16 & var3 == 11 or var1 == 5 & var2 == 15 & var3 == 25 or var1 == 5 & var2 == 10 & var3 == 102 :
    print ("Not Vulnerable")
else:
    print("Vulnerable")