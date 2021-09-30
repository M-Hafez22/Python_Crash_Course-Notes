# Files and Exceptions

## Reading from a File

### Reading an Entire File

```py
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
```

- **with**
  - The keyword `with` **closes the file** once access to it is no longer needed.
  - Notice how we call `open()` in this program but not `close()`. You could open and close the file by calling `open()` and `close()`, but if a bug in your program prevents the `close()` statement from being executed, the file may never close.

- **open()**
  - The `open()` function needs one argument **the name of the file** you want to open.
  - The `open()` function returns an object representing the file.

- **read()**
  - we use the `read()` method to read the entire contents of the file and *store it as one long string in contents*.
  - `read()` returns an empty string when it reaches the end of the file. this empty string shows up as a blank line.
    - to remove the extra blank line use `rstrip()`
        `print(contents.rstrip())`

### File Paths

- Python looks for the file in the directory where the program that’s currently being executed is stored.
- A **relative file path** tells Python to look for a given location relative to the directory where the currently running program file is stored.
  - On Linux and OS X use *forward slashes* `/`:
    `with open('file_path/filename.txt') as file_object:`
  - On Windows systems use *backslashes* `\`: 
    `with open('file_path\filename.txt') as file_object:`
- **absolute file** is the location from the root to the directory where the currently running program file is stored.

### Reading Line by Line

```py
"""Reading Line by Line"""
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
```

### Making a List of Lines from a File

- When you use `with`, the file object returned by `open()` **is only available inside the `with` block** that contains it. If you want to retain access to a file’s contents outside the `with` block, you can **store the file’s lines in a list inside the block** and then work with that list.

- the readlines() method takes each line from the file and stores it in a list.

```py
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```

### Working with a File’s Contents

```py
filename = 'pi_digits.txt'
# Opens the file
with open(filename) as file_object:
    # read the file line by line
    lines = file_object.readlines()

# Creates holder for the string
pi_string = ''

# loops through the lines
for line in lines:
    # appand the line to the string
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
```

> When Python reads from a text file, it interprets all text in the file as a string. If you read in a number and want to work with that value in a numerical context, you’ll have to convert it to an integer using the `int()` function or convert it to a float using the `float()` function.

### Large Files: One Million Digits

> Python has no inherent limit to how much data you can work with; you can work with as much data as your system’s memory can handle.

## Writing to a File

### Writing to an Empty File

- To write text to a file, you need to call `open()` with a second argument `w` that tells Python that we want to open the file in **write mode**.

```py
filename = 'programming.txt'

# Opens the file in write mode
with open(filename, 'w') as file_object:
  # writes a string to the file
  file_object.write("I love programming.")
```

- You can open a file
  - in *read* mode `('r')`
  - *write* mode `('w')`
  - *append* mode `( 'a')`
  - or a mode that allows you to **read and write** to the file `('r+')`.
  - If you omit the mode argument, Python opens the file in **read-only mode** by default.

- The open() function automatically creates the file
- If the was exist python will erase the file before returning the file object.

> Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the `str()` function.

### Writing Multiple Lines

- The `write()` function doesn’t add any newlines to the text you write.

```py
filename = 'programming.txt'

with open(filename, 'w') as file_object:
  file_object.write("I love programming.")
  file_object.write("I love creating new games.")
```

- Including newlines in your `write()` statements makes each string appear on its own line:

```py
filename = 'programming.txt'

with open(filename, 'w') as file_object:
  file_object.write("I love programming.\n") # Ends every line with \n to end the line
  file_object.write("I love creating new games.\n")
```

### Appending to a File

- To append a string to a file use *append* mode `( 'a')`
- When you open a file in append mode, Python doesn’t erase the file before returning the file object.
- Any lines you write to the file will be added at the end of the file.

```py
filename = 'programming.txt'

with open(filename, 'a') as file_object:
  file_object.write("I also love finding meaning in large datasets.\n")
  file_object.write("I love creating apps that can run in a browser.\n")
```

## Exceptions

- Exceptions are handled with `try-except` blocks. A `try-except` block asks Python to do something, but it also tells Python what to do if an exception is raised. When you use `try-except` blocks, your programs will continue running even if things start to go wrong. Instead of tracebacks, which can be confusing for users to read, users will see friendly error messages that you write.

### Using try-except Blocks

- You tell Python to try running some code, and you tell it what to do if the code results in a particular kind of exception.

```py
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

- We put print(5/0), the line that caused the error, inside a try block. If the code in a try block works, Python skips over the except block. If the code in the try block causes an error, Python looks for an except block whose error matches the one that was raised and runs the code in that block.

### Using Exceptions to Prevent Crashes

- We can make the program more error resistant by wrapping the line that might produce errors in a `try-except` block.

```py
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("\nYou can't divide by 0!")
    else:
        print(answer)
```

### Handling the FileNotFoundError Exception

```py
filename = 'alice.txt'

try:
  with open(filename) as f_obj:
    contents = f_obj.read()
except FileNotFoundError:
  msg = "Sorry, the file " + filename + " does not exist."
  print(msg)
```

### Analyzing Text

- Let’s pull in the text of Alice in Wonderland and try to *count the number of words in the text*. We’ll use the string method `split()`, **which can build a list of words from a string**. Here’s what `split()` does with a string containing just the title "Alice in Wonderland":

```py
title = "Alice in Wonderland"
print(title.split()) # ['Alice', 'in', 'Wonderland']
```

### Working with Multiple Files

> word_count.py

```py
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
```

- Using the try-except block in this example provides two significant advantages:
  - We prevent our users from seeing a traceback
  - we let the program continue analyzing the texts it’s able to find.

### Failing Silently

- In the previous example, we informed our users that one of the files was unavailable. But you don’t need to report every exception you catch. Sometimes you’ll want the program to fail silently when an exception occurs and continue on as if nothing happened.

- To make a program fail silently, you write a try block as usual, but you explicitly tell Python to do nothing in the except block.

```py
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # if it failed do nothing
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
```

### Deciding Which Errors to Report

- Giving users information they aren’t looking for can decrease the usability of your program. Python’s error-handling structures give you finegrained control over how much to share with users when things go wrong; *it’s up to you to decide how much information to share*.
