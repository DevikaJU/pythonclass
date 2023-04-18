#read a string
#find the most occuring letter

string=input("Enter a string:")
counter={}
#store letter occurances
for i in string:
    if not i in counter:   #seeing this for the first time
        counter[i]=1
    else:
        counter[i]=counter[i]+1

maxSoFar=0
maxOccuringLetter=""
for i in counter:     #going through each key in the given dictionary
    if counter[i]>maxSoFar:
        maxOccuringLetter=i
        maxSoFar=counter[i]
print("Most occuring letter is:",maxOccuringLetter)
print("count of the most occuring letter is:",maxSoFar)





