nums=[1,2,3,4,5,6]
target=7



def sol():
    solutions=[]
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+ nums[j]==target:
                solutions.append((i,j))
    print(solutions)
sol()

                   
                   