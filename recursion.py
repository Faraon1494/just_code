def list_sum(ls,i=0):
    if i==len(ls):
        return 0
    else:
        return ls[i]+list_sum(ls,i+1)

ls=[1,2,3,4,5,6]
print(list_sum(ls))

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
    
print(factorial(5)) # 5! 1*2*3*4*5