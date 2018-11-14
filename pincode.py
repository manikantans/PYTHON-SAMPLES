import csv
import re
import matplotlib as plt
from colorama import init, Fore, Back, Style
init(convert=True)

path="C:\\TEMP\\mani\\ml\\machineLearninG\\pincode.csv"
file=open(path,newline='')
reader=csv.reader(file)
data=[row for row in (csv.reader(open(path)))]
code=input("enter a code: ")
codeTest=code
if re.search(',',codeTest):
    code1=code.split(sep=",",maxsplit=-1)
else:
    code1=["null","null"]

rc=0
j=0
for row in reader:
    match=re.search(str.upper(code),str.upper(row[0]))
    match2=re.search(str.upper(code1[1]),str.upper(row[7]))
    matchcode=re.search(str.upper(code1[0]),str.upper(row[0]))
    if code==row[1] or match:
        j=j+1
        print("----------------------------------------------------")
        print(Fore.BLUE ,"Post Office Name : ",row[0])
        print(Fore.LIGHTBLUE_EX ,"Pin code : ",row[1])
        print(Fore.LIGHTCYAN_EX ,"Taluk : ",row[4])
        print(Fore.CYAN ,"City : ",row[7])
        print(Fore.LIGHTGREEN_EX ,"District : ",row[8])
        print(Fore.LIGHTYELLOW_EX ,"State : ",row[9])
        print(Fore.LIGHTWHITE_EX,"______________________________________________")
    elif match2 and matchcode:
        j=j+1
        print("----------------------------------------------------")
        print(Fore.BLUE ,"Post Office Name : ",row[0])
        print(Fore.LIGHTBLUE_EX ,"Pin code : ",row[1])
        print(Fore.LIGHTCYAN_EX ,"Taluk : ",row[4])
        print(Fore.CYAN ,"City : ",row[7])
        print(Fore.LIGHTGREEN_EX ,"District : ",row[8])
        print(Fore.LIGHTYELLOW_EX ,"State : ",row[9])
        print(Fore.LIGHTWHITE_EX,"______________________________________________")
    else:
        if (len(data)-1)==rc:
            print(Fore.RED ,"Try with another key word")
        else:
            rc=rc+1       
print(j," Results Found For",code)                    
#print(len(data),rc)

   