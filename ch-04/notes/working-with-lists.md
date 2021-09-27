# Working with Lists

## Looping Through an Entire List (for loop)

- **Looping** allows you to take the same action, or set of actions, with every item in a list.

### A Closer Look at Looping

```py
magicians = ['alice', 'david', 'carolina']
# For every magician in the list of magicians, print the magician’s name.
for magician in magicians:
 print(magician)
```

- you can choose any name for the **temporary variable** that holds each value in the list. However, it’s helpful to choose a **meaningful name** that represents a single item from the list.

- Every indented line following the for statement  line considered **inside the loop**

### Avoiding Indentation Errors

- Python uses indentation to determine when one line of code is connected to the line above it.
- These indentation levels help you gain a general sense of the overall program’s organization.
- When Python expects an indented block and doesn’t find one, it lets you know which line it had a problem with.

    ```py
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    ```

- A **logical error** happens when *The syntax is valid Python code*, but the *code does not produce the desired result* because a problem occurs in its logic.

    ```py
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n") # Forgetting to Indent Additional Lines
    ```

    ```py
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print("I can't wait to see your next trick, " + magician.title() + ".\n")
        print("Thank you everyone, that was a great magic show!") # Indenting Unnecessarily Line
    ```

- If you accidentally indent a line that doesn’t need to be indented, Python informs you about the unexpected indent

    ```py
    message = "Hello Python world!"
        print(message)
    ```

### Forgetting the Colon

- The colon at the end of a for statement tells Python to interpret the next line as the start of a loop.

## Making Numerical Lists

### Using the `range()` Function

- The range() function causes Python to *start counting at the first value* you give it, and it *stops when it reaches the second value* you provide.

```py
for value in range(1,5):
print(value) # 1 2 3 4
```

### Using `range()` to Make a List of Numbers

- If you want to make a list of numbers, you can convert the results of `range()` directly into a list using the `list()` function.

```py
numbers = list(range(1,6))
print(numbers)
```

- skip numbers in a given range.

```py
even_numbers = list(range(2,11,2))
print(even_numbers) # [2, 4, 6, 8, 10]

numbers = list(range(2,11,3))
print(numbers) #  [2, 5, 8]
```

- make a list of the first 10 square numbers

```py
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
```

### Simple Statistics with a List of Numbers

```py
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # 0
print(max(digits)) # 9
print(sum(digits)) # 45
```

### List Comprehensions

- A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.

```py
# List of Numbers 1 - 10
numbers = [value for value in range(1,11)]
print(numbers) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List of square numbers 1 - 10
squares = [value**2 for value in range(1,11)]
print(squares) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

- To use this syntax, begin with a descriptive name for the list, such as squares. Next, open a set of square brackets and define the expression for the values you want to store in the new list. In this example the expression is value**2, which raises the value to the second power. Then, write a for loop to generate the numbers you want to feed into the expression, and close the square brackets.

## Working with Part of a List

### Slicing a List

- To make a slice, you specify the index of the first and last elements you
want to work with.

```py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # ['charles', 'martina', 'michael']
```

- If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list

    ```py
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[:4])  #  ['charles', 'martina', 'michael', 'florence']
    ```

- If you omit the last index in a slice, Python automatically ends your slice at the end of the list

    ```py
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[2:]) # ['michael', 'florence', 'eli']
    ```

- A negative index returns an element a certain distance from the end of a list

    ```py
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[-3:]) # ['michael', 'florence', 'eli']
    ```

### Looping Through a Slice

- You can use a slice in a for loop if you want to loop through a subset of the elements in a list.

```py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    # Here are the first three players on my team:
    # Charles
    # Martina
    # Michael
```

### Copying a List

- To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index `([:])`

```py
my_foods = ['pizza', 'falafel', 'carrot cake']
# copy the list
friend_foods = my_foods[:]
# append a new element
friend_foods.append('koshary')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```

- If we had simply set friend_foods equal to my_foods, we would not produce two separate lists.

```py
my_foods = ['pizza', 'falafel', 'carrot cake']
# This doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```

- Instead of storing a copy of `my_foods` in `friend_foods` we set `friend_foods` equal to `my_foods`. This syntax actually tells Python to connect the new variable `friend_foods` to the list that is already contained in `my_foods` , so now both variables point to the same list. As a result, when we add 'cannoli' to `my_foods`, it will also appear in `friend_foods`. Likewise 'ice cream' will appear in both lists, even though it appears to be added only to `friend_foods`.
