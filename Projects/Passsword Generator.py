import random as ra

def Pm(i, n):
    alpha = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    nums = ['1','2','3','4','5','6','7','8','9','0']
    signs = ['!','@','#','$','%','&','?','/'] 
    if i == n:
        return
    if i == 1:
        print(alpha[ra.randint(0, len(alpha) - 1)], end="")
    Assign = ra.randint(1,3)
    if Assign == 1:
        print(alpha[ra.randint(0, len(alpha) - 1)], end="")
    elif Assign == 2:
        print(nums[ra.randint(0, len(nums) - 1)], end="")
    elif Assign == 3:
        print(signs[ra.randint(0, len(signs)- 1)], end="")
    Pm(i + 1, n)

Pm(1, int(input("Enter the length of the password : ")))