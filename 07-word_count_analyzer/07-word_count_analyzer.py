from collections import Counter
#hello world my name is sampath name
print("Welcome to word count analyzer!!")
n=input("Enter words or sentence or paragrah:")
sentence=(n)
words=sentence.split()
count=Counter(words)
print("Total number of words:",len(words))
characters=len(n)
print("Total number of characters with space:",characters)
words_without_space=n.replace(" ","")
print("Total number of character without space:",len(words_without_space))
print("\n✌️  Word frequency:")

for word, count in Counter(words).items():
    print(word,":",count)
