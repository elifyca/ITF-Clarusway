age = "yes"
chronic = "yes"
immune = "yes"
print("Give your answer yes or no")
age = input ("Are you a cigarette addcit older than 75 years old?")
chronic = input ("Do you have a severe chronic disease")
immune = input ("Is your immune system too weak?")
if age == True and chronic == True and immune == True:
     print("You are in risky group")
else:
     print("You are not in risky group")