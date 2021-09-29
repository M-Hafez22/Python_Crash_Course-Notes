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

## Working with Classes and Instances

> You can modify the attributes of an instance directly or write methods that update attributes in specific ways.

```py
class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_new_car = Car('audi', 'q3', 2021)
print(my_new_car.get_descriptive_name())
```

- **Setting a Default Value for an Attribute**
  - when setting a default value, it makes sense to specify this initial value in the body of the `__init__()` method; if you do this for an attribute, you don’t have to include a parameter for that attribute.

    ```py
    class Car():
        """A simple attempt to represent a car."""
        
        def __init__(self, make, model, year):
            """Initialize attributes to describe a car."""
            self.make = make
            self.model = model
            self.year = year
            # Create attribute with default value
            self.odometer_reading = 0
        
        def get_descriptive_name(self):
            """Return a neatly formatted descriptive name."""
            long_name = str(self.year) + ' ' + self.make + ' ' + self.model
            return long_name.title()

        def read_odometer(self):
            """Print a statement showing the car's mileage."""
            print("This car has " + str(self.odometer_reading) + " miles on it.")

    my_new_car = Car('audi', 'a4', 2016)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()
    ```

- **Modifying Attribute Values**
  - You can change an attribute’s value in three ways:
    1. you can change the value directly through an instance
    2. set the value through a method
    3. or increment the value (add a certain amount to it) through a method.

  - **Modifying an Attribute’s Value Directly**

    ```py
    # modify the default value
    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()
    ```

  - **Modifying an Attribute’s Value Through a Method**
    - It can be helpful to have methods that update certain attributes for you. Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.

    ```py
    # method to update the odometer_reading
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage
    
    # Updating the odometer_reading with the new value
    my_new_car.update_odometer(23)
    my_new_car.read_odometer()
    ```

  - **Incrementing an Attribute’s Value Through a Method**
    - Sometimes you’ll want to increment an attribute’s value by a certain amount rather than set an entirely new value.

    ```py
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
    my_used_car.increment_odometer(100)
    my_used_car.read_odometer()
    ```

> You can use methods like this to control how users of your program update values such as an odometer reading, but anyone with access to the program can set the odometer reading to any value by accessing the attribute directly. Effective security takes extreme attention to detail in addition to basic checks like those shown here.
