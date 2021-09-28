# User Input and while Loops

- [How the input() Function Works](#how-the-input()-function-works)

## How the input() Function Works

- The `input()` function pauses your program and waits for the user to enter some text, then it stores it in a variable.

```py
name = input("Please enter your name: ")
print("Hello, " + name + "!")
```

- The `input()` function takes one argument: the *prompt*
- The response is stored in the variable `name`

### Writing Clear Prompts

- Each time you use the `input()` function, you should include a clear, easy-to-follow prompt that tells the user exactly what kind of information you’re looking for.

- Add a space at the end of your prompts to separate the prompt from the user’s response and to make it clear to your user where to enter their text.

- You can store your **prompt** in a variable and pass that variable to the `input()` function. This allows you to build your **prompt** over several lines, then write a clean `input()` statement.

    ```py
    prompt = "If you tell us who you are, we can personalize the messages you see."
    prompt += "\nWhat is your first name? "
    name = input(prompt)
    print("\nHello, " + name + "!")
    ```

### Using int() to Accept Numerical Input

- When you use the input() function, Python interprets everything the user enters as a **string**.

```py
age = input("How old are you? ")
print(type(age))  # <class 'str'>

age = int(input("How old are you? "))
print(type(age)) # <class 'int'>
```

```py
height = int(input("How tall are you, in centimeters? "))

if height >= 36:
  print("\nYou're tall enough to ride!")
else:
  print("\nYou'll be able to ride when you're a little older.")
```

> When you use numerical input to do calculations and comparisons, be sure to convert the input value to a numerical representation first.

### The Modulo Operator

- The **modulo operator* (` % `)  divides one number by another number and returns the remainder

```py
4 % 3 # 1
5 % 3 # 2
6 % 3 # 0
```

- Determine if a number is *even* or *odd*:

    ```py
    number = int(input("Enter a number, and I'll tell you if it's even or odd: "))

    if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
    else:
    print("\nThe number " + str(number) + " is odd.")
    ```

### Accepting Input in Python 2.7

- If you’re using Python 2.7, you should use the `raw_input()` function when prompting for user input. This function interprets all input as a string, just as `input()` does in Python 3.

- Python 2.7 has an `input()` function as well, but this function interprets the user’s input as Python code and attempts to run the input. At best you’ll get an error that Python doesn’t understand the input; at worst you’ll run code that you didn’t intend to run. If you’re using Python 2.7, use `raw_input()` instead of `input()`.

## Introducing while Loops

- the while loop runs as long as, (or *while*), a certain condition is true.

### The while Loop in Action

- while loop counts from 1 to 5

```py
current_number = 1
while current_number <= 5:
print(current_number)
current_number += 1
```

### Letting the User Choose When to Quit

```py
# program instructions 
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' or 'q' to end the program. "
prompt += "\n>  "

# list of words to quit the program
quiting_words = ['quit', 'q', 'end', 'exit']

message = ""
while message not in quiting_words:
  message = input(prompt)
  if message not in quiting_words:
    print(message)
```

### Using a Flag

- For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False.

```py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' or 'q' to end the program. "
prompt += "\n>  "

# list of words to quit the program
quiting_words = ['quit', 'q', 'end', 'exit']

active = True

while active:
  message = input(prompt)
  if message in quiting_words:
    print("\nGame Over")
    active = False
  else:
    print(message)
```

### Using break to Exit a Loop

- Use the break statement to exit a while loop immediately without running any remaining code in the loop

```py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' or 'q' to end the program. "
prompt += "\n>  "

# list of words to quit the program
quiting_words = ['quit', 'q', 'end', 'exit']


while True:
  message = input(prompt)
  if message in quiting_words:
    print("\nGame Over")
    break # ends (break) the loop
  else:
    print(message)
```

- A loop that starts with `while` `True` will run forever unless it reaches a `break` statement.
- You can use the break statement in any of Python’s loops. For example, you could use break to quit a for loop that’s working through a list or a dictionary.

### Using continue in a Loop

- Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop based on the result of a conditional test.

- Printing even Numbers

    ```py
    current_number = 0

    while current_number < 10:
    current_number += 1
    if current_number % 2 != 0:
        continue # ignore the rest of the loop and return to the beginning.
    print(current_number)
    ```

### Avoiding Infinite Loops

- If your program gets stuck in an infinite loop, press ctrl-C or just close the terminal window displaying your program’s output.
- Make sure at least one part of the program can make the loop’s condition `False` or cause it to reach a break statement.