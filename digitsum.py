def digitsSum(j):
    ##Your code here
    res=0
    while j>0:
        res+=j%10
        j=j//10
    return res
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        print(digitsSum(a))
        testcases-=1
        


if __name__=='__main__':
    main()
        
