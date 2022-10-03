def sum_of_range(f,l,j):
    sum=0
    for i in range(f,l+1,j):
        sum+=i
    return sum

print(sum_of_range(1, 10, 1))
