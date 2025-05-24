while True:  
     n=int(input("Enter the year:"))
     if n%4==0 and n%100!=0:
         print(f"{n} is a leap year")
     else:
         print(f"{n} is not a leap year")
     b=input("Do you want continue say (yes or no): ").lower()
     if b!="yes":
         print("Thanks for using leap year checker!")
         break   
