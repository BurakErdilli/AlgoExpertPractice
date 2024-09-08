

# o(n^2) time, o(1) space
def twoNumberSum_1(array,targetSum):
    for i in range(len(array)-1):
        firstNum= array[i]
        for j in range (i+1,len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum,secondNum]
            
    return


# o(n) time, o(n) space
def twoNumberSum_2(array,targetSum):
    nums= {}
    for num in array:
        if targetSum- num in nums:
            return [targetSum- num,num]
        
        else: nums[num]= True
        
    return
        
        
        
# o(n^2) time, o(1) space
def twoNumberSum_3(array,targetSum):
    array=sorted(array)
    i=0
    j=len(array)-1
    while i<j:
        currentSum=array[i]+array[j]
        if currentSum<targetSum:
            i+=1 
        elif currentSum>targetSum:
            j-=1
        else: return[array[i],array[j]]
    return

    
    
    
    
    

array=[1,-4,3,8,-1,11,6,5]

targetSum=13

couple1 = twoNumberSum_1(array, targetSum)
couple2 = twoNumberSum_2(array, targetSum)
couple3 = twoNumberSum_3(array, targetSum)
