name = input('Enter your name: ')
age = int(input('Enter your age: '))

current_year = 2023
birth_date = current_year - age

# print('Hello, ' + name + '! You are ' + str(age) +
#       ' years old, so you were born in year ' + str(birth_date) + '.')
# print('Hello, % s! You are % s years old, so you were born in year % s.' %
#       (name, age, birth_date))
# print('Hello, {}! You are {} years old, so you were born in year {}.'.format(
#     name, age, birth_date))
print(
    f'Hello, {name}! You are {age} years old, so you were born in year {birth_date}.')
