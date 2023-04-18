credentials={"alice":"alice1243","bob":"bobspassword123"}

a=input("Enter username:")

if a in credentials:
    b=input("Enter password:")
    if b== credentials[a]:
        print("Login success.")
    else:
        print("Incorrect Password")
            
else:
    print("User not found")
