# Dictionaries

- [A Simple Dictionary](#a-simple-dictionary)
- [Working with Dictionaries](#working-with-dictionaries)
- [Looping Through a Dictionary](#looping-through-a-dictionary)
- [Nesting](#nesting)

## A Simple Dictionary

- dictionary is wrapped in braces `{}`, with a series of `key: value` pairs inside the braces. Every key
  is connected to its value by a colon `:`, and individual key-value pairs are separated by commas `,`.

```py
alien_0 = {
  'color': 'green',
  'points': 5
}

print(alien_0['color'])
print(alien_0['points'])
```

## Working with Dictionaries

- A dictionary in Python is a collection of key-value pairs.
- you can use a _key_ to access the _value_ associated with that key.
- A key’s value can be a _number_, a _string_, a _list_, or even another _dictionary_.

### Accessing Values in a Dictionary

- To get the value associated with a key, give the _name of the dictionary_ and then place the _key_ inside a set of square brackets

```py
alien_0 = {'color': 'green'}
print(alien_0['color'])
```

### Adding New Key-Value Pairs

```py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

### Starting with an Empty Dictionary

- To start filling an empty dictionary, define a dictionary with an empty set of braces and then add each key-value pair on its own line.

```py
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
```

### Modifying Values in a Dictionary

```py
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

#change the color
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
```

### Removing Key-Value Pairs

- you can use the `del` statement to completely remove a key-value pair.

```py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# Deleting key-value pair permanently.
del alien_0['points']
print(alien_0)
```

### A Dictionary of Similar Objects

```py
favorite_languages = {
    'hafez': 'JavaScript',
    'edward': 'JavaScript',
    'jen': 'python',
    'linus': 'c',
    'phil': 'python',
    'kyle': 'JavaScript',
}
```

> It’s good practice to include a comma `,` after the last key-value pair as well.

## Looping Through a Dictionary

### Looping Through All Key-Value Pairs

```py
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items():
  print("\nKey: " + key)
  print("Value: " + value)
```

- The method `items()` **returns a list of key-value pairs**.
- Notice again that **the key-value pairs are not returned in the order in which they were stored**, even when looping through a dictionary. Python doesn’t care about the order in which key-value pairs are stored; **it tracks only the connections between individual keys and their values**.

### Looping Through All the Keys in a Dictionary

- The `keys()` method is useful when you don’t need to work with all of the values in a dictionary.

```py
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

# use keys() TO looping through the dictionary
for name in favorite_languages.keys():
  print(name.title())

# Looping through the keys is actually the default behavior when looping through a dictionary
for name in favorite_languages:
  print(name.title())
```

- You can also use the keys() method to find out if the dictionary have a specific key

```py
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

if 'erin' in favorite_languages.keys():
  print("Erin, thanks for your poll")
else:
  print("Erin, please take our poll!")
```

### Looping Through a Dictionary’s Keys in Order

- you never get the items from a dictionary in any predictable order.
- You can use the `sorted()` function to get a copy of the keys in order

```py
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

# Sorting keys list temporarily before the looping through it.
for name in sorted(favorite_languages.keys()):
  print(name.title() + ", thank you for taking the poll.")
```

### Looping Through All Values in a Dictionary

- The values() method returns a **list of values without any keys**.

```py
favorite_languages = {
  'hafez': 'JavaScript',
  'edward': 'JavaScript',
  'jen': 'python',
  'linus': 'c',
  'phil': 'python',
  'kyle': 'JavaScript',
}

print("The following languages have been mentioned:")

# Looping through a list of values
for language in favorite_languages.values():
  print(language.title())
```

- to selecting Values without repetition use `set()`

```py
favorite_languages = {
  'hafez': 'JavaScript',
  'edward': 'JavaScript',
  'jen': 'python',
  'linus': 'c',
  'phil': 'python',
  'kyle': 'JavaScript',
}

print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
  print(language.title())
```

> As you continue learning about Python, you’ll often find a built-in feature of the language that helps you do exactly what you want with your data.

## Nesting

- Sometimes you’ll want to store a set of dictionaries in a list or a list of items as a value in a dictionary. This is called nesting.

### A List of Dictionaries

```py
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

# print(aliens)

for alien in aliens:
  print(alien)
```

```py
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)

# Change aliens characteristics
for alien in aliens[0:3]:
  alien['color'] = 'yellow'
  alien['speed'] = 'medium'
  alien['points'] = 10


for alien in aliens[3:5]:
  alien['color'] = 'blue'
  alien['speed'] = 'fast'
  alien['points'] = 15

# Show the first 5 aliens:
for alien in aliens[:5]:
  print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
```

### A List in a Dictionary

```py
# Store information about a pizza being ordered.
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
"with the following toppings:")

for topping in pizza['toppings']:
  print("\t" + topping)
```

```py
favorite_languages = {
'hafez': ['JavaScript', 'python'],
'linus': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
  print("\n" + name.title() + "'s favorite languages are:")
  for language in languages:
    print("\t" + language.title())
```

### A Dictionary in a Dictionary

```py
users = {
  'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
  },
  'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
  },
}

for username, user_infos in users.items():
  print("\nUsername: " + username)
  
  for user, user_info in user_infos.items():
    print(f"\t{user}: {user_info.title()}")

  # full_name = user_info['first'] + " " + user_info['last']
  # location = user_info['location']
  
  # print("\tFull name: " + full_name.title())
  # print("\tLocation: " + location.title())

```
