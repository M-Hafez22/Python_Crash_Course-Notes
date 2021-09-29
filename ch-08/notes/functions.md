# Functions

> *Functions* are named blocks of code that are designed to **do one specific job**.

- [Defining a Function](#defining-a-function)
- [Passing Arguments](#passing-arguments)
- [Return Values](#return-values)
- [Passing a List](#passing-a-list)
- [Passing an Arbitrary Number of Arguments](#passing-an-arbitrary-number-of-arguments)
- [Storing Your Functions in Modules](#storing-your-functions-in-modules)
- [Styling Functions](#styling-functions)

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

## Return Values

### Returning a Simple Value

- The *return* statement takes a value from inside a function and sends it back to the line that called the function.

```py
def get_formatted_name(first_name, last_name):

  """Return a full name, neatly formatted."""
  full_name = first_name + ' ' + last_name
  return full_name.title()

developer = get_formatted_name('mohamed', 'hafez')
print(developer)
```

- When you call a function that returns a value, you need to provide a variable where the return value can be stored.

### Making an Argument Optional

- You can use default values to make an argument optional.

```py
def get_formatted_name(first_name, last_name, middle_name=''):
  
  """Return a full name, neatly formatted."""
  if middle_name:
    full_name = first_name + ' ' + middle_name + ' ' + last_name
  else:
    full_name = first_name + ' ' + last_name
  return full_name.title()

developer = get_formatted_name('mohamed', 'hafez')
print(developer)
```

### Returning a Dictionary

```py
def build_person(first_name, last_name, age=''):
  """Return a dictionary of information about a person."""
  person = {'first': first_name, 'last': last_name}
  if age:
    person['age'] = age
  return person

developer = build_person('mohamed', 'hafez', age=27)
print(developer)
```

### Using a Function with a while Loop

```py
def get_formatted_name(first_name, last_name):
  """Return a full name, neatly formatted."""
  full_name = first_name + ' ' + last_name
  return full_name.title()

# This is an infinite loop!
while True:
  print("\nPlease tell me your name:")
  print("(enter 'q' at any time to quit)")

  f_name = input("First name: ")
  if f_name == 'q':
    break

  l_name = input("Last name: ")
  if l_name == 'q':
    break

  formatted_name = get_formatted_name(f_name, l_name)
  print("\nHello, " + formatted_name + "!")
```

## Passing a List

```py
def greet_users(names):
  """Print a simple greeting to each user in the list."""
  for name in names:
    message = "Hello, " + name.title() + "!"
    print(message)
    
usernames = ['Mohamed', 'hafez', 'mansour']
greet_users(usernames)
```

### Modifying a List in a Function

- When you pass a list to a function, the function can modify the list. Any changes made to the list inside the function’s body are permanent

```py
def print_models(unprinted_designs, completed_models):
  """
  Simulate printing each design, until none are left.
  Move each design to completed_models after printing.
  """
  while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

def show_completed_models(completed_models):
  """Show all the models that were printed."""
  print("\nThe following models have been printed:")
  for completed_model in completed_models:
    print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

> Every function should have one specific job.

### Preventing a Function from Modifying a List

- To prevent a function from midifying the list You can send a copy of the list to a function like this:

```py
function_name(list_name[:])
```

```py
def print_models(unprinted_designs, completed_models):
  """
  Simulate printing each design, until none are left.
  Move each design to completed_models after printing.
  """
  while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

def show_completed_models(completed_models):
  """Show all the models that were printed."""
  print("\nThe following models have been printed:")
  for completed_model in completed_models:
    print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Sending a copy of unprinted_designs list
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
# the unprinted_designs list still remain
print(unprinted_designs)
```

> It’s more efficient for a function to work with an existing list to avoid using the time and memory needed to make a separate copy, especially when you’re working with large lists

## Passing an Arbitrary Number of Arguments

```py
def make_pizza(*toppings):
  """Summarize the pizza we are about to make."""
  print("\nMaking a pizza with the following toppings:")
  for topping in toppings:
    print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

- The asterisk in the parameter name `*toppings` tells Python to make an empty tuple called `toppings` and pack whatever values it receives into this tuple.
- Note that Python packs the arguments into a tuple, even if the function receives only one value

### Mixing Positional and Arbitrary Arguments

- If you want a function to accept several *different kinds of arguments*, the parameter that accepts an **arbitrary number of arguments must be placed last in the function definition*.
- Python **matches positional and keyword arguments first** and then **collects any remaining arguments in the final parameter**.

### Using Arbitrary Keyword Arguments

```py
def build_profile(first, last, **user_info):
  """Build a dictionary containing everything we know about a user."""
  profile = {}
  
  profile['first_name'] = first
  profile['last_name'] = last
  
  for key, value in user_info.items():
    profile[key] = value
  
  return profile


def print_dictionary(dictionary):
  """Printing out the dictionary Keys with Values"""
  for key, value in dictionary.items():
    print(f'{key}: {value}')  


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print_dictionary(user_profile)
```

- The double asterisks before the parameter `**user_info` cause Python to create an empty dictionary called `user_info` and pack whatever name-value pairs it receives into this dictionary.

## Storing Your Functions in Modules

- You can store your functions in a separate file called a **module** and then **importing** that module into your main program.

> Storing your functions in a separate file allows you to hide the details of your program’s code and focus on its higher-level logic. It also allows you to reuse functions in many different programs.

### Importing an Entire Module

- A *module* is a file ending in .py that contains the code you want to import into your program.
- To **call a function from an imported module**, enter the name of the module you imported, followed by the name of the function, separated by a dot

- In **pizza.py** file we create the function that generate the pizza

  ```py
  def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    # print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    print(f"\nMaking a {str(size)}-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
  ```

- In **making_pizzas.py** we import the pizza file with all functions in it
- we access the function with `module_name.function_name()`

  ```py
  import pizza

  pizza.make_pizza(16, 'pepperoni')
  pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
  ```

### Importing Specific Functions

- You can also import a specific function from a module. Here’s the general syntax for this approach:
  `from module_name import function_name`
  `from module_name import function_0, function_1, function_2`

- With this syntax, you don’t need to use the dot notation when you call a function.

```py
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Using as to Give a Function an Alias

- The general syntax for providing an alias is:
  `from module_name import function_name as fn`

```py
from pizza import make_pizza as mp # making alias for make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Using as to Give a Module an Alias

- You can also provide an alias for a module name.
- The general syntax for this approach is:
  `import module_name as mn`

```py
import pizza as p # Now you can access all functions from pizza module with p.function

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Importing All Functions in a Module

- You can tell Python to import every function in a module by using the asterisk (`*`) operator:
- you can call each function by name without using the dot notation.

```py
from pizza import * # use all functions in pizza module with only it's name

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

> it’s best not to use this approach when you’re working with larger modules that you didn’t write
> The best approach is to import the function or functions you want, or import the entire module and use the dot notation.

## Styling Functions

- Functions should have **descriptive names**, and these names should use **lowercase letters** and underscores.
- Every function should have a **comment that explains concisely what the function does**. and use the docstring format.
- If you specify a default value for a parameter, **no spaces should be used on either side of the equal sign**:
  `def function_name(parameter_0, parameter_1='default value')`
- The same convention should be used for keyword arguments in function calls:
  `function_name(value_0, parameter_1='value')`
- If you have too many parameters separate them in lines
  - press **tab twice** to separate the list of arguments from the body of the function

  ```py
  def function_name(
      parameter_0, parameter_1, parameter_2,
      parameter_3, parameter_4, parameter_5):
    function body...
  ```

- separate functions by two blank lines.
- All import statements should be written at the beginning of a file.
