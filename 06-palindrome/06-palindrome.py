print("Welcome to polindrome checker!!")
while True:
    n=(input("Enter a word ,phrase or a number to check (or type 'exit' to quit ):"))
    if n.lower()=='exit':
        print("Thank you for using palindrome checker!!!")
        break
    clean=(n.replace(" ","")).lower()
    if clean==clean[::-1]:
        print(f"{n} is a palindrome")
    else:
        print(f"{n} is not a palindrome")
