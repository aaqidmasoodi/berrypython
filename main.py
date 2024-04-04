name: str = 'Aaqid'
age: int = 24
salary: int = 2300

# 5 ways of doing formatting
# I am Aaqid and I am 24 and I make $2300 per hour.

# Method 1
print('I am', name, 'and I am', age, 'and I make $', salary, 'per hour')

# Method 2
print('I am '+name+' and I am '+ str(age) + ' and I make $'+str(salary)+' per hour.')

# Method 3
print('I am %s and I am %s and I make $%s per hour' %(name, age, salary))

# Method 4
print('I am {} and I am {} and I make ${} per hour'.format(name, age, salary))

# Method 5
print(f'I am {name} and I am {age} and I make ${salary} per hour.')