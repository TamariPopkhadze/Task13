n = (input("camelCase:"))
capital_letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for x in n:
    if(x in capital_letters):
        index = n.find(x)
        n=n[:index] + "_" + x.lower() + n[index+1:]
        
print("snake_case:" +  n)        
           
       

