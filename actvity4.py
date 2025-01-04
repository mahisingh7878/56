def example_function(arr):
    n = len(arr)
    
    # Loop 1: O(n)
    for i in range(n):
        print(arr[i])
    
    # Loop 2: O(n^2)
    for i in range(n):
        for j in range(n):
            print(arr[i] + arr[j])
    
    # Loop 3: O(1)
    print("Done")
