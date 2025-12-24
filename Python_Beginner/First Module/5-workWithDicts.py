person = {
    'name': 'Rodrigo',
    'age':'18'
}

print(person)
print(person['name'])
print(person['age'])

# Methods
print(person.keys())
print(person.values())
print(person.items())

# Update Method
new_method = {'profession': 'dev'}
person.update(new_method)
print(person)