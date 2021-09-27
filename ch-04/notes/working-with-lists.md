# Working with Lists

- **Looping** allows you to take the same action, or set of actions, with every item in a list.

## Looping Through an Entire List (for loop)

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
