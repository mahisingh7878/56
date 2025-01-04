#Program to show time complexity(O(n^2)) by entering any n.
def timecomOn2(n):
    iteration=0
    for  i in range(0,n):
     for j in range(0,n):
        print("*",end="")
        iteration+=1
     print("")

    print("when n is ",n,"iteration is ",iteration)
          
timecomOn2(8)
timecomOn2(7)