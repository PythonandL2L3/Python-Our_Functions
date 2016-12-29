## This is the Module. This function reverses the numbers.

def reverse_num(n):
    
    rev=0
    while n>0:
          rem=n%10
          rev=rev*10+rem
          n /=10
    print rev
    return rev
    
 ###This is calling function. Here 'reverse' is the module.
 
 import reverse

 print reverse.reverse_num(1234)
