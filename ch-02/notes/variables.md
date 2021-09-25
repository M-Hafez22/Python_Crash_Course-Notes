# Variables

- [Naming and Using Variables](#naming-and-using-variables)
- [Avoiding Name Errors When Using Variables](#avoiding-name-errors-when-using-variables)

## Naming and Using Variables

- Variable names can contain only **letters, numbers, and underscores**.
- They can start with a **letter or an underscore** but not with a number.
- **Spaces are not allowed** in variable names.
- Avoid using **Python keywords and function names** as variable names;
- Variable names should be **short but descriptive**.
  - For example
    ```name``` is better than ```n```,
    ```student_name``` is better than ```s_n```,
    ```name_length``` is better than ```length_of_persons_name```.

> The Python variables you’re using at this point should be **lowercase**. You won’t get errors if you use uppercase letters, but it’s a good idea to avoid using them for now.

## Avoiding Name Errors When Using Variables

- The interpreter provides a traceback when a program cannot run successfully. A **traceback** is a record of where the interpreter ran into trouble when trying to execute your code.

```bash
Traceback (most recent call last):
File "hello_world.py", line 2, in <module>
 print(mesage)
NameError: name 'mesage' is not defined
```
