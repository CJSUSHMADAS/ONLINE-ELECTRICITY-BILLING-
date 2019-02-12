print("********************YOU ARE AT THE REGISTER PAGE********************")

def register(name,state,address,city,pincode,pno,usrid,pswd,cpswd):                                                      #defined own function register()
    name=raw_input("enter your name")
    state=raw_input("enter your state")
    address=raw_input("enter your street number")
    city=raw_input("enter your city")
    pincode=raw_input("enter your pincode")
    pno=int(input("enter your phone number "))
    usrid=raw_input("enter user id(****remember****)")
    if usrid==" ":
        print("it cannot be empty")
        quit()
    pswd=raw_input("enter your password(***remember your password***)")
    cpswd=raw_input("enter your password again(***confirm your password***)")
    if pswd==cpswd:
        print("password matched!!!!!!")
        from time import sleep
        sleep(1)
        print("processing......"+".........")
        sleep(2)
        print(name)
        print(address  +" "+ city+" " + state+" "  + pincode)
        print(pno)
        sleep(1)
        print("YOU ELECTRICITY BOARD IS KEB")
        print("your customer id is give below please use it for your further transaction!!!")
        print("1KEB018254")
        from time import sleep                                                                                           # provides delay
        sleep(2)
        print("REGISTRATION SUCCESSFULL!!!")

        print("click 2 to login")
        m = int(input())
        if m == 2:
         print("************************YOU ARE AT THE LOGIN PAGE************************")
         uid = raw_input("enter userid")
         passwd = raw_input("enter your password")

         if uid == usrid and passwd == pswd:
            print("SUCCESS")
            print(name)
            print(address + " " + city + " " + state + " " + pincode)
            print(pno)
            print("1KEB018254")
            print('payment staus:pending')
            print('Amount:1500rs')
         else:
            print("invalid username or password")
            quit()
        else:
            print("invalid input")
            quit()
    else:
        print("password mismatch!!!!!!!!!")
        quit()






r=register('s','karnataka','h','bangalore','560091',23,'sdf234','123*df','123*df')