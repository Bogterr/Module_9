# Вызов разом

def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

print('1: ', apply_all_func([6, 20, 15, 9], max, min))
print('2: ', apply_all_func([6, 20, 15, 9], len, sum, sorted))