n=int(input("Enter the number:"))
start=int(input("Enter the start of range:"))
end=int(input("Enter the end of range:"))
even_number=[]
odd_number=[]
for num in range(start,end+1):
    if num%2==0:
        even_number.append(num)
    else:
        odd_number.append(num)
print("Even number",even_number)
print("Total Even number",len(even_number))
print("Odd number",odd_number)
print("Total odd number:",len(odd_number))
def odd_even():
    if n%2==0:
        print("The number is even")
    else:
        print("The number is odd")
odd_even()
divisors=[2,3,4,5,6,8,10]
print(f"Divisibility check{n}")
for d in divisors:
    if n%d==0:
        print(f"{n} is divisible by {d}")
    else:
        print(f"{n} is not divisible by {d}")