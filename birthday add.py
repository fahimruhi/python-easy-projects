f= open("birthday.txt","w+")
dict = { }
while True:
    
    print("1. show")
    print("2. add")
    print("3. exit")
    choice= int(input("enter your choice: ") )
    if (choice == 3):
        break
    if (choice==2):
        name= input("name: " )
        date= input("date: ")
        dict[name]= date
        print("added")
        f.write(str(dict))
        f.close()
    if(choice==1):
        r=open("birthday.txt","r+")
        if len(r.keys())==0:
            print("nothing to show")
        else:
            name= input("enter the name: ")
            birthday= dict.get(birthday.txt(name),"no match")
            print(birthday)
    
