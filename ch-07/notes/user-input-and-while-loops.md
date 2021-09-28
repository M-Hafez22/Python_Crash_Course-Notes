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
