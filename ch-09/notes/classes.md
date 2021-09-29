# Classes

- [Creating a Class](#creating-a-class)
- [Making an Instance from a Class](#making-an-instance-from-a-class)
- [Working with Classes and Instances](#working-with-classes-and-instances)
- [Inheritance](#inheritance)
- [Importing Classes](#importing-classes)
- [The Python Standard Library](#the-python-standard-library)
- [Styling Classes](#styling-classes)

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

## Inheritance

- When one class *inherits* from another, it automatically **takes on all the attributes and methods of the first class and also free to define new attributes and methods of its own**.
- The original class is called the *parent class*, and the new class is the *child class*.

### The __init__() Method for a Child Class

```py
from car import Car

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```

- The `super()` function is a special function that helps Python **make connections between the parent and child class**.

> The name *super* comes from a convention of calling the parent class a *superclass* and the child class a *subclass*.

### Defining Attributes and Methods for the Child Class

- Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary to differentiate the child class from the parent class.

### Overriding Methods from the Parent Class

- You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class.
- To do this, you define a method in the child class with the same name as the method you want to override

### Instances as Attributes

- If your class becomes lengthy, You can break your large class into smaller classes that work together.
- You can pass a class as an attribute to another class

```py
from car import Car

class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

### Modeling Real-World Objects

> Focus on the ***Logic*** behind the code, not just the *syntax*
> Don’t be discouraged if you find you’re ripping apart your classes and rewriting them several times using different approaches. In the quest to write accurate, efficient code, everyone goes through this process.

## Importing Classes

> once your classes work as you want them to, you can leave those files alone and focus on the *higher-level logic* of your main program.

- **Importing a Single Class**
  `from module_name import Class_name`
- **Importing Multiple Classes from a Module**
  - You import multiple classes from a module by separating each class with a comma `.`
  `from module_name import Class_name_1, Class_name_2`
- **Importing an Entire Module**
  - You can also import an entire module and then access the classes you need using dot notation.
  `import module_name`
  `module_name.class_name`
- **Importing All Classes from a Module**
  `from module_name import *`
  - This method is not recommended for two reasons:
    1. it’s helpful to be able to read the import statements at the top of a file and get a clear sense of which classes a program uses.
    2. can also lead to confusion with names in the file.

## The Python Standard Library

- The Python standard library is a set of modules included with every Python installation.
- You can use any function or class in the standard library by including a simple import statement at the top of your file. Let’s look at one class, OrderedDict, from the module collections.

## Styling Classes

- Class names should be written in **CamelCaps**.
- **Instance** and **module** names should be written in **lowercase with underscores** between words.
- Every class should have a **docstring** immediately following the class definition.
- Each module should also have a docstring.
- You can use blank lines to organize code, Within a class you can use *one blank line between methods*, and within a module you can use *two blank lines to separate classes*.
- place the import statement for the standard library module first. Then add a blank line and the import statement for the module you wrote.
