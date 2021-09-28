# Functions

> *Functions* are named blocks of code that are designed to **do one specific job**.

- [Defining a Function](#defining-a-function)

## Defining a Function

- **Docstrings** are enclosed in triple `"""Docstrings"""` quotes, which Python looks for when it generates documentation for the functions in your programs.
- To call a function, you write the name of the function, followed by any necessary information in parentheses

```py
def greet_user():
  """Display a simple greeting."""
  print("Hello!")

greet_user()
```

### Passing Information to a Function

```py
def greet_user(username):
  """Display a simple greeting."""
  print("Hello, " + username.title() + "!")

greet_user('jesse')
```

### Arguments and Parameters

- **parameter**, a piece of information the function needs to do its job.

- **Argument**, is a piece of information that is passed from a function call to a function.

## Passing Arguments

Passing Arguments functions:

1. positional arguments:  which need to be in the same order the parameters were written
2. keyword arguments where each argument consists of a variable name and a value

### Positional Arguments

```py
def describe_pet(animal_type, pet_name):
  """Display information about a pet."""
  print("\nI have a " + animal_type + ".")
  print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
```

- You can get unexpected results if you mix up the order of the arguments in a function call when using positional arguments:

```py
def describe_pet(animal_type, pet_name):
  """Display information about a pet."""
  print("\nI have a " + animal_type + ".")
  print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry', 'hamster')
```

### Keyword Arguments

- A **keyword argument** is a **name-value pair** that you pass to a function.

```py
def describe_pet(animal_type, pet_name):
  """Display information about a pet."""
  print("\nI have a " + animal_type + ".")
  print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')
```

- The order of keyword arguments doesn’t matter because Python knows where each value should go.

### Default Values

- you can define a default value for each parameter.
- If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value.

```py
def describe_pet(pet_name, animal_type='dog'):
  """Display information about a pet."""
  print("\nI have a " + animal_type + ".")
  print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(pet_name='willie')
# describe_pet() # describe_pet() missing 1 required positional argument: 'pet_name'
```

> When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly.

### Equivalent Function Calls

> It doesn’t really matter which calling style you use. As long as your function calls produce the output you want, just use the style you find easiest to understand.

### Avoiding Argument Errors

- Python reads the function’s code for us and tells us the names of the arguments we need to provide. so **Give your variables and functions descriptive names**. If you do, Python’s error messages will be more useful.