import re

g = input("Do you agree : \n") 


if re.search("^y(es)?$", g,re.IGNORECASE):
    print("Agreed")
elif re.search("n(o)?", g.lower()):
    print("Not Agreed")


 
