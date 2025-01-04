#Program to show linear time complexity(O(n)) by entering any n.


def lintimecom(n):
    iteration=0
    for i in range(1,n+1):
      iteration+=1

    print("for number ",n,"iteration are",iteration)


lintimecom(600)
lintimecom(700)