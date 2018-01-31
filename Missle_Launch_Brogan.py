#Brogan Mutarelli
#11/1/17
#Missle Launch


#TODO timing for 3, 2, 1

print("*" * 80)
print("Fedaral Goverment Missle Launch")
print("*" * 80)

real_name = "brogan"
real_password = "pizza"


name = input("What is your name?")
password = input("What is the password?")

if name == real_name:
    if password == real_password:
        print ("Missle launch in 3, 2, 1")
    else:
        print("Self destruct in 3, 2, 1")
        print("Boom")
        print("Bam")

else:
    print("Self destruct in 3, 2, 1")
    print("Boom")
    print("Bam")
