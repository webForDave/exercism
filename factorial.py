def factorial(num):
    if num == 0:
        return 1
    list_of_num = sorted([i for i in range(1, num+1)], reverse=True)
    product = 1

    for num in list_of_num:
        product *= num
    
    return product


print(factorial(4))