#program 5
'''f=open("Be rough.txt",'r')
try:
    while True:
        fi = f.readline()
        a = fi.split()
        for j in a:
            j = j+"#"
            print(j,end="")
except:
    f.close()'''

#program 6
'''f=open("Be rough.txt",'r')
fi=f.read()
vo,c,l,u=0,0,0,0
v=["A",'a','E','e','I','i','O','o','U','u']
for i in fi:
    if i.isalpha():
        if i in v:
            vo=vo+1
        else:
            c=c+1
        if i.islower():
            l=l+1
        else:
            u=u+1
print("number of vowels=",vo)
print("number of consonants=",c)
print("number of lower case=",l)
print("number of uppercase=",u)
f.close()'''

#program 7
'''f=open("Be rough.txt",'r')
fi=f.read()
word = fi.split()
for i in word:
    if len(i)==4:
        print(i)
f.close()'''

#program 8
'''import os
f=open("Be rough.txt",'r')
fa=open("emp.txt",'w')
fwa = open("vowel.txt",'w')
l=f.readlines()
for line in l:
    if "a" in line:
        fa.write(line)
    else:
        fwa.write(line)
fa.close()
fwa.close()
f.close()
os.remove('Be rough.txt')
os.rename('vowel.txt','Be rough.txt')'''

#program 9
'''def write_fun():
    f=open('Be rough.txt ','w')
    l=[]
    while True:
        s = input("enter line to be enter")
        l.append(s)
        if input("enter E if to exit")=="E":
            break
    print("list",l)
    f.writelines(l)
    f.close()
write_fun()'''

#program 10
'''import pickle
f=open('bina.dat','ab')
while True:
    Tno=int(input("enter Train number"))
    From = input("enter starting point")
    To = input("enter destination")
    l = [Tno, From,To]
    pickle.dump(l,f)
    if input("Enter E for exit")=="E":
        break
f.close()'''

#program 11

'''import pickle
f=open("bina.dat",'rb')
try:
    while True:
        x=pickle.load(f)
        if x[1].lower()=="delhi" and x[2].lower()=="kolkata":
            print(x)
except:
    print("completed")
    f.close()'''

#program 12
'''import os
import pickle
f=open("bina.dat",'rb')
f1=open('bina2.dat','wb')
Tno=int(input("entre train numberto be updated:"))
From=input("Enter starting point")
To=input("enter new destination:")
c=0
try:
    while True:
        x=pickle.load(f)
        if x[0]==Tno:
            x[1]=f
            x[2]=To
        pickle.dump(x,f1)
except:
    f.close()
    f1.close()
os.remove("bina.dat")
os.rename('bina2.dat',"bina.dat")'''

#program13
'''import csv
f=open("data1.csv",'w')
wrt=csv.writer(f)
while True:
    name = input("enter your name")
    age=int(input("enter your age"))
    class_sec=input("enter your class")
    wrt.writerow([name,age,class_sec])
    if input("enter E for exit")=="E":
        break
f.close()'''

#program 14
'''import csv
f=open('data1.csv','r')
f_reader=csv.reader(f)
for row in f_reader:
    if int (row[1])>=0 and int (row[1])<=17:
        print(row)
f.close()'''

#program 15
'''import random
question = input('would you like to roll the dice[y/n]?\n')
while question!='n':
    if question =="y":
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(die1,die2)
        question=input("would you like to roll the dice [y/n]?\n")

    else:
        print('invalid respose. please type "y"or "n".')
        question = input("would you like to roll the dice [y/n]?\n")
print('Good-bye!') '''

#program 19
'''import mysql.connector as con
mycon = con.connect(host="localhost",user="root",passwd="123456789")
if mycon.is_connected():
    print("successful")

c1=mycon.cursor();
c1.execute("create database zoo1")
c1.execute("use zoo1")
c1.execute('create table animal (id int (2) primary key, name varchar(20),age int)')
while (True):
    id1= int(input("enter animal id number"))
    name = input("enter the name")
    age=int(input("enter age"))
    c1.execute("insert into animal values(%s,%s,%s)",(id1,name,age))
    if input("want more:")=='n':
        break
mycon.commit()
mycon.close()'''

#program 20
'''import mysql.connector as con
mycon=con.connect(host="localhost",user="root",passwd="123456789",database="KV")
if mycon.is_connected():
    print("successfull")
c1=mycon.cursor();
f1=int(input("enter fee for science stream"))
f2=int(input("enter fee for science stream"))
c1.execute("update student set fee=%s where stream=%s",(f2,"science"))
c1.execute("update student set fee =%s where stream=%s",(f2,"art"))
mycon.commit()
print("successfully updated")
mycon.close()'''

#program 21
'''import mysql.connector as con
mycon=con.connect(host="localhost",user="root",passwd="123456789",database="KV")
if mycon.is_connected():
    print("successfull")
c1=mycon.cursor();
ename=input("enter name")
c1.execute("select * from student where sname = %s", (ename,))
d=c1.fetchall()
for i in d:
    print(i)
mycon.close()'''
