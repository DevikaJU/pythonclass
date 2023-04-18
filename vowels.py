x=input("Enter the word:")
vowels =[]
y=['a','e','i','o','u']
for i in x:
    for j in y:
        if i==j:
            vowels.append(i)
print("The vowels in the word are ",vowels)