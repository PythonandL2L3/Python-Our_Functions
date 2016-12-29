## This is the Module, which iam defining the function with varibles. This executes star pattern followed by by my name at center followed by star pattern

def star(a,b,c):

    a='*'*125
    b="Its me Naveen".center(139)
    c="*"*125
    print a,b,c
    
 ### This is the calling function. Here starpattern is module (file name), so importing module.
     
   import starpattern
   print starpattern.star(1,2,5)
