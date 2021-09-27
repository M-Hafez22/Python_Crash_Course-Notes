# Dictionaries

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
- you can use a *key* to access the *value* associated with that key.
- A key’s value can be a *number*, a *string*, a *list*, or even another *dictionary*.

### Accessing Values in a Dictionary

- To get the value associated with a key, give the *name of the dictionary* and then place the *key* inside a set of square brackets

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
