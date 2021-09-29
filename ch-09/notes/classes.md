# Classes

```py
# By convention, **capitalized** names refer to classes in Python.
class Dog():
    # the docstring describes what this class does.
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
```

## Creating a Class

- By convention, **capitalized** names refer to classes in Python.
- A function that’s part of a class is a **method**
- *methods* are like the function in everything except **the way we call it**.
- The `__init__()` method at w is a special method Python runs automatically whenever we create a new instance based on the
Dog class.
- We define the `__init__()` method to have three parameters:
  - `self` : is required in the method definition, and it must come first before the other parameters. It must be included in the definition because when Python calls this `__init__()` method later , the method call will automatically **pass the `self` argument**. which is **a reference to the instance itself**.
  - The two variables defined at x each have the prefix `self`. Any variable prefixed with `self` **is available to every method in the class**
  - `self.name = name` takes the value stored in the parameter name and stores it in the variable name, which is then attached to the instance being created.
  - Variables that are accessible through instances like this are called **attributes**.

## Making an Instance from a Class

- **Accessing Attributes**: To access the attributes of an instance, you use dot notation.

```py
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
```

- **Calling Methods**: we can use dot notation to call any method defined in the class

```py
my_dog = Dog('willie', 6)

my_dog.roll_over()
my_dog.sit()
```

- **Creating Multiple Instances**

```py
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
```
