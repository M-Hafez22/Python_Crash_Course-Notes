# if Statements

- [Conditional Tests](#conditional-tests)
- [if Statement](#if-statement)
- [Using if Statements with Lists](#using-if-statements-with-lists)

```py
cars = ['audi', 'bmw', 'subaru', 'toyota', 'mg', 'kia']
for car in cars:
    if len(car) <= 3:
        print(car.upper())
    else:
        print(car.title())

# Audi
# BMW
# Subaru
# Toyota
# MG
# KIA
```

- The loop in this example first checks if the current length of the car name is less than 3 If it is, the value is printed in uppercase. If the length of the car name is not less than 3, it’s printed in title case

## Conditional Tests

- At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test.
- If a conditional test evaluates to `True`, Python *executes the code following* the if statement.
- If the test evaluates to `False`, Python *ignores the code following* the if statement.

### Checking for Equality

- the **equality operator** is `==`
- Conditional tests compare the *current value* of a variable to a *specific value* of interest. `age == 27`

- Testing for equality is **case sensitive**

    ```py
    car = 'bmw'
    print(car == "BMW") # False
    ```

- if case doesn’t matter you can convert the variable’s value to lowercase

    ```py
    car = 'BMW'
    print(car.lower() == "bmw") #  True
    # the value stored in car has not been affected by the conditional test.
    ```

### Checking for Inequality

- the **Inequality operator** is `!=`

```py
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!") # Hold the anchovies!
```

### Numerical Comparisons

- test to see if two numbers are:
  - equal.

    ```py
    age = 30
    print(age == 30)
    ```

  - not equal.

    ```py
    age = 30
    print(age != 30)
    ```

  - less than

    ```py
    age = 30
    print(age < 30)
    ```

  - less than or equal to

    ```py
    age = 30
    print(age <= 30)
    ```

  - greater than

    ```py
    age = 30
    print(age > 30)
    ```

  - greater than or equal

    ```py
    age = 30
    print(age >= 30)
    ```

### Checking Multiple Conditions

- **Using `and` to Check Multiple Conditions**

  - To check whether two conditions are both True simultaneously.

  ```py
  age_0 = 22
  age_1 = 18
  print(age_0 >= 21 and age_1 >= 21) # False
  print(age_0 >= 21 and age_1 >= 18) # True
  ```

  > To improve readability, you can use parentheses around the individual tests, but they are not required.

- **Using `or` to Check Multiple Conditions**
  - The keyword `or` allows you to check multiple conditions as well, but it *passes when either or both of the individual tests pass*.

  ```py
  age_0 = 22
  age_1 = 18
  print(age_0 >= 21 or age_1 >= 21) # True
  age_0 = 18
  print(age_0 >= 21 or age_1 >= 21) # False
  ```

### Checking Whether a Value Is in a List

- To find out whether a particular value is already in a list, use the keyword `in`.

```py
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) # True
print('pepperoni' in requested_toppings) # False
```

### Checking Whether a Value Is Not in a List

- To find out whether a particular value is not already in a list, use the keyword `not in`.

```py
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
```

### Boolean Expressions

- A Boolean value is either `True` or `False`, just like the value of a conditional expression after it has been evaluated.
- Boolean values provide an efficient way to track the state of a program or a particular condition that is important in your program.

## if Statement

### Simple if Statements

- The simplest kind of if statement has one test and one action:

```py
if conditional_test:
  do something
```

```py
age = 27
if age >= 18:
    print("You are old enough to vote!")
```

### if-else Statements

- Often, you’ll want to *take one action when a conditional test passes* and a *different action in all other cases*.

```py
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

### The if-elif-else Chain

- Python runs each conditional test in order until one passes. When a test passes, the code following that test is executed and Python skips the rest of the tests.

- Determine a person’s admission rate?
  - Admission for anyone under age 4 is free.
  - Admission for anyone between the ages of 4 and 18 is $5.
  - Admission for anyone age 18 or older is $10.

  ```py
  age = 27

  if age < 4:
      print("Your admission cost is $0.")
  elif age < 18:
      print("Your admission cost is $5.")
  else:
      print("Your admission cost is $10.")
  ```

### Using Multiple elif Blocks

```py
age = 27
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
elif age < 25:
    print("Your admission cost is $10.")
else:
    print("Your admission cost is $15.")
```

### Omitting the else Block

- Python does not require an else block at the end of an if- elif chain.

```py
age = 27
if age < 4:
  price = 0
elif age < 18:
  price = 5
elif age < 65:
  price = 10
elif age >= 65:
  price = 5
print("Your admission cost is $" + str(price) + ".")
```

### Testing Multiple Conditions

- In this case, you should use a series of simple `if` statements with no `elif` or else blocks.

```py
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
  print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
  print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
  print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

## Using if Statements with Lists

### Checking for Special Items

```py
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
run_out_toppings = ['green peppers']

# loop through the list
for requested_topping in requested_toppings:
  # Check if the topping is run out
  if requested_topping in run_out_toppings:
    print("Sorry, we are out of green peppers right now.")
  else:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
```

### Checking That a List Is Not Empty

```py
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
requested_toppings = []
run_out_toppings = ['green peppers']

# checks if the list is empty
if requested_toppings:
  # loop through the list
  for requested_topping in requested_toppings:
    # Check if the topping is run out
    if requested_topping in run_out_toppings: 
      print("Sorry, we are out of green peppers right now.")
    else:
      print("Adding " + requested_topping + ".")
else:
  print("Are you sure you want a plain pizza?")

print("\nFinished making your pizza!")
```

### Using Multiple Lists

```py
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
    print("Adding " + requested_topping + ".")
  else:
    print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
```
