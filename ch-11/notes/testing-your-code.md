# Testing Your Code

> *Every programmer makes mistakes*, so every programmer must test their code often, catching problems before users encounter them.

## Testing a Function

### Unit Tests and Test Cases

- A **unit test** verifies that one specific aspect of a function’s behavior is correct.
- A test case is a collection of unit tests that together prove that a function behaves as it’s supposed to, within the full range of situa- tions you expect it to handle.
- It’s often good enough to write tests for your code’s critical behaviors and then aim for full coverage only if the project starts to see widespread use.

### Make a test

```py

# name_function
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()


# test_name_function.py
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
```

1. First, we import **unittest** and **the function we want to test**
2. we create a **class** called NamesTestCase , which will contain a series of unit tests
3. the class inherits from the class **unittest.TestCase**
4. the class includes methods each one tests one aspect of function
5. The method must start with `test_`
6. Within the *test method*, we call the function we want to test and store a return value that we’re interested in testing.
7. we use Assert methods that verifies that a result you received matches the result you expected to receive. we use `assertEqual()`
8. Run the test by calling `unittest.main()`

### Failed test message

```bash
E # tells us one unit test in the test case resulted in an error
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase)
Do names like 'Janis Joplin' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Python_Crash_Course-Notes/ch-11/notes/code_snippets/test_name_ function.py", line 8, in test_first_last_name
    formatted_name = get_formatted_name('janis', 'joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

### Responding to a Failed Test
