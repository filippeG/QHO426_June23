h = input("Are you happy ?")
k = input("Do you know it?")

if h.lower() =="yes" and k.lower() == "yes":
    print("Clap your hands")
elif h.lower() == "yes" and k.lower() == "no":
    print("Appreciete what you have, you ungreatful ...")
elif h.lower() == "no" and k.lower() == "yes":
    print("It will get better!")
else:
    print("Seek help - let's talk")
print("Glad you are here")
