from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
import sys
import msvcrt
client = MongoClient("mongodb://127.0.0.1:27017")
db=client.emp
ename=""
eid=1
edes=""
epay=1

edoj=datetime.now()
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)

       
def insert():
    print("____________________________\n INSERT\n____________________________\n")
    eid=int(input("Employee ID : "))
    ename=input("\nEmployee Name : ")
    edes=input("\nDesignation : ")
    epay=int(input("\nSalary : "))
    empdetails={
        'ID':eid,
        'NAME':ename,
        'DESIGNATION':edes,
        'DOJ':str(edoj.strftime('%Y-%m-%d')),
        'SALARY':epay
    }
    result=db.employee.insert_one(empdetails)
    print('\n\nInserted with ID {0}'.format(result.inserted_id))
    selectedView(eid)
    sys.exit()

def eupdate():
    print("____________________________\nUPDATE\n____________________________\n")
    empid=int(input("Enter Employee Id to Update : "))
    res=db.employee.find_one({'ID':empid})
    if res==None:
        print("ID {} Not Found".format(empid))
        sys.exit()
    uname=res['NAME']
    udes=res['DESIGNATION']
    usalary=res['SALARY']
    updlist=[uname,udes,usalary]
    nlist=['NAME','DESIGNATION','SALARY']
    i=0
    status="Unknown Error"
    reslist=[]
    print("Press [ESC] to skip updating value")
    print("SALARY")   
    while True:
        if msvcrt.kbhit():
            
            key = msvcrt.getch()
            
                    
            if "b\'\\x1b'"==str(key) and i!=3:
                
                updlist[i-1]=res[nlist[i-1]]
                print(nlist[i-1]," : ",updlist[i-1])
                if i!=2:
                    print(nlist[i])
                
                i=i+1
                continue
            elif "b\'\\r'"==str(key) and i!=3:
                #i=i+1
                updlist[i-1]=input("{} : ".format(nlist[i-1]))
                reslist.append(i) 
                while updlist[i-1]=="":
                    updlist[i-1]=input("{} : ".format(nlist[i-1]))
                print("Updated {}:".format(nlist[i-1]),updlist[i-1])
                if i!=2:
                    print(nlist[i])
                
            else:
                print("You are about to update\n")
                #print(updlist)
                for item in reslist:
                    print(nlist[item-1]," : ",updlist[item-1])
                sel=input("Update (Y/N) : ")
                if sel=='Y' or sel=='y':
                    try:
                        db.employee.update_one({'ID':res['ID']},{"$set": {
                        "NAME":updlist[0],
                        "DESIGNATION":updlist[1],
                        "SALARY":updlist[2]
                        }
                        } )
                        status="Successfully Updated"
                        selectedView(res['ID'])
                    except Exception as e:
                        status=e
                elif sel=='N' or sel=='n':
                    status="Update cancelled by User"
                else:
                    status="invalid Choice"

                break
            
            i=i+1
            if i>3:
                
                sys.exit()
    return status        
def exi():
    sys.exit()
def selectedView(empid):
    disp=db.employee.find_one({'ID':empid})
    if disp==None:
        display()
    else:
        print("____________________________\nEmployee {}\n____________________________\n".format(empid))
        print("EMPLOYEE ID: {}\nNAME: {}\nDESIGNATION: {}\nDOJ: {}\nSALARY: {}".format(disp['ID'],disp['NAME'],disp['DESIGNATION'],disp['DOJ'],disp['SALARY']))

def delete():
    print("____________________________\nDELETE\n____________________________\n")
    empid=int(input("Enter Employee Id to DELETE : "))
    res=db.employee.find_one({'ID':empid})
    if res==None:
        print("Employee ID {} Not Found".format(empid))
    else:
        db.employee.delete_one({'ID':res['ID']})
        print("Deleted ID: {} with Name: {}".format(res['ID'],res['NAME']))
        selectedView(res['ID'])
    sys.exit()
def display():
    print("____________________________\nEmployee Details\n____________________________\n")
    disp=db.employee.find({})
    for item in disp:
        pprint(item)
        
    
    sys.exit()

 
switcher = {
        1: insert,
        2: delete,
        3: eupdate,
        4: display,
        5: exi
    }
 
 
def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument,"")
    # Execute the function
    return func()
#while True:
inp=int(input("Select Your Choice : \n 1.Insert \n 2.Delete \n 3.Update \n 4.Display \n 5.Exit : \n"))
print(numbers_to_strings(inp))