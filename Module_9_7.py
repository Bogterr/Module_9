# Декораторы - урок

# def null_decorator(func):
#     def wrapper(name):
#         original_result = func(name)
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
#
#
# @null_decorator
# def greet(name):
#     return f"Hello, {name}!"

# greet = null_decorator(greet)

# inp_name = input("Enter your name: ")
# hello = greet(inp_name)
#
# print(hello)

# print('\n' * 3)


###############################
def is_prime(sum_func):
    def wrapper(*args, **kwargs):

        result = sum_func(*args, **kwargs)

        if result > 1:
            if all((result % i != 0) for i in range(2, int(result**0.5) + 1)):
                print('Простое')
                return result
            else:
                print('Составное')
                return result
    return wrapper


@is_prime
def sum_three(first_num, second_num, third_num):
    summa = first_num + second_num + third_num
    return summa
###############################

result = sum_three(2, 3, 6)
print(result)