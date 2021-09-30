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
