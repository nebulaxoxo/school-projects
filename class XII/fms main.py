import os
import platform
import mysql.connector
import pandas as pd
import datetime

mydb = mysql.connector.connect(user='root', password='nebula_3F0', host='localhost', database='airindigo')
mycursor = mydb.cursor()

def registercust():
    L = []
    name = input("Enter name: ")
    L.append(name)
    addr = input("Enter address: ")
    L.append(addr)
    jr_date = input("Enter date of journey: ")
    L.append(jr_date)
    source = input("Enter source: ")
    L.append(source)
    destination = input("Enter destination: ")
    L.append(destination)
    cust = tuple(L)
    sql = "insert into pdata(custname, addr, jrdate, source, destination) values(%s, %s, %s, %s, %s)"
    mycursor.execute(sql, cust)
    mydb.commit()

def classtypeview():
    print("Do you want to see class type available : Enter 1 for yes :")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        sql = "select * from classtype"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        global x
        for x in rows:
            print(x)

def ticketprice():
    classtypeview()
    x=int(input("Enter Your Choice Please->"))
    n = int(input("No of passenger: "))
    if x == 1:
        print("you have opted First class")
        s = 6000 * n
    elif x == 2:
        print("you have opted Business class")
        s = 4000 * n
    elif x == 3:
        print("you have opted Economy class")
        s = 2000 * n
    else:
        print("please choose a class type")
    print("your bill is = ", s, "\n")

def menuview():
    print("Do you want to see menu available : Enter 1 for yes :")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        sql = "select * from food"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)

def orderitem():
    global s
    print("Do you want to see menu available : Enter 1 for yes :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from food"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)

        d = int(input("Enter your choice:"))
        if d == 1:
            print("You have ordered tea")
            a = int(input("Enter quantity: "))
            s = 10 * a
            print("Your amount for tea is :", s, "\n")
        elif d == 2:
            print("You have ordered coffee")
            a = int(input("Enter quantity: "))
            s = 10 * a
            print("Your amount for coffee is :", s, "\n")
        elif d == 3:
            print("You have ordered coldrink")
            a = int(input("Enter quantity: "))
            s = 20 * a
            print("Your amount for coldrink is :", s, "\n")
        elif d == 4:
            print("You have ordered samosa")
            a = int(input("Enter quantity: "))
            s = 10 * a
            print("Your amount for samosa is :", s, "\n")
        elif d == 5:
            print("You have ordered sandwich")
            a = int(input("Enter quantity: "))
            s = 50 * a
            print("Your amount for sandwich is :", s, "\n")
        elif d == 6:
            print("You have ordered dhokla")
            a = int(input("Enter quantity: "))
            s = 30 * a
            print("Your amount for dhokla is :", s, "\n")
        elif d == 7:
            print("You have ordered kachori")
            a = int(input("Enter quantity: "))
            s = 10 * a
            print("Your amount for kachori is :", s, "\n")
        elif d == 8:
            print("You have ordered milk")
            a = int(input("Enter quantity: "))
            s = 20 * a
            print("Your amount for kachori is :", s, "\n")
        elif d == 9:
            print("You have ordered noodles")
            a = int(input("Enter quantity: "))
            s = 50 * a
            print("Your amount for noodles is :", s, "\n")
        elif d == 10:
            print("You have ordered pasta")
            a = int(input("Enter quantity: "))
            s = 50 * a
            print("Your amount for pasta is :", s, "\n")
        else:
            print("Please enter your choice from the menu")

def lugagebill():
    global z
    print("Do yoy want to see rate for lugage  : Enter 1 for yes :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from luggage"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)
        y = int(input("Enter your weight of extra lugage->"))
        z = y * 1000
        print("Your luggage bill:", z, "\n")
    return z

def lb():
    print(z)

def res():
    print(s)

def ticketamount():
    a = input("enter customer name:")
    print("customer name :", a, "\n")
    print("lugage bill:")
    lb()
    print("food bill:")
    print(s)
    print("total amount")

def Menuset():
    print("AIR TICKET RESERVATION")
    print("enter 1: To enter customer data")
    print("enter 2: To view class")
    print("enter 3: For  Ticket amount")
    print("enter 4: For viewing food menu")
    print("enter 5: For food bill")
    print("enter 6: For lugage bill")
    print("enter 7: For complete amount")
    print("enter 8: For exit")
    userinput = int(input("Enter your choice: "))
    if userinput == 1:
        registercust()
    elif userinput == 2:
        classtypeview()
    elif userinput == 3:
        ticketprice()
    elif userinput == 4:
        menuview()
    elif userinput == 5:
        orderitem()
    elif userinput == 6:
        lugagebill()
    elif userinput == 7:
        ticketamount()
    elif userinput == 8:
        quit()
    else:
        print("Enter correct choice")

Menuset()

def runagain():
    runagn = input("\n Want to run again y/n? ")
    while runagn.lower() == 'y':
        if platform.system() == "windows":
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menuset()
        runagn = input("\n Want to run again y/n? ")

runagain()
