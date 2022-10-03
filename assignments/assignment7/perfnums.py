def sum_of_factors(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum

def decide(num):
    sum = sum_of_factors(num)
    if sum > num:
        return f"{num} is abundant."
    elif sum < num:
        return f"{num} is deficient."
    elif sum == num:
        return f"{num} is a perfect number."
