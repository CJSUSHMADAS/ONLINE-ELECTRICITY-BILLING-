print("*****************PAYMENT DONE HERE*****************")
accno1='1SBI9876123'                                                                                                     # global variables
accno2='1CNR6512340'
accno3='1AXS1209457'
accno4='1ICI2398645'
accno5='1VJY2309556'
ch1='STATE BANK OF INDIA'
ch2='CANARA BANK'
ch3='AXIS BANK'
ch4='ICICI BANK'
ch5='VIJAYA BANK'

print('amount:1500')
print("SELECT YOUR CARD")
print('1.STATE BANK OF INDIA')
print('2.CANARA BANK')
print('3.AXIS BANK')
print('4.ICICI BANK')
print('5.VIJAYA BANK')
n=int(input())
if n==1:
    print('STATE BANK OF INDIA')
    print('our SBI account number is:1SBI7654325')
    print('enter your account number')
    accno=raw_input()
    if accno==accno1:
     print(accno,ch1)
     print('thank you for using',ch1)
    else:
     print("invalid account number")
     quit()
elif n==2:
    print('CANARA BANK')
    print('our CANARA account number is:1CNR7698323')
    print('enter your account number')
    accno = raw_input()
    if accno == accno2:
     print(accno,ch2)
     print('thank you for using',ch2)
    else:
     print("invalid account number")
     quit()
elif n==3:
    print('AXIS BANK')
    print('our AXIS account number is:1AXS7654990')
    print('enter your account number')
    accno = raw_input()
    if accno == accno3:
     print(accno,ch3)
     print('thank you for using',ch3)
     quit()
    else:
     print("invalid account number")
elif n==4:
    print('ICICI BANK')
    print('our ICICI account number is:1ICI3764439')
    print('enter your account number')
    accno = raw_input()
    if accno == accno4:
     print(accno,ch4)
    else:
     print("invalid account number")
     print('thank you for using',ch4)
     quit()
elif n==5:
    print('VIJAYA BANK')
    print('our VIJAYA account number is:1VJY7884412')
    print('enter your account number')
    accno = raw_input()
    if accno == accno5:
     print(accno,ch5)
     print('thank you for using',ch5)
    else:
     print("invalid account number")
     quit()
else:
    print("invalid input")
    quit()
from  time import sleep
print("processing......................")
sleep(2)
print("payment successfull!!!!")
print('customer id:1KEB018254')
print('payment status:clear(no Due)')
print("************THANK YOU*************")
print("ou will receive a system generated mail")
print("Or message to the registered mobile number")


