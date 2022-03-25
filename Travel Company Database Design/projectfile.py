#!/usr/bin/env python
# coding: utf-8

# In[3]:


import mysql.connector as mysql
from tabulate import tabulate


# In[4]:


db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Pass@1234",
    database = "sql_project"
)
cursor=db.cursor()


# In[ ]:


print("welcome to our database")
while True:
    show = int(input("If You want to see list of tables in our database enter 1 \nIf you want to see list of stored procedures enter 2\nIf you want to see list of triggers enter 3 \nIf you want to see list of views enter 4 \nIf you want to quit enter 0:"))

    if show == 1:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print(tabulate(tables))
    
    elif show == 2:
        cursor.execute("SHOW PROCEDURE STATUS where Db = 'sql_project'")
        stored_procedures = cursor.fetchall()
        print(tabulate(stored_procedures,tablefmt = 'fancy_grid'))
        
        while True:
            print("this procedure will show u the outpuct for airlines departure schedule in selected city")
            args=(input("enter name of city:\n"))
            cursor.callproc('cityschedule',(args,))
            for i in cursor.stored_results():
                a=i.fetchall()
                print(tabulate(a,tablefmt = 'fancy_grid'))
                print("thats your output for",args)
            select=int(input("select 1 to continue n 2 to exit: \n"))
            if select==2:
                break
            elif select==1:
                continue
            else :
                print("Galat input mat dalo")    
                
        while True:
            print("This procedure will show u fare prices for selected faretype")
            args1=(input("Enter fare type you want to see:\n"))
            cursor.callproc('airfare_selection',(args1,))
            for i in cursor.stored_results():
                a1=i.fetchall()
                print(tabulate(a1,tablefmt = 'fancy_grid'))
            select=int(input("select 1 to continue n 2 to exit: \n"))
            if select==2:
                break
            elif select==1:
                continue
            else :
                print("kya kar raha hai bhai Galat input mat dal")    
                 
        while (True):
            print("This procedure will show u repeated booking")
                
            args=int(input("enter number of u want to see for repeated booking:\n"))
            cursor.callproc('repeated_user',[args,])
            for result in cursor.stored_results():
                a=result.fetchall()
                print(tabulate(a,tablefmt = 'fancy_grid'))
                print("done")
            select=int(input("select 1 to continue n 2 to exit: \n"))
            if select==2:
                break
            elif select==1:
                continue
            else :
                print("kya kar raha hai bhai Galat input mat dalo")    
                  
    elif show == 3:
        cursor.execute("SHOW TRIGGERS")
        triggers = cursor.fetchall()
        print(tabulate(triggers,tablefmt = 'fancy_grid'))
        triggers=int(input("If you want to see details of triggers please type 5:\n and to stop viewing triggers enter stop"))
        if triggers==5:
            while True:
                print("this is an after insert trigger that will delete the entered user_id input and will show the deleted users table")
                userid = input("enter user_id: \n")
                query="delete from users where user_id ={}".format(userid)
                cursor.execute(query)
                db.commit()
                if cursor.rowcount>0:
                    print("user deleted successfully")
                    query1 = "select * from deleted_users"
                    cursor.execute(query1)
                    booking = cursor.fetchall()
                    print(tabulate(booking,tablefmt='fancy_grid'))
                else:
                    print("wrong input")
                select=int(input("select 1 to continue n 2 to exit: \n"))
                if select==2:
                    break
                elif select==1:
                    continue
                else :
                    print("kya kar raha hai bhai Galat input mat dal")    
                

            while True:
                print("this trigger will not let u enter the wrong input for email and after entering correct inputs it will take current time in booking date")
                try:
                    user_id = input("Enter user_id:\n")
                    first_name = input("Enter first_name:\n")
                    email = input("Enter email:\n")
                    query="INSERT INTO `sql_project`.`users` (`User_id`, `FirstName`, `Email_Id`) VALUES (%s, %s, %s)"
                    record = (user_id,first_name,email)
                    cursor.execute(query,record)
                    test_triggers = cursor.fetchall()
                    print(test_triggers)
                    query1 = "select * from users"
                    cursor.execute(query1)
                    booking = cursor.fetchall()
                    db.commit()
                    print(cursor.rowcount)
                    if cursor.rowcount >0: 
                        query1 = "select * from users"
                        cursor.execute(query1)
                        booking = cursor.fetchall()
                        print(tabulate(booking,tablefmt='fancy_grid'))
                        

                except Exception as e:
                    print(e)
                select=int(input("select 1 to continue n 2 to exit: \n"))
                if select==2:
                    break
                elif select==1:
                    continue
                else :
                        print("kya kar raha hai bhai Galat input mat dal")
            while True:
                print(" this trigger allows frequent user get discount on the nth booking")
                cursor.execute("select * from offer_table")
                a=cursor.fetchall()
                b=cursor.rowcount
                print(b)
                booking_id = input("Enter booking_id:\n")
                user_id = input("Enter user_id:\n")
                service_id = input("Enter service_id:\n")
                query="INSERT INTO `sql_project`.`booking_table` (`booking_id`, `user_id`, `service_id`) VALUES (%s, %s, %s)"
                record = (booking_id,user_id,service_id)
                cursor.execute(query,record)
                test_triggers = cursor.fetchall()
                db.commit()
                cursor.execute("select * from offer_table")
                d = cursor.fetchall()
                f = cursor.rowcount
                if f>b:
                    print(tabulate(d))
                else:
                    print("booking succesfull but offer not applied")
                select=int(input("select 1 to continue n 2 to exit: \n"))
                if select==2:
                    break
                elif select==1:
                    continue
                else :
                    print("kya kar raha hai bhai Galat input mat dal")

    elif show == 4:
        cursor.execute("SHOW FULL TABLES IN sql_project WHERE TABLE_TYPE LIKE 'VIEW';")
        triggers = cursor.fetchall()
        print(tabulate(triggers,tablefmt = 'fancy_grid'))
        try:
            while (True):
                z=int(input("Press 1 to see airlines_revenue_analysis view or 2 to see service_analysis_over_booking or 3 to break :\n"))
                if z==1:
                      cursor.execute("select * from airlinesrevenue_analysis_over_booking")
                      data=cursor.fetchall()
                      print(tabulate(data))

                elif z==2:
                    cursor.execute("select * from service_analysis_over_booking")
                    data=cursor.fetchall()
                    print(tabulate(data))
                elif z==3:
                    break
                else :
                    print("Galat input mat dalo")    

        except Exception as Error:
            print(Error)
    if show == 0:
        print("Thanks for watching")
        print ("submitted by:\n 1)Lakshita sahdev \n 2)siddhesh Kumamekar \n 3)dikshant Sakharkar \n 4)dipak charpe")
        break


# In[ ]:





# In[ ]:




