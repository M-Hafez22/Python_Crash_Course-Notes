# Data Types

- [Strings](#strings)

## Strings

- [How to make a String](#how-to-make-a-string)
- [Changing Case in a String with Methods](#changing-case-in-a-string-with-methods)
- [Combining or Concatenating Strings](#combining-or-concatenating-strings)
- [Adding Whitespace to Strings with Tabs or Newlines](#adding-whitespace-to-strings-with-tabs-or-newlines)
- [Stripping Whitespace](#stripping-whitespace)
- [Avoiding Syntax Errors with Strings](#avoiding-syntax-errors-with-strings)
- [Printing in Python 2](#printing-in-python-2)


### How to make a String

- A string is simply a series of characters.
- Anything inside quotes (single or double) is considered a string in Python

  ```py
  "This is a string."
  'This is also a string.'
  ```

### Changing Case in a String with Methods

- You can use *Methods* to change the case in a string.

```py
name = "mOhamEd  hAfEZ"
# titlecase: where each word begins with a capital letter.
print(name.title()) # Mohamed  Hafez

# change a string to all uppercase letters.
print(name.upper()) # MOHAMED  HAFEZ

# change a string to all lowercase letters.
print(name.lower()) # mohamed  hafez
```

> A method is an action that Python can perform on a piece of data.
> Every method is followed by a set of parentheses, because methods often need additional information to do their work. That information is provided inside the parentheses.

### Combining or Concatenating Strings

- **concatenation**.

```py
first_name = "mohamed"
last_name = "Hafez"
# Using the plus symbol (+) to combine strings.
full_name = first_name + " " + last_name
print(full_name.title())
```

### Adding Whitespace to Strings with Tabs or Newlines

- In programming, **whitespace** refers to any nonprinting character, such as *spaces*, *tabs*, and *end-of-line* symbols.

```py
print("Python")
# \t: Adds a tab
print("\tPython")
# \n: Adds a newline
print("Languages:\n\tJavaScript\n\tPython\n\tC")
```

### Stripping Whitespace

- In programming ```'python'``` and ```'python '``` are two different strings.
- Python can look for extra whitespace on the right and left sides of a string.
- To ensure that no whitespace exists at the right end of a string, use
the **rstrip()** method.

```py
favorite_language = '   python   '
# Reomving Whitespaces Temporarily
print("(" + favorite_language + ")")
# Reomving whitespaces from the Right
print("(" + favorite_language.rstrip() + ")")
# Reomving whitespaces from the Left
print("(" + favorite_language.lstrip() + ")")
# Reomving whitespaces from the Right & Left
print("(" + favorite_language.strip() + ")")

# Reomving Whitespaces Permanently
favorite_language = favorite_language.strip()
print("(" + favorite_language + ")")
```

### Avoiding Syntax Errors with Strings

- A **syntax error** occurs when Python doesn’t recognize a section of your program as valid Python code.

```py
# message = 'One of Python's strengths is its diverse community.' 
message = "One of Python's strengths is its diverse community."
print(message)

```

### Printing in Python 2

- In *Python 2* Parentheses are not needed around the phrase you want to print
  ```print "Hello Python 2.7 world!"```
- But in *Python 3* print is a function.
