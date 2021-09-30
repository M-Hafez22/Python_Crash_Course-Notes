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
