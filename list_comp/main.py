numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_num = [num+1 for num in numbers]
print(numbers)
print(new_num)
print("==================")
challenge = [num*2 for num in range(1,5) if num%2==0]
print(challenge)


numbers2 = {"one":1,"two":2,"three":3}
new_num2 = {key:value for (key,value) in numbers2.items() if value%2==0}

print(new_num2)
