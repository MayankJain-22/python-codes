import  mysql.connector as sql
conn = sql.connect(host="localhost",user="root",passwd="123456",charset="utf8",database="csp")
cur = conn.cursor()
usersname = ""
billlist = []
zeroth=0
first = 0
second = 0
third = 0
fourth = 0
fifth = 0
six = 0
while zeroth ==0:
    # cur.execute('create table usertable(username varchar(25) primary key,passwrd varchar(25) not null,address varchar(200),phonenumber varchar(20),emailid varchar(100) )')
    print('=========================WELCOME TO food ordering page============================================================')
    print('1.REGISTER')
    print()
    print('2.LOGIN')
    print()
    print("3.EXIT")
    print()

    no=(input('enter your choice='))
    print()

    if no== "1":
        name=input('Enter a Username=')
        print()
        passwd=int(input('Enter a 4 DIGIT Password='))
        print()
        adres = str(input("Enter your address="))
        print()
        phno = int(input("enter phone number="))
        print()
        email = str(input("enter your email id="))
        print()                                                #(passwd,'name,')
        V_SQLInsert="INSERT INTO usertable (passwrd,username,address,phonenumber,emailid) values ("+str(passwd)+",'"+name+"','"+str(adres)+"','"+str(phno)+"','"+str(email)+"')"
        cur.execute(V_SQLInsert)
        conn.commit()
        print()
        print('USER created succesfully')
        continue
        

    elif  no=="2" :
            name=input('Enter your Username=')
            usersname = name
            print()
            passwd=int(input('Enter your 4 DIGIT Password='))
            V_Sql_Sel="select * from usertable where passwrd='"+str (passwd)+"' and username='"+name+"'"
            
            cur.execute(V_Sql_Sel)
            if cur.fetchone() is  None:
                print()
                print('Invalid username or password')
                continue
            else:
                print("logged in succesfully")
                while first ==0:
                    print("1)Order Food")
                    print("2)Menu")
                    print("3)Payment")
                    print("4)Change Current Account Details")
                    print("5)Delete Current Account")
                    print("6)About app")
                    print("7)Back")
                    n=(input("enter your choice= "))
                    if n=="1":
                        while second == 0:
                            fdtype = int(input("select the category of food\n1)Starters\n2)Seafood\n3)Tandoori Specials\n4)Vegetable Dishes\n5)Side Orders\n6)Desserts\n7)Go back to main menu\n"))
                            if fdtype == 7:
                                break
                            list1 =["Starters","Seafood","Tandoori Specials","Vegetable Dishes","Side Orders","Dessert"]
                            query1 = "select itemno,foodname,price,type from menu where category='"+list1[fdtype-1]+"'"
                            # quer = "select foodname,price,type from menu where category='Starters'"
                            cur.execute(query1)
                            content =cur.fetchall()
                            # sno = 1
                            print("itemno","|","type","|","price","|","foodname",sep="\t")
                            print("----------------------------------------------------------")
                            for itemno,foodname,price,type in content:
                                # print(foodname,"\t",price,"\t",type)
                                
                                print(itemno,"|",type,"|",price,"|",foodname,sep="\t")
                            kya = int(input("\n1)order item\n2)go back to select category\n3)go back to main menu\n"))
                            if kya ==1:
                                billitemno=int(input("\nenter the item no. of the food you want to add to cart = "))
                                query2 = "select foodname,price from menu where itemno="+str(billitemno)
                                cur.execute(query2)
                                content2 = cur.fetchone()
                                print (content2)
                                noofitem = int(input("enter no of item to be added ="))

                                while third ==0:
                                    print("do you want to add",noofitem,content2[0],"of rupees",noofitem*content2[1],"in your cart")
                                    yesno= input("enter yes or no = ")
                                
                                    if yesno == "yes":
                                        query3 = "insert into bill values('"+str(content2[0])+"',"+str(content2[1])+","+str(noofitem)+")"
                                        cur.execute(query3)
                                        print("item added successfully")
                                        conn.commit()
                                        break
                                    elif yesno == "no":
                                        print("item not added")
                                        break
                                    else:
                                        print("wrong input entered")
                                        continue
                            elif kya == 2:
                                continue
                            elif kya == 3:
                                break

                    
                    elif n =="2":
                        while fourth == 0:
                            fdtype = int(input("select the category of food\n1)Starters\n2)Seafood\n3)Tandoori Specials\n4)Vegetable Dishes\n5)Side Orders\n6)Desserts\n7)Go back to main menu\n"))
                            if fdtype == 7:
                                break
                            list1 =["Starters","Seafood","Tandoori Specials","Vegetable Dishes","Side Orders","Dessert"]
                            query1 = "select itemno,foodname,price,type from menu where category='"+list1[fdtype-1]+"'"
                            # quer = "select foodname,price,type from menu where category='Starters'"
                            cur.execute(query1)
                            content =cur.fetchall()
                            # sno = 1
                            print("itemno","|","type","|","price","|","foodname",sep="\t")
                            print("----------------------------------------------------------")
                            for itemno,foodname,price,type in content:
                                # print(foodname,"\t",price,"\t",type)
                                
                                print(itemno,"|",type,"|",price,"|",foodname,sep="\t")
                            while 1:
                                kya = int(input("1) Go Back to food category\n"))
                                if kya == 1:
                                    break
                                else:
                                    print("wrong input entered")
                                    continue
                            
                    elif n=="3":
                        query4 = "select foodname,price as Mrp,quantity ,price*quantity as totalprice from bill"
                        cur.execute(query4)
                        content3 = cur.fetchall()
                        print(content3)
                        if content3 == []:
                            print("There is nothing your the cart")
                            continue
                        print("-"*60)
                        print("Mrp\t| Quantity\t| price\t| Food name")
                        print("-"*60)
                        finalamount = 0
                        for i in range(len(content3)):
                            print(content3[i][1],"\t|",content3[i][2],"\t\t|",content3[i][3],"\t|",content3[i][0])
                            finalamount = finalamount + content3[i][3]
                        print("-"*60)
                        print("TOTAL PRICE TO BE PAID IS = ",finalamount)
                        print("-"*60)
                        while True :
                            var = int(input("do you want to pay now or add other items?\n1)Pay Now\n2)Add ither items\n"))
                            if var == 1:
                                print("payment made successfully")
                                query5 = "delete from bill"
                                cur.execute(query5)
                                conn.commit()
                                break
                            elif var == 2:
                                break
                            else:
                                print("wrong input entered")
                                continue

                    elif n == "4":
                        while six==0:
                            print("Current User information is")
                            query7="select * from usertable where username ='"+usersname+"'"
                            cur.execute(query7)
                            content4 = cur.fetchall()
                            print(content4)
                            for nameuser,passs,addr,phnum,emal in content4:
                                print("Username = ",nameuser)
                                print("Password = ",passs)
                                print("Address = ",addr)
                                print("Phone number = ",phnum)
                                print("Email Id = ",emal)
                                inp = int(input("what do you want to update\n1)Username\n2)Password\n3)Address\n4)Phone number\n5)Email Id\n6)Go Back\n"))
                                if inp == 6:
                                    six=1
                                    break
                                list2 = ["username","passwrd","address","phonenumber","emailid"]
                                entry = input("Change it into = ")
                                query8 = "update usertable set "+list2[inp-1]+"='"+entry+"' where username ='"+usersname+"'"
                                cur.execute(query8)
                                conn.commit()
                                print("detail updated succesfully")
                                if list2[inp-1] =="username":
                                    usersname = entry
                                num = input("do you want to update anything else? enter yes or no\n")
                                if num == "yes":
                                    continue
                                if num =="no":
                                    six = 1
                                    break
                        six = 0    

                    elif n== "5":
                        query6="delete from usertable where username = '"+usersname+"'"
                        cur.execute(query6)
                        conn.commit()
                        print("User Deleted Successfully!!!")
                        break

                            
                    elif n=="7":
                        break
                    else:
                        print("wrong input enterred")
                        continue            

    elif no=="3":
        print("thankyou! please visit again")
        break

    else:
        print("Wrong input entered TRY AGAIN!!")
        continue



        
        