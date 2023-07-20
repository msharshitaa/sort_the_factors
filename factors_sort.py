def factors_sort(num):
    i = 1
    factor_count = 0
    while i * i <= num:
        if num % i == 0:
            if num // i == i:
                factor_count += 1
            else:
                factor_count += 2
        i += 1
    return factor_count

def factor_sort(array):
    array.sort(key=lambda num: (factors_sort(num), num)) 
    return array
array = list(map(int, input().split()))
print(factor_sort(array))
