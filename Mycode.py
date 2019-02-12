print("***********************WELCOME TO ONLINE ELECTRICITY BILLING***********************")
from PIL import Image
myImage=Image.open("main.jpg")                                                                                           #opens/pops-up main.jpg (image)
myImage.show()
print("Paying electricity bills online usually requires you to physically go to an outlet and stand in long queues!!!!")
print("to clear the payment.Well not anymore! Here is our project, ")
print("that even provides you with exclusive offers that will save your time and money")
print(" while providing you an easier way for online bill payments")
print("click 1 to register")
print("click 2 to login")
n=int(input())
if n==1:
 from register import *                                                                                                  #imports the functions defined in register module
else:
 print("invalid choice")
 quit()
print("**Type pay to pay**")
ch=raw_input()
if ch=='pay':
 from time import sleep
 print("proceeding to pay>>........")
 sleep(2)
 from pay import *                                                                                                       #imports the contents of the module pay

print("click 3 to exit")
o=int(input())
if n==3:
  print("logging out>>>>...........")
  sleep(3)
print("THANK YOU FOR USING ONLINE ELECTRICITY BILLING")
print("               All Rights Reserved            ")
print("                     2019                     ")





