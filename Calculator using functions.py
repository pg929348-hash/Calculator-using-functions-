      
def calculator(a,b,c):
                    if a=="+":
                        return b+c
                    elif a=="-":
                        return b-c
                    elif a=="*":
                        return b*c
                    elif a=="/":
                        if c!=0:
                            return b/c
                        else:
                            return  "its not divided by 0"
history=[]
attempt=0
while attempt<10:
               print()   
               a=input("enter operator +,-,*,/,quit:-")
               if a=="quit":
                   print("thankyou")
                   break
               try:
                    b=int(input("enter first no.:-"))
                    c=int(input("enter second no.:-"))
                    result=calculator(a,b,c)
                    print("Answer:-",result)
                    history.append(f"{b}{a}{c}={result}")
                    attempt+=1
               except:
                    print("enter only numbers")
                    
print("##history##")     
for i in history:
         print(i)     
         
         
