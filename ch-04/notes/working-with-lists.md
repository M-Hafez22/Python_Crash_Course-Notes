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
