email=input("enter email to validate:")
k=0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4]=="." ) ^ (email[-3]=="."):
                for i in email:
                    if (i== i.isspace()):
                        k=1
                    elif i.isalpha():
                        if (i==i.isupper()):
                            k=1
                    elif i.isdigit():
                        continue
                    elif (i=="_") or (i==".") or (i=="@"):
                        continue
                    else:
                        k=1
                if (k==1):
                    print("you cannot use uppercase, special charactos excluding _ . @ and blank spaces in your email")
                else:
                    print("your email is correct")
            else:
                print ("you can only input emails of .com, .in, .org")
        else:
            print("you have to strictly use @ only once")
    else:
        print("email first object must be a charactor")
else:
    print("wrong email you have missd something in your email")
