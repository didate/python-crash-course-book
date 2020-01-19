def get_formatted_name(first_name, last_name):
    full_name = first_name+' '+last_name
    return full_name


print(get_formatted_name('Mamadou Lamarana', 'DIALLO'))


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('Mamadou Lamarana', 'DIALLO')
print(musician)
print('-----------------------------')
musician = build_person('Mamadou Lamarana', 'DIALLO', 28)
print(musician)
