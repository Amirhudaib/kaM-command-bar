from time import *
from random import *
from turtle import *
print("                                            kaM project by Jcnxz(Amir Hudaib)")
uname = input("ENTER YOUR NAME:")
print("Welcome",uname,"to kaM project!")
print("type /help to show all the commands")


















def calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /):")
    num2 = float(input("Enter the second number: "))
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)
    else:
        print("invalid operator")










uwriting = ""

while True:
    cmbar = input("COMMAND BAR:")
    if cmbar == "/time&date":  
        print(ctime(time()))
    elif cmbar == "/shutdown":
        print("shuting down please wait")
        sleep(1.5)
        print("\nTHE PROJECT HAS SHUTTED DOWN\n")
        break
    elif cmbar == "/writing":
        uwriting = input("write what you want here:\n")
    elif cmbar == "/printwriting":
        if uwriting:
            print(uwriting)
        else:
            print("nothing written yet")
    elif cmbar == "/calculator":
        calculator()
    elif cmbar == "/devsGitHub":
        print("https://github.com/Amirhudaib")
    elif cmbar == "/A1Z26":
        print("A1Z26 is a simple substitution cipher where each letter is replaced by its position in the alphabet")
        print("1=A 2=B 3=C 4=D 5=E 6=F 7=G 8=H 9=I 10=J\n11=K 12=L 13=N 14=M 15=O 16=P 17=Q 18=R 19=X 20=T\n21=U 22=V 23=W 24=S 25=Y 26=Z")
    elif cmbar == "/dice":
        dice = randint(1, 6)
        print(dice)
    elif cmbar == "/joke":
        print("why is the laptop cold??\n'cuz it left windows open")
        sleep(2.5)
        print("not funny?!")
        sleep(1)
        print("im sorry")
        sleep(1)
        print("let's continue")
    elif cmbar == "/kaMslogo":
        pensize(10)
        color("gray")
        left(120)
        fd(150)
        left(220)
        fd(50)
        left(220)
        fd(150)
        exitonclick()
    elif cmbar == "/help":
        print("/help")
        print("/time&date")
        print("/writing")
        print("/printwriting")
        print("/shutdown")
        print("/calculator")
        print("/devsGitHub")
        print("/A1Z26")
        print("/dice")
        print("/joke")
        print("/kaMslogo")
    else:
        print("INVALID COMMAND PLEASE TRY AGAIN")