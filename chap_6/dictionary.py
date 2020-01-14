alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
print('------------------------------')

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for k, v in user_0.items():
    print(k+" => "+v)

print('------------------------------')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for key in favorite_languages.keys():
    print(key.title())

print('------------------------------')

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
