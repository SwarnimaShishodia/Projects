#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from autocorrect import spell
print("\t\t\t\t\t Welcome to ELWORDINO\n")
a=input("""Want to read instructions?: 
        Enter yes 
        otherwise enter no : """)
if a.casefold()=="yes":
    print("""1-Each player will enter one alphabet turn by turn.
2-When its your word, your name will be displayed and length of the word will be added to your score.
3-The other player should try to shorten the word to lessen the score.
4-First character will be given by computer.
5-You will be having alternate turns.\n""")
b=int(input("""Enter 1 for level-1.
Level 2 will get unlocked when you score above 15 in Level 1
Level 3 will get unlocked when you score above 15 in level 2\n"""))
p1=0
p2=0
if b==2 or b==3:
    print("The level is locked. You need to unlock it")
    print("YOU CAN ONLY PLAY LEVEL 1 NOW")
    b=1
if b>3:
    print("""Read the instructions carefully
    You have entered a wrong choice""")
    print("YOU CAN ONLY PLAY LEVEL 1 NOW")
    b=1
def deduction(ne,comp,ef,c,d):
    global p1
    global p2
    lne=len(ne)
    lcomp=len(comp)
    if lne>lcomp:
        ldif=lne-lcomp
        for i in range(0,ldif):
            comp=comp+"/"
    if lne<lcomp:
        ldif=lcomp-lne
        for i in range(0,ldif):
            ne=ne+"/"
    a=0 
    for i in comp:
        if i!=ne[a]:
            if e==1 and a%2==0:
                p2=p2-10
                break
            if e==1 and a%2!=0:
                p1=p1-10
                break
            if e==2 and a%2==0:
                p1=p1-10
                break
            if e==2 and a%2!=0:
                p2=p2-10
                break
        a=a+1
    print(c+"current score is:"+str(p1))
    print(d+"current score is:"+str(p2))
def comments():
    if p1==40 or p2==40:
        print("Amazing!!!")
    if p1==80 or p2==80:
        print("Splendid!!!")
    if p1==100 or p2==100:
        print("Outstanding!!! :) ")
if b==1:
    print("\t\t WeLcOmE To LeVeL-1\n")
    c=input("Enter name of player1 --")
    d=input("Enter name of player2 --")
    chance=1
    while chance<=6: 
        if chance%2!=0:
            print(c+"-YOUR TURN")
        if chance%2==0:
            print(d+"-YOUR TURN")
        e=random.randrange(1,2)
        if e==1:
            print(c+" will enter first character\n")
        if e==2:
            print(d+" will enter first character\n")
        print("If you want to terminate a word enter .")
        print("START")    
        g=random.randrange(65,90)
        h=chr(g)
        print(h)
        i=[]
        i.append(h)
        turn=1
        while h!=".":
            if turn==1:
                turn=2
                print(c+" -enter")
            else:
                turn=1
                print(d+" -enter")
            h=input()
            z=len(h)
            if z==1:
                if h!=".":
                    i.append(h)
                    new=""
                    j=len(i)
                    for k in range(0,j):
                        new=new+i[k]
                    print("   "+new)
            else:
                print("""Hahaha you are cheating
                     The characters you have entered will not be considered """)
        score=len(new)
        compare=spell(new)
        if compare==new:
            if chance%2!=0:
                p1=p1+score
                print(c+" current score is:"+str(p1))
            if chance%2==0:
                p2=p2+score
                print(d+" current score is:"+str(p2))
        else:
            deduction(new,compare,e,c,d) 
        if p1>=15:
            print("""Wow You scored 15 first...:)
            BONUS=='10 POINTS' """)
            p1=p1+10
            level=input("""Do you want to play level 2 
            If yes enter 2 : """)
            comments()
            if level=="2":
                bd=2
                break
        if p2>=15:
            print("""Wow You scored 15 first...:)
            BONUS=='10 POINTS' """)
            p2=p2+10
            level=input("""Do you want to play level 2 
            If yes enter 2 : """)
            comments()
            if level=="2":
                bd=2
                break
        if chance==6:
            choice=input("""Do you want to play more?
            Enter yes
            Otherwise enter no""")
            if choice.casefold()=="yes":
                chance=0
            else:
                print("Thankyou for playing :)")
                break       
        chance=chance+1       
        comments()
if bd==2:        
    print("""CONGRATULATIONS!!!
         \t\t\t WELCOME TO LEVEL 2""")
    chance=1
    while chance<=6:
        if chance%2!=0:
            print(c+"-YOUR TURN")
        if chance%2==0:
            print(d+"-YOURTURN")
        e=random.randrange(1,2)
        if e==1:
            print(c+" will enter first character\n")
        if e==2:
            print(d+" will enter first character\n")
        print("if your word gets complete enter .")
        print("START")    
        g=random.randrange(65,90)
        h=chr(g)
        print(h)
        i=[]
        i.append(h)
        turn=1
        while h!=".":
            if turn==1:
                turn=2
                print(c+" -enter")
            else:
                turn=1
                print(d+" -enter")
            h=input()
            z=len(h)
            if z==1:
                if h!=".":
                    i.append(h)
                    new=""
                    j=len(i)
                    for k in range(0,j):
                        new=new+i[k]
                    print("   "+new)
            else:
                print("""Hahaha you are cheating 
                      You have entered two characters
                      They will not be considered""")
        score=len(new)
        compare=spell(new)
        if compare==new:
            print("""READ CAREFULLY
            1-You will be given specific length and the word that you have formed ,
            for each character of that word you have to input a word of given length.
            2-If the words entered are invalid or exceed the length then score will turn 0..BE CAREFUL... """)
            guess=random.randrange(3,6)
            for i in new:
                sw=input("Enter the word of length "+str(guess)+" starting with- "+i+"  ")
                sw=sw.casefold()
                i=i.casefold()
                res=sw.startswith(i)
                if (str(res))=="True":
                    newone=spell(sw)
                    if sw==newone:
                        length=len(sw)
                        if length==guess:
                            if chance%2!=0:
                                p1=p1+length
                            else:
                                p2=p2+length
                        else:
                            if chance%2!=0:
                                p1=0
                            else:
                                p2=0
                if str(res)=="False":
                    print("FIRST CHARACTER IS NOT MATCHING")
        else:
            deduction(new,compare,e,c,d)             
        if chance%2!=0:
            p1=p1+score
            print(c+"current score is:"+str(p1))
        if chance%2==0:
            p2=p2+score
            print(d+"current score is:"+str(p2))
        if p1>=15:
            print("""Wow You scored 15 first...:)
            BONUS=='10 POINTS' """)
            p1=p1+10
            level=input("""Do you want to play level 3
            If yes enter 3 : """)
            comments()
            if level=="3":
                bd=3
                break
        if p2>=15:
            print("""Wow You scored 15 first...:)
            BONUS=='10 POINTS' """)
            p2=p2+10
            level=input("""Do you want to play level 3
            If yes enter 3 : """)
            comments()
            if level=="3":
                bd=3
                break        
        chance=chance+1
        if chance==6:
            choice=input("""DO YOU WANT TO CONTINUE? 
            Enter yes 
            otherwise enter no :""")
            if choice=="yes":
                chance=1
            else:
                print("THANKYOU FOR PLAYING")
                break
        comments() 
if bd==3:
    print("""WOW!!!
    \t\t\t Welcome to level 3.
    You nailed it !!!!
     read instructions  """)
    print("""1-You will be given three characters
        2-Any of the two characters should appear in you word""")
    chance=1
    while chance<=6: 
        if chance%2!=0:
            print(c+"-YOUR TURN")
        if chance%2==0:
            print(d+"-YOUR TURN")
        e=random.randrange(1,2)
        if e==1:
            print(c+" will enter first character\n")
        if e==2:
            print(d+" will enter first character\n")
        print("if your word gets complete enter .")
        alpha=random.randrange(65,90)
        nm=chr(alpha)
        alpha1=random.randrange(65,90)
        mn=chr(alpha1)
        alpha2=random.randrange(65,90)
        mm=chr(alpha2)
        print(" ANY TWO CHARACTERS OUT OF THESE SHOULD APPEAR IN YOUR WORD "+str(nm)+" "+str(mn)+" "+str(mm)+" :" )
        print("START")    
        g=random.randrange(65,90)
        h=chr(g)
        print(h)
        i=[]
        i.append(h)
        turn=1
        while h!=".":
            if turn==1:
                turn=2
                print(c+" -enter")
            else:
                turn=1
                print(d+" -enter")
            h=input()
            z=len(h)
            if z==1:
                if h!=".":
                    i.append(h)
                    new=""
                    j=len(i)
                    for k in range(0,j):
                        new=new+i[k]
                    print("   "+new)
            else:
                print("""Hahaha you are cheating
                      The characters you have entered will not be considered""")
        score=len(new)
        new=new.casefold()
        mn=mn.casefold()
        nm=nm.casefold()
        mm=mm.casefold()
        if ((str(mn) in new and str(nm) in new ) or (str(mn) in new and str(mm) in new) or (str(mm) in new and str(nm) in new)):
            compare=spell(new)
            if new==compare:
                if chance%2!=0:
                    p1=p1+score
                    print(c+"current score is:"+str(p1))
                    comments()
                if chance%2==0:
                    p2=p2+score
                    comments()
                    print(d+"current score is:"+str(p2))
            else:
                deduction(new,compare,e,c,d) 
        else:
            print("Task not completed") 
        if chance==6:
            choice=input("DO YOU WANT TO CONTINUE? Enter yes or no :")
            if choice.casefold()=="yes":
                chance=1
            else:
                print("THANKYOU HOPE YOU LIKED IT")
                break
        chance=chance+1
print(c+" score is "+str(p1)) 
print(d+" score is "+str(p2))
if p1>p2:
    print(c+" WINS :)")
else :
    print(d+" WINS :)")
comm=input("Before you exit ,We would like to know your experience :")
print("Thnankyou :)")            


# In[ ]:




